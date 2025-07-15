import streamlit as st


def main():
    st.header("Alex Le Tran")

    about_me = st.Page("about_me.py", title="About Me", icon="🎈")
    skills = st.Page("skills.py", title="Skills", icon="🔨")
    experience = st.Page("experience.py", title="Experience", icon="🤸")
    portfolio = st.Page("portfolio.py", title="Portoflio", icon="📗")
    education = st.Page("education.py", title="Education", icon="🏫")
    contact = st.Page("contact.py", title="Contact", icon="🤙")

    pg = st.navigation(
        [
            about_me,
            skills,
            experience,
            portfolio,
            education,
            contact,
        ]
    )

    pg.run()


if __name__ == "__main__":
    main()
