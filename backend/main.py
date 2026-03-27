from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
import os
import re

from resume_parser import extract_text, extract_sections
from scorer import combined_score
from classifier import train_model, predict_label
from database import save_candidate, get_all_candidates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
model = train_model()
current_jd = {"text": ""}

@app.post("/set-jd")
async def set_jd(jd: str = Form(...)):
    current_jd["text"] = jd
    return {"message": "JD saved"}

@app.post("/upload-resumes")
async def upload_resumes(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        path = f"C:/Users/Sachin/Desktop/resume-screener/backend/{file.filename}"
        with open(path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        raw_text = extract_text(path)
        sections = extract_sections(raw_text)
        score = combined_score(raw_text, current_jd["text"])

        years = len(re.findall(r'\b(20\d{2})\b', raw_text))
        skill_count = len(sections["skills"])

        label = predict_label(model, score, years, skill_count)
        sections.update({
            "raw_text": raw_text,
            "match_score": score,
            "label": label
        })
        save_candidate(sections)
        results.append({
            **sections,
            "match_score": score,
            "label": label
        })
        os.remove(path)

    return {
        "candidates": sorted(results, key=lambda x: x["match_score"], reverse=True)
    }

@app.get("/rankings")
async def get_rankings():
    return {"candidates": get_all_candidates()}