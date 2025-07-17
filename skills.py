import streamlit as st
import pandas as pd
import altair as alt
from dataclasses import make_dataclass


def skills():
    st.markdown("### Skills")
    st.markdown(
        "All skills are set between level 1 to 5, where 1 is beginner and 5 is advanced with professional experience."
    )
    st.markdown("#### Programming Languages")

    prog_lang_skills = pd.DataFrame(
        {
            "Languages": ["Python", "SQL", "JavaScript", "Lua"],
            "Level": [5, 5, 4, 3],
        },
    )

    prog_lang_skills_chart = (
        alt.Chart(prog_lang_skills)
        .mark_bar()
        .encode(
            y="Languages",
            x="Level",
            color=alt.Color("Level").legend(None),
        )
        .configure_axis(
            grid=False,
            tickMinStep=1,
        )
        .properties(
            height=alt.Step(30),
        )
    )

    st.altair_chart(prog_lang_skills_chart)

    st.markdown("#### Python Frameworks")

    PythonFramework = make_dataclass(
        "PythonFramework",
        [
            ("framework", str),
            ("professional_exp", int),
            ("personal_exp", int),
        ],
    )

    python_fw_skills = pd.DataFrame(
        [
            PythonFramework("FastAPI", 5, 4),
            PythonFramework("Pandas", 5, 5),
            PythonFramework("Apache Beam", 4, 3),
            PythonFramework("Streamlit", 1, 3),
        ]
    )

    st.dataframe(python_fw_skills)

    base = (
        alt.Chart(python_fw_skills)
        .encode(
            alt.X("personal_exp:Q")
            .axis(labelAngle=0)
            .scale(domain=[0, 6])
            .title("Personal Experience"),
            alt.Y("professional_exp:Q")
            .scale(domain=[0, 6])
            .title("Professional Experience"),
        )
        .properties(
            width=200,
            height=700,
        )
    )
    pts = base.mark_point(
        size=50,
    )
    text = base.mark_text(
        dx=10,
        dy=-2,
        align="left",
        fontSize=14,
        color="white",
    ).encode(text="framework:N")

    python_fw_skills_chart = (pts + text).configure_axis(
        tickMinStep=1,
    )

    st.altair_chart(python_fw_skills_chart)

    st.markdown("#### SQL Flavours")


if __name__ == "__main__":
    skills()
