# preprocesado.py

import re
import nltk
from nltk.corpus import stopwords

# Asegúrate de haber descargado esto una vez:
# nltk.download('punkt')
# nltk.download('stopwords')

stopwords_es = set(stopwords.words('spanish'))

def normalizar(texto: str) -> str:
    """
    Pasa a minúsculas y elimina caracteres raros.
    """
    texto = texto.lower()
    # Sustituimos cualquier cosa que no sea letra o número por espacio
    texto = re.sub(r'[^a-záéíóúüñ0-9]+', ' ', texto)
    return texto

def tokenizar(texto: str) -> list[str]:
    """
    Divide el texto en palabras (tokens).
    """
    from nltk.tokenize import word_tokenize
    return word_tokenize(texto)

def limpiar_tokens(tokens: list[str]) -> list[str]:
    """
    Elimina stopwords y tokens muy cortos.
    """
    tokens_limpios = [
        t for t in tokens
        if t not in stopwords_es and len(t) > 2
    ]
    return tokens_limpios

def preprocesar_texto(texto: str) -> str:
    """
    Pipeline completo: normalizar + tokenizar + limpiar,
    y devolver un string listo para TF-IDF.
    """
    texto = normalizar(texto)
    tokens = tokenizar(texto)
    tokens = limpiar_tokens(tokens)
    return " ".join(tokens)
