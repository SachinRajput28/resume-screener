import { useState } from "react";
import axios from "axios";

function App() {
  const [jd, setJd] = useState("");
  const [files, setFiles] = useState([]);
  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!jd || files.length === 0) {
      alert("Please enter JD and upload resumes!");
      return;
    }
    setLoading(true);
    await axios.post("http://localhost:8000/set-jd",
      new URLSearchParams({ jd }));
    const form = new FormData();
    files.forEach(f => form.append("files", f));
    const res = await axios.post("http://127.0.0.1:8000/upload-resumes", form);
    setCandidates(res.data.candidates);
    setLoading(false);
  };

  const getBadgeColor = (label) => {
    if (label === "Shortlist") return "green";
    if (label === "Maybe") return "orange";
    return "red";
  };

  return (
    <div style={{ maxWidth: "800px", margin: "0 auto", padding: "20px" }}>
      <h1>🎯 AI Resume Screener</h1>

      <div style={{ marginBottom: "20px" }}>
        <h3>Step 1 — Enter Job Description</h3>
        <textarea
          rows={6}
          style={{ width: "100%", padding: "10px" }}
          placeholder="Paste job description here..."
          value={jd}
          onChange={e => setJd(e.target.value)}
        />
      </div>

      <div style={{ marginBottom: "20px" }}>
        <h3>Step 2 — Upload Resumes (PDF)</h3>
        <input
          type="file"
          multiple
          accept=".pdf"
          onChange={e => setFiles([...e.target.files])}
        />
      </div>

      <button
        onClick={handleSubmit}
        style={{
          padding: "10px 30px",
          background: "blue",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
          fontSize: "16px"
        }}
      >
        {loading ? "Screening..." : "🚀 Screen Resumes"}
      </button>

      {candidates.length > 0 && (
        <div style={{ marginTop: "30px" }}>
          <h2>📊 Candidate Rankings</h2>
          {candidates.map((c, i) => (
            <div key={i} style={{
              border: "1px solid #ccc",
              borderRadius: "8px",
              padding: "15px",
              marginBottom: "10px"
            }}>
              <h3>{i + 1}. {c.name}</h3>
              <p>📧 {c.email}</p>
              <p>🎯 Match Score: <b>{c.match_score}%</b></p>
              <span style={{
                background: getBadgeColor(c.label),
                color: "white",
                padding: "4px 12px",
                borderRadius: "4px"
              }}>
                {c.label}
              </span>
              <p>🛠 Skills: {Array.isArray(c.skills) ? c.skills.join(", ") : c.skills}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;