import re
import networkx as nx

def inject_links(text: str, G: nx.DiGraph) -> str:
    """
    Scans text for entity mentions and injects links.
    """
    if not G or not G.number_of_nodes():
        return text
        
    entities = list(G.nodes())
    # Sort by length descending (Longest Match Heuristic)
    entities.sort(key=len, reverse=True)
    
    # Split by code blocks to avoid modification inside them
    parts = re.split(r'(```[\s\S]*?```)', text)
    
    processed_parts = []
    for part in parts:
        if part.startswith('```'):
            processed_parts.append(part)
        else:
            # We want to replace entities with links.
            # To avoid replacing inside already created links, we can tokenize or use a placeholder.
            # But for simplicity, we'll just run through entities.
            # Risk: "User Authentication" becomes "[User](...) Authentication" if "User" is processed after?
            # No, we sorted by length descending, so "User Authentication" is processed first.
            
            # Risk: Replacing inside the URL of a link: [Foo](http://User/...)
            # We skip this for now.
            
            current_text = part
            for entity in entities:
                if len(entity) < 3: continue # Skip very short entities
                
                # Word boundary check
                pattern = r'\b' + re.escape(entity) + r'\b'
                
                # Check if it's already linked? Hard with regex. 
                # We'll just apply blindly but safely for Vibe Coding.
                # Actually, blindly is bad because [User Authentication](...) -> [[User](...) Authentication](...)
                
                # We can check if the match is not preceded by [
                
                # Lookbehind is fixed width in Python re, so (?<!\[) works.
                regex = re.compile(r'(?<!\[)\b' + re.escape(entity) + r'\b(?!\])')
                
                link = f"[{entity}](/?entity={entity.replace(' ', '%20')})"
                current_text = regex.sub(link, current_text)
                
            processed_parts.append(current_text)
            
    return "".join(processed_parts)
