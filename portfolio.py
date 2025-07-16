import streamlit as st


def portfolio():
    st.link_button("My Github", "https://github.com/lbhtran")
    st.page_link("https://lbhtran.github.io/", label="My Blog")
    st.markdown("[My LinkedIn](https://www.linkedin.com/in/alex-le-tran/)")


if __name__ == "__main__":
    portfolio()
