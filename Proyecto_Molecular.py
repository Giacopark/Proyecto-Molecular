"""Lanza el visualizador atómico HTML en un navegador local."""
from pathlib import Path
import webbrowser


HTML_FILE = Path(__file__).with_name("Proyecto_Molecular.html")


if __name__ == "__main__":
    if not HTML_FILE.exists():
        raise FileNotFoundError(f"No se encontró la interfaz: {HTML_FILE}")
    webbrowser.open(HTML_FILE.as_uri())
