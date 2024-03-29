from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profilepic = current_dir / "assets" / "profilepic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Caleb Ngeno"
PAGE_ICON = ":random"
NAME = "Caleb  Ngeno"
DESCRIPTION = """
Accomplished software developer with extensive background in IT. Proficient in areas of web development and SaaS web applications.
\n Assisting Small and Midsize Enterprises seeking data-driven decisions.
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
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 3 Years experience extracting actionable insights from data.
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
- 📚 Modelling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 2
st.write('\n')
st.write("💻", "**IT Consultant | Tech Gaetano – Consultancy firm**")
st.write(" 01/2024 - Present")
st.write(
    """
- Advise clients on software. \n
- Redeveloped frontend for 5 web applications. \n
- Manage e-commerce websites for the clients by monitoring web traffic and tieing orders.\n
- Acted as a data controller.\n
- Integrated AI into existing web application. (chatbot)\n
- Implemented a secure payment integration gateway into an e-commerce website (MPESA).\n
- Built an AI powered news aggregator by scraping data from news multiple news sources.\n
- Utilized a variety of API’s and developed one such as typesense hybrid search, OpenAI, google API’s.\n
- Software Testing.

"""
)

# --- JOB 1
st.write('\n')
st.write("🏢", "**Data Analyst | Parse Consulting - An Accounting firm**")
st.write("05/2021 - 12/2023")
st.write(
    """
- Used Power BI and SQL to redeﬁne and track KPI's surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%.\n
- Led a team of analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads.\n
- Redesigned data model through iterations that improved predictions by 12%.
Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%.\n
- Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase for clients.\n
- Compiled, studied, and inferred large amounts of data, modelling information to drive auto policy pricing.\n
- Devised KPI's using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc.\n
- Analyzed, documented, and reported user survey results to improve customer communication processes by 18%.\n
- Collaborated with the analysts' team to oversee end-to-end process surrounding customers' return data.

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
