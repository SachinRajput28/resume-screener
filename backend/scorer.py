from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

def tfidf_score(resume_text: str, jd_text: str) -> float:
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([jd_text, resume_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

def sbert_score(resume_text: str, jd_text: str) -> float:
    embeddings = sbert_model.encode([jd_text, resume_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(score) * 100, 2)

def combined_score(resume_text: str, jd_text: str) -> float:
    t = tfidf_score(resume_text, jd_text)
    s = sbert_score(resume_text, jd_text)
    return round((t * 0.4 + s * 0.6), 2)