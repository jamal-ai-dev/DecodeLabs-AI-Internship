# Project 3 — AI Recommendation Logic (Tech Stack Recommender)

**DecodeLabs AI Internship — Batch 2026**

## 🎯 Goal
Build a simple, content-based recommendation engine that maps a user's
skills and career interests to the most relevant tech-stack / job role,
using pattern matching and similarity logic (no historical user data
required).

## 🧠 How It Works — Input → Process → Output

| Step | Description |
|------|-------------|
| **1. Ingestion** | The user enters at least 3 skills or interests (e.g. `Python, Cloud Computing, Automation`). |
| **2. Scoring** | Each job role's skill set (from `raw_skills.csv`) and the user's skills are converted into **TF-IDF weighted vectors** within a shared vocabulary space. |
| **3. Sorting** | The engine computes **Cosine Similarity** between the user vector and every job-role vector, then sorts scores in descending order. |
| **4. Filtering** | The list is truncated to the **Top-3** highest-scoring job roles to avoid choice overload. |

This is a **Content-Based Filtering** system: recommendations are driven
purely by item (job role) attributes, not by other users' behavior —
which means it works immediately with zero "cold start" problem for new
job roles.

## 📂 Files
- `recommender.py` — main recommendation engine (CLI)
- `raw_skills.csv` — dataset mapping job roles to their core skills
- `requirements.txt` — Python dependencies

## ▶️ How to Run
```bash
pip install -r requirements.txt
python recommender.py
```

Then enter 3 or more comma-separated skills when prompted, for example:

```
Your skills: Python, Machine Learning, Statistics
```

Sample output:
```
1. Data Scientist — 62.4% match
   Key skills: Python, SQL, Machine Learning, Statistics, Data Analysis, Pandas, NumPy

2. AI Research Engineer — 51.2% match
   Key skills: Python, Machine Learning, Deep Learning, Algorithms, Statistics, Research, TensorFlow

3. Machine Learning Engineer — 48.9% match
   Key skills: Python, Machine Learning, TensorFlow, Deep Learning, Data Structures, Algorithms, Cloud Computing
```

## 🛠️ Key Concepts Applied
- **Vector Mapping** — converting qualitative skills into numerical arrays
- **TF-IDF Weighting** — rewarding specific/rare skills, penalizing generic ones
- **Cosine Similarity** — measuring the angle between user & job vectors, independent of profile length
- **IPO Pipeline** — Ingestion → Scoring → Sorting → Filtering

## 📌 Notes / Possible Extensions
- Add more job roles / skills to `raw_skills.csv` to widen coverage.
- Handle the **cold start problem** with an onboarding survey or trending fallback.
- Swap in real interaction data later to move from content-based to collaborative filtering.