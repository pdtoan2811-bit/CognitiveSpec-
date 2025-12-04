import os
import hashlib
import json
import re
from typing import List, Dict, Any

class Document:
    def __init__(self, content: str, metadata: Dict[str, Any]):
        self.content = content
        self.metadata = metadata
    
    def __repr__(self):
        return f"Document(metadata={self.metadata})"

class FileWatcher:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.manifest_dir = os.path.join(root_dir, ".cognitivespec")
        self.manifest_path = os.path.join(self.manifest_dir, "manifest.json")
        os.makedirs(self.manifest_dir, exist_ok=True)
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> Dict[str, str]:
        if os.path.exists(self.manifest_path):
            with open(self.manifest_path, "r") as f:
                return json.load(f)
        return {}

    def _calculate_file_hash(self, file_path: str) -> str:
        """Read file in binary mode and return MD5."""
        try:
            with open(file_path, "rb") as f:
                return hashlib.md5(f.read()).hexdigest()
        except FileNotFoundError:
            return ""

    def get_changed_files(self) -> List[str]:
        """Compare current disk state with manifest."""
        changed = []
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    # Normalize path separators
                    path = os.path.normpath(path)
                    
                    try:
                        current_hash = self._calculate_file_hash(path)
                        if self.manifest.get(path) != current_hash:
                            changed.append(path)
                            self.manifest[path] = current_hash # Update Optimistically
                    except Exception as e:
                        print(f"Error processing {path}: {e}")
        return changed

    def save_manifest(self):
        """Persist the new state."""
        with open(self.manifest_path, "w") as f:
            json.dump(self.manifest, f, indent=2)

def chunk_text(text: str, source_file: str) -> List[Document]:
    """
    Splits text by H2 headers (##).
    Respects atomic blocks (code blocks).
    Adds context injection (breadcrumbs).
    """
    chunks = []
    lines = text.split('\n')
    current_chunk = []
    current_header = "Root"
    
    # Simple state machine
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        # Check for H2 header, but not inside code block
        if not in_code_block and line.strip().startswith('## '):
            # Save previous chunk if exists
            if current_chunk:
                content = '\n'.join(current_chunk).strip()
                if content:
                    chunks.append(Document(
                        content=content,
                        metadata={
                            "source": source_file,
                            "header_path": current_header
                        }
                    ))
            
            # Start new chunk
            current_header = line.strip().replace('#', '').strip()
            current_chunk = [line]
        else:
            current_chunk.append(line)
            
    # Add last chunk
    if current_chunk:
        content = '\n'.join(current_chunk).strip()
        if content:
             chunks.append(Document(
                content=content,
                metadata={
                    "source": source_file,
                    "header_path": current_header
                }
            ))
            
    return chunks

def process_changes(directory: str) -> List[Document]:
    """
    Checks for changed files and returns their chunks.
    Updates the manifest.
    """
    watcher = FileWatcher(directory)
    changed_files = watcher.get_changed_files()
    
    all_chunks = []
    
    for file_path in changed_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                chunks = chunk_text(text, file_path)
                all_chunks.extend(chunks)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    watcher.save_manifest()
    return all_chunks

def load_all_docs(directory: str) -> List[Document]:
    """
    Loads all docs regardless of manifest (useful for reader view).
    """
    docs = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # We treat the whole file as one doc for reader, or chunks?
                        # For reader view, we probably want the raw content.
                        # But here we return Document objects.
                        docs.append(Document(content, {"source": path}))
                except Exception as e:
                    print(f"Error reading {path}: {e}")
    return docs
