import os
import chromadb
from chromadb.utils import embedding_functions
import google.generativeai as genai
import networkx as nx
from typing import List, Dict, Any
import streamlit as st

# Lazy load function
@st.cache_resource
def get_collection():
    # Initialize ChromaDB
    # Persist in .cognitivespec/chroma
    CHROMA_PATH = os.path.join(os.getcwd(), ".cognitivespec", "chroma")
    os.makedirs(CHROMA_PATH, exist_ok=True)
    
    try:
        client = chromadb.PersistentClient(path=CHROMA_PATH)
    except Exception as e:
        print(f"ChromaDB Init Error: {e}")
        return None

    # Use default encoding (Sentence Transformers)
    try:
        ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    except Exception:
        print("SentenceTransformers not found, using default.")
        ef = None # Chroma default

    return client.get_or_create_collection(name="cognitivespec_docs", embedding_function=ef)

def add_documents(documents: List[Any]):
    """
    Adds documents to ChromaDB.
    """
    collection = get_collection()
    if not collection or not documents:
        return

    ids = [str(hash(doc.content)) for doc in documents]
    documents_text = [doc.content for doc in documents]
    metadatas = [doc.metadata for doc in documents]

    collection.upsert(
        ids=ids,
        documents=documents_text,
        metadatas=metadatas
    )

def query_rag(query: str, G: nx.DiGraph, chat_history: List[Dict[str, str]] = None) -> Tuple[str, Dict[str, int]]:
    """
    RAG Logic
    Returns: (answer_text, usage_dict)
    """
    api_key = os.getenv("GEMINI_API_KEY")
    empty_usage = {"prompt_token_count": 0, "candidates_token_count": 0, "total_token_count": 0}
    
    if not api_key:
        return "Please set GEMINI_API_KEY in Settings.", empty_usage

    collection = get_collection()
    if not collection:
        return "Vector Database unavailable.", empty_usage

    # 1. Vector Retrieval
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    
    retrieved_docs = results['documents'][0] if results['documents'] else []
    retrieved_metas = results['metadatas'][0] if results['metadatas'] else []

    # 2. Graph Expansion
    context_text = "Context from Documents:\n"
    related_nodes_info = []

    for i, doc_text in enumerate(retrieved_docs):
        context_text += f"---\n{doc_text}\n"
        source = retrieved_metas[i].get('source')
        if source and G:
            file_nodes = [n for n, attr in G.nodes(data=True) if attr.get('source_file') == source]
            for node in file_nodes:
                 neighbors = list(G.neighbors(node))
                 for neighbor in neighbors:
                     related_nodes_info.append(f"{node} -> {neighbor} ({G.edges[node, neighbor].get('label', 'related')})")

    graph_context = "\nGraph Context:\n" + "\n".join(list(set(related_nodes_info))[:20])

    # 3. Format Chat History
    history_text = ""
    if chat_history:
        # Take last 5 exchanges
        recent_history = chat_history[-10:] 
        history_text = "Chat History:\n"
        for msg in recent_history:
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            history_text += f"{role.upper()}: {content}\n"

    full_prompt = f"""You are a helpful technical assistant for a software project.
    
{history_text}

Current Question: {query}

{context_text}

{graph_context}

Answer the question based on the context provided. Explain your reasoning."""

    # 4. Synthesis
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    try:
        response = model.generate_content(full_prompt)
        
        usage = empty_usage.copy()
        if hasattr(response, 'usage_metadata'):
            usage = {
                "prompt_token_count": response.usage_metadata.prompt_token_count,
                "candidates_token_count": response.usage_metadata.candidates_token_count,
                "total_token_count": response.usage_metadata.total_token_count
            }
            
        return response.text, usage
    except Exception as e:
        return f"Error generating response: {e}", empty_usage
