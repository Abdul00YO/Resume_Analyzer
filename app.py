import streamlit as st
from analyzer import extract_text_from_pdf, analyze_resume
import matplotlib.pyplot as plt
import seaborn as sns
from predictor import predict_resume_category_from_text  # import the new function

# Predict category



# Set page config
st.set_page_config(page_title="📄 Professional Resume Analyzer", page_icon="📄", layout="wide")

# Title and Description
st.title("📄 Professional Resume Analyzer")
st.write("Upload your resume and get a detailed analysis of how well it matches the desired skills, professional standards, and formatting suggestions.")

# File upload and skills input
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
required_skills_input = st.text_input("Enter required skills (comma-separated)", placeholder="e.g. Python, Data Analysis, Leadership")

if uploaded_file and required_skills_input:
    required_skills = [skill.strip() for skill in required_skills_input.split(',')]
    text = extract_text_from_pdf(uploaded_file)
    analysis = analyze_resume(text, required_skills)

    # Display sections in a structured manner
    with st.container():
        st.header("📋 Resume Analysis Report")
        predicted_category = predict_resume_category_from_text(text)

# Display it in your UI
        with st.container():
            st.subheader("🏷️ Predicted Resume Category")
            st.success(f"**{predicted_category}**")
        # Section 1: Found Sections
        st.subheader("🔍 Found Resume Sections:")
        st.write(f"**Sections Detected**: {analysis['Found Sections']}")
        st.write("We detected the following sections in your resume. Please ensure that these sections are clear and formatted professionally.")
        
        st.write("**✅ Key Sections:**")
        for section in analysis['Found Sections']:
            st.write(f"- {section}")
        st.write("If any important sections are missing, consider adding them to your resume.")

    # Section 2: Skills Comparison (Matched vs Missing)
    with st.container():
        st.subheader("🔑 Skills Analysis")

        st.write("We will compare the skills you required vs the ones found in your resume.")
        st.write(f"**Required Skills**: {', '.join(required_skills)}")
        st.write(f"**Matched Skills**: {', '.join(analysis['Matched Skills'])}")
        st.write(f"**Missing Skills**: {', '.join(analysis['Missing Skills'])}")

        # Graph: Matched vs Missing Skills
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(['Matched Skills', 'Missing Skills'], [len(analysis['Matched Skills']), len(analysis['Missing Skills'])], color=['green', 'red'])
        ax.set_ylabel("Number of Skills")
        ax.set_title("Skills Comparison: Matched vs Missing")
        st.pyplot(fig)

    # Section 3: Action Verbs and Soft Skills
    with st.container():
        st.subheader("⚡ Action Verbs & Soft Skills")

        action_verbs_count = len(analysis['Used Action Verbs'])
        soft_skills_count = len(analysis['Mentioned Soft Skills'])
        st.write(f"**Action Verbs Used**: {action_verbs_count} action verbs found")
        st.write(f"**Soft Skills Mentioned**: {soft_skills_count} soft skills found")

        st.write("Action verbs enhance your resume by highlighting your achievements and leadership. Soft skills like teamwork and communication show your ability to work in teams.")
        if action_verbs_count < 5:
            st.warning("⚠️ Consider adding more impactful action verbs like 'managed', 'led', 'developed'.")
        if soft_skills_count < 3:
            st.warning("⚠️ Soft skills such as 'teamwork', 'communication', and 'leadership' are essential. Consider adding them.")

        # Graph: Action Verbs & Soft Skills Distribution
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie([action_verbs_count, soft_skills_count], labels=['Action Verbs', 'Soft Skills'], autopct='%1.1f%%', colors=['#FFD700', '#87CEEB'])
        ax.set_title("Distribution of Action Verbs and Soft Skills")
        st.pyplot(fig)

    # Section 4: Resume Sections Progress
    with st.container():
        st.subheader("📊 Resume Sections Completion")

        section_names = ["Experience", "Education", "Skills", "Certifications", "Achievements"]
        section_completion = [analysis['Found Sections'].count(section) for section in section_names]

        st.write("We analyzed the completion status of the following resume sections:")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(section_names, section_completion, color='skyblue')
        ax.set_ylabel("Number of Sections Completed")
        ax.set_title("Resume Sections Progress")
        st.pyplot(fig)

    # Section 5: Grammar and Formatting Analysis
    with st.container():
        st.subheader("📝 Grammar and Formatting Suggestions")
        
        grammar_mistakes = analysis['Grammar Mistakes']
        st.write(f"**Grammar Mistakes**: {grammar_mistakes}")
        
        if grammar_mistakes > 10:
            st.warning("⚠️ Your resume contains a high number of grammar mistakes. Consider proofreading and using grammar-checking tools.")
        elif grammar_mistakes > 5:
            st.warning("⚠️ There are some grammar mistakes. Please review and fix them for a more professional appearance.")

    # Final Conclusion & Suggestions
    with st.container():
        st.header("🔧 Final Recommendations")
        
        # Suggestions based on analysis
        st.write("Based on your resume analysis, here are some suggestions:")
        if len(analysis['Matched Skills']) < len(required_skills):
            st.write("1. Consider adding more of the required skills that are missing in your resume.")
        if len(analysis['Used Action Verbs']) < 5:
            st.write("2. Add more impactful action verbs to make your accomplishments stand out.")
        if len(analysis['Mentioned Soft Skills']) < 3:
            st.write("3. Highlight more soft skills like communication, leadership, and collaboration.")
        if grammar_mistakes > 5:
            st.write("4. Proofread your resume and fix the grammar mistakes to enhance professionalism.")

        st.success("✅ Resume Analysis Completed Successfully!")
