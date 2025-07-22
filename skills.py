import streamlit as st
import pandas as pd
import altair as alt
from dataclasses import make_dataclass
from themes.catppuccin import macchiato


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

    # st.dataframe(prog_lang_skills)

    st.altair_chart(prog_lang_skills_chart)

    st.markdown("#### Frameworks")

    Framework = make_dataclass(
        "Framework",
        [
            ("framework", str),
            ("experience_lvl", int),
            ("proficiency_lvl", int),
            ("language", str),
        ],
    )

    skills_matrix = pd.DataFrame(
        [
            Framework("FastAPI", 25, 20, "Python"),
            Framework("Pandas", 39, 45, "Python"),
            Framework("Apache Beam", 15, 7, "Python"),
            Framework("Streamlit", -45, -30, "Python"),
            Framework("Flask", -17, 28, "Python"),
            Framework("Prefect", 37, 23, "Python"),
            Framework("React", -38, 5, "Javascript"),
            Framework("dbt", -12, -42, "SQL"),
            Framework("dataform", 12, 32, "SQL"),
        ]
    )

    st.dataframe(skills_matrix)

    base = (
        alt.Chart(skills_matrix)
        .encode(
            alt.X("experience_lvl:Q")
            .axis(
                grid=False,
                ticks=False,
                labels=False,
            )
            .scale(domain=[-50, 50])
            .title(None),
            alt.Y("proficiency_lvl:Q")
            .axis(
                grid=False,
                ticks=False,
                labels=False,
            )
            .scale(domain=[-50, 50])
            .title(None),
        )
        .properties(
            width=200,
            height=700,
        )
    )

    x_axis = (
        alt.Chart(
            pd.DataFrame({"x": [0]}),
        )
        .mark_rule(
            color=macchiato.lavender,
        )
        .encode(
            x="x",
            size=alt.value(2),
        )
    )

    y_axis = (
        alt.Chart(
            pd.DataFrame({"y": [0]}),
        )
        .mark_rule(
            color=macchiato.lavender,
        )
        .encode(
            y="y",
            size=alt.value(2),
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

    skills_matrix_chart = (x_axis + y_axis + pts + text).configure_view(
        fill=macchiato.surface0,
    )

    st.altair_chart(skills_matrix_chart)

    st.markdown("#### Database Experience")


if __name__ == "__main__":
    skills()
