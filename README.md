# 🎯 AI Resume Screener

An AI-powered Resume Screener web application that helps HR users upload multiple resumes, define a Job Description (JD), and automatically rank candidates by how well their resume matches the JD using Machine Learning.

---

## 🚀 Live Demo
> Run locally by following the steps below

---

## 📸 Features
- 📄 Upload multiple PDF resumes at once
- 📝 Enter or paste a Job Description
- 🤖 ML-based resume scoring using TF-IDF + SBERT
- 🏷️ Auto label candidates as **Shortlist / Maybe / Reject**
- 📊 Ranked dashboard showing all candidates
- 💾 All data saved to MySQL database
- 🔌 REST API backend separate from frontend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + FastAPI |
| ML / NLP | scikit-learn (TF-IDF), Sentence-Transformers (SBERT) |
| PDF Parsing | PyMuPDF (fitz) |
| Classifier | Logistic Regression (scikit-learn) |
| Database | MySQL |
| Frontend | React.js |

---

## ⚙️ How to Run Locally

### Step 1 — Clone the Repository
```bash
git clone https://github.com/SachinRajput28/resume-screener.git
cd resume-screener
```

### Step 2 — Setup MySQL Database
Open MySQL and run:
```sql
CREATE DATABASE resume_screener;
USE resume_screener;
CREATE TABLE candidates (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  skills TEXT,
  education TEXT,
  experience TEXT,
  raw_text LONGTEXT,
  match_score FLOAT,
  label VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3 — Setup Backend
```bash
cd backend
pip install fastapi uvicorn pymupdf scikit-learn sentence-transformers spacy mysql-connector-python python-multipart pydantic
python -m spacy download en_core_web_sm
python -m uvicorn main:app --reload
```
Backend runs at: http://127.0.0.1:8000

### Step 4 — Setup Frontend
```bash
cd frontend
npm install
npm start
```
Frontend runs at: http://localhost:3000

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /set-jd | Save the Job Description |
| POST | /upload-resumes | Upload PDF resumes and get scores |
| GET | /rankings | Get all candidates ranked by score |

---

## 🤖 ML Approach

### Scoring
- **TF-IDF + Cosine Similarity** — matches keywords between resume and JD (40% weight)
- **SBERT Semantic Similarity** — understands meaning not just keywords (60% weight)
- **Combined Score** = TF-IDF × 0.4 + SBERT × 0.6

### Classifier
- **Model:** Logistic Regression
- **Training Data:** 30 labeled samples
- **Features:**
  - match_score — how well resume matches JD
  - years_of_experience — total years of work experience
  - skill_count — number of skills found in resume
- **Labels:** Shortlist / Maybe / Reject
- **Accuracy:** 100%

### Confusion Matrix
```
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]
```

### Why Logistic Regression?
- Simple and fast
- Works well for small datasets
- Easy to explain and interpret
- Perfect for multi-class classification

---

## 📁 Project Structure
```
resume-screener/
├── backend/
│   ├── main.py            # FastAPI app and API endpoints
│   ├── resume_parser.py   # PDF text extraction
│   ├── scorer.py          # TF-IDF + SBERT scoring
│   ├── classifier.py      # Logistic Regression classifier
│   └── database.py        # MySQL connection
├── frontend/
│   └── src/
│       └── App.js         # React frontend
└── README.md
```

---

## 🎥 Video Demo
[Add your Loom/Google Drive video link here]

---

## 👨‍💻 Author
**Sachin Rajput**
- GitHub: [@SachinRajput28](https://github.com/SachinRajput28)
- Email: work.sachinrajput28@gmail.com
