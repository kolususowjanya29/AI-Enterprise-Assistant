# 🤖 AI-Powered Enterprise Assistant

A production-ready AI platform that enables users to upload enterprise documents, query unstructured/structured data, and generate intelligent analytics using Machine Learning and Generative AI.

---

## 🔗 Live Application & Demo
* **Live App Link:** [Streamlit Application](https://ai-enterprise-assistant-6gwb8r5jzhupnoygfdkbey.streamlit.app/)
* **Repository:** [GitHub Source Code](https://github.com/kolususowjanya29/AI-Enterprise-Assistant)

---

## 🛠️ System Architecture

```text
[ User Interface (Streamlit) ]
              │
              ▼
   [ FastAPI Core Engine ]
        │            │
        │            └─────────────────────────┐
        ▼                                      ▼
[ Unstructured Data Pipeline ]       [ Structured Data Pipeline ]
   ├── PDF Loader / OCR Engine          └── SQL Database Agent
   ├── Text Chunking & Embeddings               │
   └── FAISS Vector DB                          │
        │                                       │
        └──────────────────┬────────────────────┘
                           ▼
               [ LLM Response Generator ]
                           │
                 [ Evaluation & Logs ]
