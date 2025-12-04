import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

def render_graph(nodes, edges, config):
    """
    Renders the graph using streamlit-agraph
    """
    if not nodes:
        st.warning("No nodes to display.")
        return None

    return agraph(nodes=nodes, edges=edges, config=config)
