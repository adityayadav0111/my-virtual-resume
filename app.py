from pathlib import Path

import streamlit as st
from PIL import Image


# ---- Path Setting -----
current_dir = Path(__file__).parent if"__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/"main.css"
resume_file = current_dir / "assets" / "aditya_s_resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- general settings
PAGE_TITLE = "Digital CV | Aditya Yadav"
PAGE_ICON = ":wave:"
NAME = "Aditya Yadav"
DESCRIPTION = """
Aspiring Machine Learning Engineer with a solid foundation in data science, currently in my 3rd year of BSc in Data Science.
Skilled in data visualization, preprocessing, and team-based ML projects. 
"""
EMAIL = "aditya.yadav.bse@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/aditya-s-yadav01/",
    "Github": "https://github.com/adityayadav0111",
    "Kaggle": "https://www.kaggle.com/adityayadav01",
    "Twitter(X)": "https://x.com/yadavv_adityaa",
    "Leetcode": "https://leetcode.com/u/adityayadav011103/"
}

PROJECTS = {
    "🏆 Movie Recommendation System - Web app using Pyton ": "https://huggingface.co/spaces/aditya-s-yadav/Movie-Recommender",
    "🏆 SMS Spam Classifier - NlP Based System to Detect Spam or Ham": "https://github.com/adityayadav0111/sms-email-spam-classifier",
    "🏆 Spotify Dashboard - Used Power Bi to create interactive dashboard": "https://github.com/adityayadav0111/Dashboards/blob/main/Spotifyy_Dashboard_000.pbix",
    "🏆 Image To Text Conversion App - Used Flask to create Web App for Text Conversion from Image": "https://github.com/adityayadav0111/Image-to-text-speech-conversion-app",
}

CERTIFICATIONS = {
    "🎓 IBM Data Analyst Specialization - Coursera": "https://drive.google.com/file/d/19p7v4aGPzlik-y0nAuc8VbzdTw9wTo3o/view?usp=sharing",
    "🎓 Python for Data Science - NPTEL": "https://drive.google.com/file/d/1yyC7cu4a63Wambw71a_XtSeUgULcXCM3/view?usp=sharing",
    "🎓 Data Analytics and Visualization Job Simulation  - Forage": "https://drive.google.com/file/d/1XWh_fz1XaUqhY_KKuo3yvyeb9NKyf3qB/view?usp=sharing"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

## -- LOAD CSS, PDF AND PROFILE PIC ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte =pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Hero Section ---
col1, col2  = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= " 📄 Download Resume",
        data=PDFbyte,
        file_name = resume_file.name,
        mime="application/octet-stream",


    )
    st.write("📫",EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

## --- Experience and Qualifiaction
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 0.5 years of experience in data analysis, focusing on generating actionable insights from various datasets
- ✔️ Proficient in Python and Excel, applied in projects such as spam detection and image-to-text conversion
- ✔️ Strong understanding of statistical principles and their applications in real-world scenarios
- ✔️ Excellent team player with a proactive approach, demonstrated during internships and collaborative projects
- ✔️ Currently pursuing a BSc in Data Science, with coursework in machine learning and financial modeling
- ✔️ Hands-on experience in developing and deploying applications using Flask and data visualization tools
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, C, Java, NoSQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Tableau
- 📚 Core Skills: Supervised Learning, Unsupervied Learning, Data Scraping,NLP
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst Intern | Ozibook**")
st.write("07/2024 - 09/2024")
st.write(
    """
- ► Led a team of 4 in lead generation, identifying and implementing strategies to drive more qualified client leads.
- ► Collection and screening of data on over 500 potential clients across sectors such as travel, fitness, and corporate
companies, with a focus on markets in Dubai and major Indian cities.
- ► Conducted interviews to assess and onboard team members, enhancing team efficiency by selecting candidates aligned
with project requirements.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Science Intern | CodSoft**")
st.write("05/2018 - 06/2022")
st.write(
    """
- ► Developed and implemented machine learning models for fraud detection, sales price prediction, and movie rating
prediction
- ► • Utilized Python and relevant libraries for data preprocessing, model training, and evaluation.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Customer Service Associate  | PVR Cinemas**")
st.write("12/2023 - 02/2024")
st.write(
    """
- ► Processed financial transactions with precision, ensuring compliance with company policies and maintaining accurate
records for customer accounts.
- ► Addressed customer inquiries and resolved issues related to ticketing and bookings, ensuring a smooth and enjoyable
cinema experience for all patrons.
"""
)


# --- Certifications ---
st.write('\n')
st.subheader("📜Certifications")
st.write("---")
for certification, link in CERTIFICATIONS.items():
    st.write(f"[{certification}]({link})")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



