import streamlit as st
import re

st.title("Contador de palabras")

# Entrada de texto
texto = st.text_area("Ingresa tu texto aquí:")

def contar_palabras(texto):
    # Usamos regex para separar palabras (evita contar espacios múltiples)
    palabras = re.findall(r'\b\w+\b', texto)
    return len(palabras)

# Botón
if st.button("Contar palabras"):
    if texto.strip() == "":
        st.warning("Por favor ingresa algún texto.")
    else:
        total = contar_palabras(texto)
        st.success(f"El texto tiene {total} palabras.")