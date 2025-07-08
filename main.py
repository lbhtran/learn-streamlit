import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


def main():
    st.header("Alex Le Tran")
    st.write("Greeting, Alex!")
    st.write("Greeting, Alex!")

    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

    df = pd.DataFrame(
        {
            "language": ["Python", "SQL", "Javascript", "Lua"],
            "level": [5, 5, 4, 3],
        }
    )
    st.write(df)

    df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
    c = (
        alt.Chart(df2)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )
    st.write(c)


if __name__ == "__main__":
    main()
