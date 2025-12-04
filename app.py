__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import os
import networkx as nx
import pickle
from dotenv import load_dotenv

# Services
from services import ingestion, graph_engine, rag_engine, linker
from components import graph_viz, chat_ui

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="CognitiveSpec",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

GRAPH_PATH = os.path.join(".cognitivespec", "graph.pkl")

def load_graph():
    if os.path.exists(GRAPH_PATH):
        try:
            with open(GRAPH_PATH, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
             print(f"Error loading graph: {e}")
             return nx.DiGraph()
    return nx.DiGraph()

def save_graph(G):
    os.makedirs(".cognitivespec", exist_ok=True)
    with open(GRAPH_PATH, 'wb') as f:
        pickle.dump(G, f)

if "graph" not in st.session_state:
    st.session_state.graph = load_graph()

if "token_usage" not in st.session_state:
    st.session_state.token_usage = {"prompt": 0, "completion": 0, "total": 0}

def update_token_usage(usage_dict):
    st.session_state.token_usage["prompt"] += usage_dict.get("prompt_token_count", 0)
    st.session_state.token_usage["completion"] += usage_dict.get("candidates_token_count", 0)
    st.session_state.token_usage["total"] += usage_dict.get("total_token_count", 0)

def main():
    st.title("CognitiveSpec 🧠")
    
    # Sidebar
    with st.sidebar:
        st.header("Navigation")
        page = st.radio("Go to", ["Graph Explorer", "Document Reader", "Chat", "Settings"])
        
        st.markdown("---")
        st.header("Graph Stats")
        st.metric("Nodes", st.session_state.graph.number_of_nodes())
        st.metric("Edges", st.session_state.graph.number_of_edges())
        
        with st.expander("Session Cost / Stats"):
            st.write(f"**Total Tokens:** {st.session_state.token_usage['total']}")
            st.write(f"Prompt: {st.session_state.token_usage['prompt']}")
            st.write(f"Completion: {st.session_state.token_usage['completion']}")

        st.markdown("---")
        if st.button("Re-Scan Documents"):
            with st.spinner("Ingesting and analyzing documents..."):
                # 1. Ingest
                docs_dir = os.path.join("data", "docs")
                if not os.path.exists(docs_dir):
                    os.makedirs(docs_dir)
                    
                chunks = ingestion.process_changes(docs_dir)
                if chunks:
                    st.toast(f"Found {len(chunks)} new/changed chunks.")
                    
                    # 2. Extract & Update Graph
                    progress_bar = st.progress(0)
                    for i, chunk in enumerate(chunks):
                        extraction, usage = graph_engine.extract_graph_from_text(chunk.content)
                        update_token_usage(usage)
                        graph_engine.update_graph(st.session_state.graph, extraction, chunk.metadata['source'])
                        progress_bar.progress((i + 1) / len(chunks))
                    
                    save_graph(st.session_state.graph)
                    
                    # 3. Update Vector Store
                    rag_engine.add_documents(chunks)
                    
                    st.success("Ingestion Complete!")
                    st.rerun()
                else:
                    st.info("No new changes detected.")

    # Main Content
    if page == "Graph Explorer":
        st.header("Knowledge Graph Explorer")
        nodes, edges, config = graph_engine.get_agraph_data(st.session_state.graph)
        graph_viz.render_graph(nodes, edges, config)
        
    elif page == "Document Reader":
        st.header("Document Reader")
        docs_dir = os.path.join("data", "docs")
        if os.path.exists(docs_dir):
            for root, _, files in os.walk(docs_dir):
                for file in files:
                    if file.endswith(".md"):
                        st.subheader(file)
                        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                            content = f.read()
                            # Linker logic
                            content = linker.inject_links(content, st.session_state.graph)
                            st.markdown(content)
        else:
            st.info("No documents found in data/docs/")
        
    elif page == "Chat":
        st.header("Cognitive Chat")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages
        for message in st.session_state.messages:
            chat_ui.render_chat_bubble(message["role"], message["content"])

        if prompt := st.chat_input("Ask about the specs..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_ui.render_chat_bubble("user", prompt)
            
            with st.spinner("Thinking..."):
                response, usage = rag_engine.query_rag(prompt, st.session_state.graph)
                update_token_usage(usage)
                
            st.session_state.messages.append({"role": "assistant", "content": response})
            chat_ui.render_chat_bubble("assistant", response)
            
    elif page == "Settings":
        st.header("Settings")
        api_key = st.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
        if api_key:
            os.environ["GEMINI_API_KEY"] = api_key
            st.success("API Key loaded session-only.")

if __name__ == "__main__":
    main()
