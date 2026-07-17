# AI Document Versioning & QA System

## 📌 Project Overview

AI Document Versioning & QA System is an intelligent backend application that automates document version management and AI-powered question-answer generation for technical PDF documents.

The system extracts document structure, reconstructs hierarchical sections, compares document versions using SHA-256 hashes, generates Question & Answer pairs using a local Large Language Model (Mistral via Ollama), and automatically identifies stale QA whenever document content changes.

---

## 🚀 Features

- PDF Parsing
- Text Extraction using PyMuPDF
- Heading Classification
- Document Hierarchy Reconstruction
- SHA-256 Content Hashing
- SQLite Database Storage
- Automatic Version Management
- Document Version Comparison
- AI-powered Question & Answer Generation
- Ollama + Mistral Integration
- Stale QA Detection
- REST APIs using FastAPI

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI

### Database
- SQLite
- SQLAlchemy

### AI
- Ollama
- Mistral LLM

### PDF Processing
- PyMuPDF

### Others
- SHA-256 Hashing
- REST API
- Uvicorn

---

## 📂 Project Structure

```
ct200-ai-backend/
│
├── app/
│   ├── database/
│   ├── services/
│   └── main.py
│
├── data/
├── docs/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Workflow

1. Upload PDF
2. Extract Text
3. Merge Text Spans
4. Classify Headings
5. Build Document Hierarchy
6. Generate SHA-256 Hashes
7. Store Document in SQLite
8. Compare Document Versions
9. Generate AI Question & Answer Pairs
10. Mark Stale QA when content changes

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/parse` | Parse and store document |
| GET | `/compare` | Compare two document versions |
| POST | `/generate-qa` | Generate AI Question & Answers |
| POST | `/mark-stale` | Mark outdated QA |

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Akshitha1155/ct200-ai-backend.git
```

Go to project

```bash
cd ct200-ai-backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🔮 Future Enhancements

- JWT Authentication
- Frontend Dashboard
- Vector Database Integration
- Semantic Search
- RAG-based Document Assistant
- Cloud Deployment

---

## 👩‍💻 Author

**Akshitha Gogikar**

AI & Machine Learning Student

Kakatiya Institute of Technology & Science (KITSW)