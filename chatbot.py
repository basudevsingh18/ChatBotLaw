import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from gpt4all import GPT4All
import pandas as pd

# Load data and embeddings
df = pd.read_csv('legal_qa.csv')
embedder = SentenceTransformer('all-MiniLM-L6-v2')
question_embeddings = embedder.encode(df['Question'].tolist(), convert_to_numpy=True)
index = faiss.IndexFlatL2(question_embeddings.shape[1])
index.add(question_embeddings)

model_path = "mistral-7b-openorca.Q4_0.gguf"

def normalize_citation(citation):
    if not isinstance(citation, str):
        return citation  # skip if it's NaN or not a string
    if "Section" in citation and "," not in citation:
        parts = citation.rsplit("Section", 1)
        if len(parts) == 2:
            return f"{parts[0].strip()}, Section {parts[1].strip()}"
    return citation


df["Citation"] = df["Citation"].apply(normalize_citation)
df.to_csv("legal_qa.csv", index=False)

def translate(text, src_lang="en", target_lang="gcr"):
    return f"(Creole Translation) {text}" if target_lang == "gcr" else text

# Main chatbot logic
def get_answer(user_input, lang_pref="en", include_raw=False):
    query_embedding = embedder.encode([user_input])[0].astype("float32").reshape(1, -1)
    _, idx = index.search(query_embedding, k=1)
    match = df.iloc[idx[0][0]]

    question = match['Question']
    answer = match['Answer']
    citation = match.get("Citation", "").strip()

    prompt = f"User question: {user_input}\nRelated legal topic: {question}\nAnswer: {answer}\n\nNow respond conversationally:"

    with GPT4All(model_path) as gpt:
        response = gpt.generate(prompt=prompt).strip()

    if include_raw:
        return response, citation  # returns both for route logic

    if citation:
        if "," in citation:
            parts = citation.split(",", 1)
            law, section = parts
            response += f"\n\n———\n📘 <strong>{law}</strong><br>{section.strip()}"
        elif "Section" in citation:
            parts = citation.rsplit("Section", 1)
            if len(parts) == 2:
                law, section = parts
                response += f"\n\n———\n📘 <strong>{law.strip()}</strong><br>Section {section.strip()}"
            else:
                response += f"\n\n📘 <strong>Legal Reference:</strong> {citation}"
        else:
            response += f"\n\n📘 <strong>Legal Reference:</strong> {citation}"

    if lang_pref == "gcr":
        return translate(response)
    elif lang_pref == "both":
        creole = translate(response)
        return f"{response}\n\n{creole}"
    return response