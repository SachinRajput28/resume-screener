# 🎯 AI Resume Screener

An AI-powered Resume Screener that helps HR users upload multiple resumes, define a Job Description, and automatically rank candidates by how well their resume matches the JD.

## 🛠 Tech Stack
- **Backend:** Python + FastAPI
- **ML/NLP:** scikit-learn (TF-IDF), Sentence-Transformers (SBERT)
- **PDF Parsing:** PyMuPDF (fitz)
- **Database:** MySQL
- **Frontend:** React.js

## ⚙️ How to Run Locally

### Backend
```bash
cd backend
pip install fastapi uvicorn pymupdf scikit-learn sentence-transformers spacy mysql-connector-python python-multipart pydantic
python -m spacy download en_core_web_sm
python -m uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

### Database
Run this in MySQL:
```sql
CREATE DATABASE resume_screener;
USE resume_screener;
CREATE TABLE candidates (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255), email VARCHAR(255),
  skills TEXT, education TEXT, experience TEXT,
  raw_text LONGTEXT, match_score FLOAT, label VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🤖 ML Approach
- **Scoring:** TF-IDF (40%) + SBERT (60%) weighted cosine similarity
- **Classifier:** Logistic Regression trained on 30 samples
- **Features:** match_score, years_of_experience, skill_count
- **Labels:** Shortlist / Maybe / Reject
- **Accuracy:** 100% on training data

## 📊 Confusion Matrix
```
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]
```

