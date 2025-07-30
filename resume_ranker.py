from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords once (only first time)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# --- Helper: Clean and tokenize text ---
def extract_keywords(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    keywords = [word for word in tokens if word not in stop_words and len(word) > 1]
    return set(keywords)

# --- File Readers ---
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# --- Read Input Files ---
resume = read_file("resume.txt")
job_description = read_file("job_description.txt")

# --- Calculate Match Score ---
vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform([resume, job_description])
similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

# --- Keyword Comparison ---
resume_keywords = extract_keywords(resume)
jd_keywords = extract_keywords(job_description)

matched = sorted(resume_keywords & jd_keywords)
missing = sorted(jd_keywords - resume_keywords)

# --- Output Results ---
print("\n🧠 Resume Match Result")
print("-" * 40)
print(f"✅ Match Score: {similarity:.2f}%\n")

print(f"✔️ Matched Keywords ({len(matched)}):")
print(", ".join(matched[:20]) or "None")

print(f"\n❌ Missing Keywords ({len(missing)}):")
print(", ".join(missing[:20]) or "None")
