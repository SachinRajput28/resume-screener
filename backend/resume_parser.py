import fitz
import re

def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    return " ".join(page.get_text() for page in doc)

def extract_sections(text: str) -> dict:
    sections = {"name": "", "email": "", "skills": [], "education": "", "experience": ""}

    email_match = re.search(r'[\w.-]+@[\w.-]+\.\w+', text)
    if email_match:
        sections["email"] = email_match.group()

    sections["name"] = text.strip().split("\n")[0]

    skill_match = re.search(r'skills[:\s]+(.*?)(?=\n[A-Z]|\Z)', text, re.IGNORECASE | re.DOTALL)
    if skill_match:
        sections["skills"] = [s.strip() for s in re.split(r'[,•\n]', skill_match.group(1)) if s.strip()]

    edu_match = re.search(r'education[:\s]+(.*?)(?=\n[A-Z]|\Z)', text, re.IGNORECASE | re.DOTALL)
    if edu_match:
        sections["education"] = edu_match.group(1).strip()

    exp_match = re.search(r'experience[:\s]+(.*?)(?=\n[A-Z]|\Z)', text, re.IGNORECASE | re.DOTALL)
    if exp_match:
        sections["experience"] = exp_match.group(1).strip()

    return sections