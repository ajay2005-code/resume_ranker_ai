# 🧠 Resume Ranker AI – Intelligent Resume Matching with Job Description

A smart Python-based tool that compares a candidate's resume to a job description and calculates a **match score** using **Natural Language Processing (NLP)** and **Cosine Similarity**. Designed to help recruiters or job seekers assess how well a resume aligns with job requirements.

---

## 🚀 Features

- ✅ Extracts and preprocesses text from resumes and job descriptions  
- 📊 Calculates keyword similarity using **TF-IDF Vectorization**  
- 📐 Computes **Cosine Similarity Score** to determine resume-job fit  
- 🔍 Displays matched and missing keywords for transparency  
- 💡 Bonus: Filters out common stop words to focus on real tech skills  

---

## 📁 Project Structure

```bash
resume_ranker_ai/
├── resume_ranker.py      # Main script to run the matching logic
├── resume.txt            # Sample resume input
├── job_description.txt   # Sample job description input
└── README.md             # Project documentation (you are here!)
