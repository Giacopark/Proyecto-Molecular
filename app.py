from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


HTML_FILE = Path(__file__).with_name("Proyecto_Molecular.html")

st.set_page_config(
    page_title="Laboratorio Atómico Interactivo",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_data
def load_html() -> str:
    return HTML_FILE.read_text(encoding="utf-8")


st.title("Laboratorio Atómico Interactivo")
st.caption("Visualizador educativo de átomos, isótopos y partículas")

if not HTML_FILE.exists():
    st.error(f"No se encontró la interfaz: {HTML_FILE}")
else:
    html = load_html()
    components.html(html, height=5400, scrolling=True)