# 🧠 Resume Analyzer – Smart Resume Evaluation Tool

**Resume Analyzer** is a Streamlit-based web app that analyzes uploaded resumes (PDF) and provides instant feedback on structure, skills, grammar, and more. It's designed to help job seekers optimize their resumes and assist recruiters in filtering suitable candidates quickly.

---

## 🚀 Features

✅ Upload a PDF resume and analyze it in real-time  
✅ Match resume content against user-specified skills  
✅ Detect action verbs and soft skills  
✅ Check grammar and formatting issues  
✅ Assess resume structure (experience, education, summary)  
✅ Predict the resume category/field using a machine learning model  
✅ Visualize key insights using charts and scores  

---

## 🖼 Demo

📺 Coming Soon – Add a demo video or screenshots here  
*(Optional: You can also link to a hosted version if deployed on Streamlit Cloud)*

---

## 🛠 Tech Stack

- **Python 3.8+**
- **Streamlit** – Web app interface
- **spaCy** – NLP and entity extraction
- **scikit-learn** – ML model for category prediction
- **PyPDF2** / **pdfminer** – Text extraction from PDF
- **matplotlib / seaborn / plotly** – Visualizations

---

## 📂 Project Structure

```bash
Resume-Analyzer/
├── app.py              # Streamlit app
├── analyzer.py         # Core logic: extraction, grammar, skill matching
├── predictor.py        # ML model and prediction logic
├── requirements.txt    # Dependencies
├── README.md           # This file
└── example_resumes/    # Sample PDF resumes (optional)
```

🔧 Installation
Clone the repository and install dependencies:
```
git clone https://github.com/Abdul00YO/Resume_Analyzer.git
cd Resume_Analyzer
pip install -r requirements.txt

```
▶️ Usage
Run the app locally with:
streamlit run app.py
Then open your browser at http://localhost:8501

📈 Future Improvements
-Resume scoring system (out of 100)
-Support for DOCX files
-Integration with LinkedIn job descriptions
-Deploy on Streamlit Cloud / Hugging Face Spaces
-Export analyzed resume as a report

🤝 Contributing
Pull requests and feature ideas are welcome! Feel free to fork and open an issue or PR.

📄 License
MIT License.
Feel free to use, modify, and distribute.

🙌 Acknowledgments
Inspired by ATS systems and resume review tools like Jobscan
spaCy, Grammarly APIs, Streamlit, and many more open-source tools

