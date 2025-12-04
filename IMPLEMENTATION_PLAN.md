# Implementation Plan: Token Management, Model Upgrade, and RAG Transparency

## 1. Token Management Integration
**Goal**: Display real-time token usage (Prompt Tokens, Output Tokens, Total) for every AI interaction to monitor "Vibe Coding" costs.

### A. Backend Updates
1.  **Modify `services/graph_engine.py`**:
    *   Update `extract_graph_from_text` to capture `response.usage_metadata`.
    *   Return a tuple: `(GraphExtraction, usage_dict)` instead of just `GraphExtraction`.
    *   `usage_dict` format: `{"prompt_token_count": int, "candidates_token_count": int, "total_token_count": int}`.

2.  **Modify `services/rag_engine.py`**:
    *   Update `query_rag` to capture `response.usage_metadata`.
    *   Return a tuple: `(answer_text, usage_dict)`.

### B. Frontend Updates (`app.py`)
1.  **State Management**:
    *   Initialize `st.session_state.token_usage` to store cumulative usage:
        ```python
        if "token_usage" not in st.session_state:
            st.session_state.token_usage = {"prompt": 0, "completion": 0, "total": 0}
        ```
2.  **Sidebar Display**:
    *   Add a "Session Cost / Stats" expander in the Sidebar.
    *   Display "Last Action Tokens" and "Session Total Tokens".

---

## 2. Embedding & Chunking Verification
**Goal**: Confirm and document the local-first embedding strategy (already present).

*   **Status**: ✅ **Implemented**.
*   **Chunking**: `services/ingestion.py` uses H2 header-based splitting + Code Block preservation.
*   **Embedding**: `services/rag_engine.py` uses `sentence-transformers/all-MiniLM-L6-v2` (Local CPU/GPU).
*   **Action**: No code changes required. We will stick to the local embedding model to maintain the "Local-First" architecture, ensuring fast, free, and private vector search.

---

## 3. Model Upgrade to `gemini-2.5-flash`
**Goal**: Upgrade the chat and extraction models to the latest stable Flash model for improved reasoning and speed.

### A. Configuration Update
1.  **Modify `services/graph_engine.py`**:
    *   Change `model_name="gemini-2.0-flash-exp"` -> `model_name="gemini-2.5-flash"`.
2.  **Modify `services/rag_engine.py`**:
    *   Change `model_name="gemini-2.0-flash-exp"` -> `model_name="gemini-2.5-flash"`.

---

## Execution Steps for Agent
1.  **Edit `services/graph_engine.py`**: Add token return values & update model name.
2.  **Edit `services/rag_engine.py`**: Add token return values & update model name.
3.  **Edit `app.py`**: Add token tracking logic to session state and sidebar UI.

