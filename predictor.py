import joblib
import re
import fitz  # PyMuPDF

# Load the saved model and vectorizer
model = joblib.load('resume_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Extract and clean text
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = re.sub(r'\\[ntr]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Predict resume category
def predict_resume_category_from_text(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    return pred[0]
