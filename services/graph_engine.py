import os
import json
import time
from typing import List, Dict, Any, Tuple
import google.generativeai as genai
from pydantic import BaseModel, Field
import networkx as nx
from streamlit_agraph import Node, Edge, Config

class Entity(BaseModel):
   name: str = Field(..., description="Canonical name of the entity")
   type: str = Field(..., description="One of: COMPONENT, REQUIREMENT, API, ACTOR")
   description: str = Field(..., description="Short summary of its role")

class Relationship(BaseModel):
   source: str = Field(..., description="Name of source entity")
   target: str = Field(..., description="Name of target entity")
   relation_type: str = Field(..., description="One of: DEPENDS_ON, CALLS, CONFLICTS_WITH, DEFINES")

class GraphExtraction(BaseModel):
   entities: List[Entity]
   relationships: List[Relationship]

def extract_graph_from_text(text: str) -> Tuple[GraphExtraction, Dict[str, int]]:
    """
    Uses Gemini API to extract graph nodes and edges.
    Returns: (GraphExtraction, usage_dict)
    """
    api_key = os.getenv("GEMINI_API_KEY")
    empty_usage = {"prompt_token_count": 0, "candidates_token_count": 0, "total_token_count": 0}
    
    if not api_key:
        return GraphExtraction(entities=[], relationships=[]), empty_usage

    genai.configure(api_key=api_key)
    
    generation_config = {
        "temperature": 0.1,
        "top_p": 0.95,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=generation_config,
        system_instruction="""You are a Senior Systems Architect analyzing a requirements document. Your goal is to map the system topology.
Task: Extract all technical Entities and their Relationships from the provided text.
Entity Types:
* COMPONENT: Software modules, services, databases, UIs.
* REQUIREMENT: Business rules, constraints, functional mandates.
* API: Endpoints, function signatures, data contracts.
* ACTOR: Users, external systems, third-party services.
Relationship Types:
* DEPENDS_ON: Structural dependency (A imports B).
* CALLS: Runtime interaction (A sends request to B).
* CONFLICTS_WITH: Logical contradiction.
* DEFINES: A document section defines an entity.
Output: A JSON object matching the Schema GraphExtraction."""
    )

    prompt = f"Analyze the following text and extract the knowledge graph:\n\n{text}"

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            data = json.loads(response.text)
            
            # Extract usage metadata safely
            usage = empty_usage.copy()
            if hasattr(response, 'usage_metadata'):
                usage = {
                    "prompt_token_count": response.usage_metadata.prompt_token_count,
                    "candidates_token_count": response.usage_metadata.candidates_token_count,
                    "total_token_count": response.usage_metadata.total_token_count
                }
                
            return GraphExtraction(**data), usage
        except Exception as e:
            print(f"Error extraction attempt {attempt+1}: {e}")
            time.sleep(2 ** attempt)
            
    return GraphExtraction(entities=[], relationships=[]), empty_usage

def update_graph(G: nx.DiGraph, extraction: GraphExtraction, source_file: str):
    """
    Updates the graph with new extraction data.
    """
    for entity in extraction.entities:
        if not G.has_node(entity.name):
            G.add_node(entity.name, 
                       label=entity.name, 
                       type=entity.type, 
                       title=entity.description,
                       source_file=source_file)
        else:
            # Update source_file list if we want multiple sources, 
            # or just overwrite for simple Vibe Coding
            pass
    
    for rel in extraction.relationships:
        G.add_edge(rel.source, rel.target, label=rel.relation_type)

def get_agraph_data(G: nx.DiGraph):
    nodes = []
    edges = []
    
    type_colors = {
        "COMPONENT": "#ff9999",
        "REQUIREMENT": "#99ff99",
        "API": "#9999ff",
        "ACTOR": "#ffff99",
        "UNKNOWN": "#cccccc"
    }

    for node_id, attrs in G.nodes(data=True):
        node_type = attrs.get('type', 'UNKNOWN')
        nodes.append(Node(
            id=node_id,
            label=attrs.get('label', node_id),
            size=25,
            title=attrs.get('title', ''),
            color=type_colors.get(node_type, "#cccccc"),
            group=node_type
        ))
        
    for source, target, attrs in G.edges(data=True):
        edges.append(Edge(
            source=source,
            target=target,
            label=attrs.get('label', ''),
            type="CURVE_SMOOTH"
        ))
        
    config = Config(width="100%", height=600, directed=True, physics=True, hierarchical=False)
    
    return nodes, edges, config
