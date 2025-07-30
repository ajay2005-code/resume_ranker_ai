# 🧠 Resume Ranker AI – Job Match Analyzer

A simple yet powerful Python-based AI tool that analyzes and compares your resume against a job description using Natural Language Processing (NLP) techniques. It helps job seekers understand how closely their resume matches a job post and identifies missing keywords.

---

## 🚀 Features

- ✅ Calculates **Match Score (%)** using TF-IDF + Cosine Similarity
- 🧩 Displays **matched** and **missing** keywords
- ⚙️ Built with `scikit-learn`, `nltk`, and basic Python
- 📄 Works with plain text resume and job description files

---

## 💻 Sample Output

## Example 1

### 🧠 Resume Match Result

✅ Match Score: 5.20%

✔️ Matched Keywords (2):
java, software

❌ Missing Keywords (16):
api, boot, control, developer, familiarity, frontend, git, looking, objectoriented, proficient, programming, required, rest, spring, tools, version

## Example 2

##🧠 Resume Match Result
----------------------------------------
✅ Match Score: 34.21%

✔️ Matched Keywords (14):
api, apis, cicd, control, database, developer, git, like, mongodb, nodejs, proficient, restful, systems, version

❌ Missing Keywords (16):
backend, candidate, cloud, deployment, development, experience, express, familiarity, hiring, knowledge, pipelines, plus, postgresql, postgresqlmongodb, required, using
