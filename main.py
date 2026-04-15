import streamlit as st
import re

st.title("Words counter")

# Text entry
text = st.text_area("Paste the text here:")

def contar_palabras(text):
    # regex for split words (avoid counting multiple spaces)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# Botón
if st.button("Count words"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        total = contar_palabras(text)
        st.success(f"The text has {total} words.")
