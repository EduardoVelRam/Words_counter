import streamlit as st
import re

st.title("Words counter")

# Entrada de texto
texto = st.text_area("Paste the text here:")

def contar_palabras(texto):
    # Usamos regex para separar palabras (evita contar espacios múltiples)
    palabras = re.findall(r'\b\w+\b', texto)
    return len(palabras)

# Botón
if st.button("Count words"):
    if texto.strip() == "":
        st.warning("Please enter some text.")
    else:
        total = contar_palabras(texto)
        st.success(f"The text has {total} words.")
