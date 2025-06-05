# analyzer.py

import re
import language_tool_python
import PyPDF2

# List of strong action verbs
ACTION_VERBS = [
    "developed", "designed", "managed", "led", "created", "achieved", "coordinated",
    "improved", "built", "initiated", "executed", "implemented", "analyzed", "resolved"
]

# List of common soft skills
SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem-solving", "time management",
    "adaptability", "creativity", "critical thinking", "work ethic", "collaboration"
]

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(text, required_skills):
    analysis = {}

    # --- Section 1: Check important sections ---
    sections = ['skills', 'education', 'projects', 'experience', 'internship', 'summary']
    found_sections = []

    lower_text = text.lower()

    for section in sections:
        if section in lower_text:
            found_sections.append(section.capitalize())

    analysis['Found Sections'] = found_sections

    # --- Section 2: Skills Matching ---
    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in lower_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    analysis['Matched Skills'] = matched_skills
    analysis['Missing Skills'] = missing_skills

    # --- Section 3: Grammar Checking ---
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    grammar_mistakes = len(matches)
    analysis['Grammar Mistakes'] = grammar_mistakes

    # --- Section 4: Action Verbs Check ---
    used_action_verbs = []
    missing_action_verbs = []

    for verb in ACTION_VERBS:
        if re.search(r'\b' + verb + r'\b', lower_text):
            used_action_verbs.append(verb)
        else:
            missing_action_verbs.append(verb)

    analysis['Used Action Verbs'] = used_action_verbs
    analysis['Missing Action Verbs'] = missing_action_verbs

    # --- Section 5: Soft Skills Check ---
    mentioned_soft_skills = []

    for soft_skill in SOFT_SKILLS:
        if soft_skill.lower() in lower_text:
            mentioned_soft_skills.append(soft_skill)

    analysis['Mentioned Soft Skills'] = mentioned_soft_skills

    # --- Section 6: Title/Professional Summary Check ---
    title_keywords = ['summary', 'profile', 'objective', 'about me']
    found_title = any(keyword in lower_text for keyword in title_keywords)
    analysis['Has Professional Summary'] = found_title

    # --- Section 7: Experience Analysis ---
    experience_keywords = ['experience', 'work history', 'professional experience']
    found_experience = any(keyword in lower_text for keyword in experience_keywords)
    analysis['Has Sufficient Experience Mentioned'] = found_experience

    # --- Section 8: Education Analysis ---
    education_keywords = ['education', 'degree', 'university', 'school']
    found_education = any(keyword in lower_text for keyword in education_keywords)
    analysis['Has Education Information'] = found_education

    # --- Section 9: Resume Length Check ---
    text_length = len(text.split())
    optimal_length = 300  # Optimal resume length, adjust as needed
    analysis['Resume Length'] = 'Optimal' if text_length > optimal_length else 'Too Short'

    # --- Section 10: Format Check ---
    format_check = 'well formatted' if found_title and found_experience and found_education else 'needs improvement'
    analysis['Format Check'] = format_check

    return analysis
