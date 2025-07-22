import streamlit as st
import pandas as pd


def education():
    data = pd.DataFrame(
        {
            "latitude": [37.7749, 34.0522, 40.7128],
            "longitude": [-122.4194, -118.2437, -74.0060],
        }
    )
    st.map(data)


if __name__ == "__main__":
    education()
