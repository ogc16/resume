from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profilepic = current_dir / "assets" / "profilepic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Caleb Ngeno"
PAGE_ICON = ":random"
NAME = "Caleb  Ngeno"
DESCRIPTION = """
Accomplished software developer with extensive background in IT. Proficient in areas of web development and SaaS web applications.
Assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "ngenokibetcaleb@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://ke.linkedin.com/in/caleb-kibet-ngeno-3a0012118",
    "GitHub": "https://github.com/ogc16",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profilepic = Image.open(profilepic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profilepic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data.
- ✔️ Strong hands on experience and knowledge in Python and Excel.
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")


# --- JOB 1
st.write('\n')
st.write("🚧", "**Data Analyst | Parse Consulting - An Accounting firm**")
st.write("01/2021 - 12/2023")
st.write(
    """
Used Power BI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%.
Led a team of analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads.
Redesigned data model through iterations that improved predictions by 12%.
Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%.
Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase for clients.
Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing.
Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc.
Analyzed, documented, and reported user survey results to improve customer communication processes by 18%.
Collaborated with analyst team to oversee end-to-end process surrounding customers' return data.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**IT Consultant | Tech Gaetano – Consultancy firm**")
st.write("09/2019 - 01/2020")
st.write(
    """
Advise clients on software. 
Redeveloped frontend for 5 web applications. 
Manage e-commerce website for our clients by monitoring web traffic.
Acted as a data controller.
Integrated AI into existing web application. (chatbot)
Implemented a secure payment integration gateway into an ecommerce website (MPESA).
Built an AI powered news aggregator by scraping data from news multiple news sources.
Utilized a variety of API’s and developed one such as typesense hybrid search, OpenAI, google API’s.
Software Testing.

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")