"""
Project 3 - AI Recommendation Logic
Tech Stack Recommender

DecodeLabs AI Internship

This script builds a Content-Based Filtering recommendation engine that
maps a user's skills / career interests to the most relevant job roles
(tech stacks) using TF-IDF vectorization + Cosine Similarity.

Pipeline (Input -> Process -> Output):
    1. Ingestion  -> capture user's skills (minimum 3 required)
    2. Scoring    -> TF-IDF vectorize skills, compute cosine similarity
    3. Sorting    -> rank job roles by similarity score (descending)
    4. Filtering  -> return only the Top-N most relevant roles
"""

import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Resolve the dataset path relative to THIS script's folder, not the
# terminal's current working directory. This way the script works no
# matter where you run it from (repo root, this folder, etc.).
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "raw_skills.csv")
TOP_N = 3


def load_dataset(path: str) -> pd.DataFrame:
    """Step 1a: Load the job-role / skills dataset from disk."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: could not find dataset '{path}'.")
        sys.exit(1)
    return df


def clean_skills_text(raw_skills: str) -> str:
    """Normalize a comma separated skills string into a single space
    separated string so each skill is treated as one token by TF-IDF."""
    skills = [s.strip().replace(" ", "_").lower() for s in raw_skills.split(",")]
    return " ".join(skills)


def build_corpus(df: pd.DataFrame) -> list:
    """Turn every job role's skill list into a TF-IDF-ready document."""
    return df["skills"].apply(clean_skills_text).tolist()


def get_user_input() -> list:
    """Step 1b: Ingest the user's skills / interests (min. 3 required)."""
    print("\nEnter at least 3 skills or interests, separated by commas.")
    print("Example: Python, Cloud Computing, Automation")
    while True:
        raw = input("\nYour skills: ").strip()
        skills = [s.strip() for s in raw.split(",") if s.strip()]
        if len(skills) >= 3:
            return skills
        print(f"Please enter at least 3 skills (you entered {len(skills)}).")


def recommend(user_skills: list, df: pd.DataFrame, corpus: list, top_n: int = TOP_N) -> pd.DataFrame:
    """Steps 2-4: Score every job role against the user profile using
    TF-IDF weighted Cosine Similarity, then sort and filter to Top-N."""

    # Fit TF-IDF on the job-role corpus so the vocabulary space is shared
    vectorizer = TfidfVectorizer()
    job_vectors = vectorizer.fit_transform(corpus)

    # Transform the user's skills into the SAME vector space (Step: Vector Mapping)
    user_doc = clean_skills_text(", ".join(user_skills))
    user_vector = vectorizer.transform([user_doc])

    # Step 2: Scoring - Cosine Similarity between user vector and every job vector
    scores = cosine_similarity(user_vector, job_vectors).flatten()

    results = df.copy()
    results["match_score"] = (scores * 100).round(2)

    # Step 3: Sorting - descending by similarity score
    results = results.sort_values(by="match_score", ascending=False)

    # Step 4: Filtering - Top-N list only, drop zero-score noise
    results = results[results["match_score"] > 0].head(top_n)
    return results[["job_role", "skills", "match_score"]]


def display_results(results: pd.DataFrame) -> None:
    if results.empty:
        print("\nNo strong matches found. Try adding more specific technical skills.")
        return

    print("\n" + "=" * 55)
    print(" TOP RECOMMENDED TECH STACKS / JOB ROLES")
    print("=" * 55)
    for rank, (_, row) in enumerate(results.iterrows(), start=1):
        print(f"\n{rank}. {row['job_role']}  —  {row['match_score']}% match")
        print(f"   Key skills: {row['skills']}")
    print("\n" + "=" * 55)


def main():
    print("DecodeLabs AI Internship - Project 3")
    print("Tech Stack Recommender (Content-Based Filtering)")

    df = load_dataset(DATA_FILE)
    corpus = build_corpus(df)

    while True:
        user_skills = get_user_input()
        results = recommend(user_skills, df, corpus, TOP_N)
        display_results(results)

        again = input("\nTry another set of skills? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for using the Tech Stack Recommender. Goodbye!")
            break


if __name__ == "__main__":
    main()