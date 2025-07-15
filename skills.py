import streamlit as st
import pandas as pd
import altair as alt


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
            color=alt.Color("Level"),
        )
        .configure_axis(
            grid=False,
            tickMinStep=1,
        )
        # .configure_tick(
        #     bandSize=1,
        # )
        .properties(
            height=alt.Step(30),
        )
    )

    st.altair_chart(prog_lang_skills_chart)

    st.markdown("#### Python Frameworks")
    st.markdown("#### SQL Flavours")


if __name__ == "__main__":
    skills()
