import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Read and render your index.html file
with open("index.html", "r") as f:
    html_code = f.read()

components.html(html_code, height=800, scrolling=True)
