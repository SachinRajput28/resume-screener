import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="resume_screener"
    )

def save_candidate(data: dict):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO candidates 
             (name, email, skills, education, experience, raw_text, match_score, label)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (
        data["name"],
        data["email"],
        str(data["skills"]),
        data["education"],
        data["experience"],
        data["raw_text"],
        data["match_score"],
        data["label"]
    ))
    conn.commit()
    conn.close()

def get_all_candidates():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM candidates ORDER BY match_score DESC")
    results = cursor.fetchall()
    conn.close()
    return results