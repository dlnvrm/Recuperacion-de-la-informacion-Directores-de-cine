# preprocesado.py
#
# Limpia y normaliza el texto antes de indexarlo.
# Mismo proceso que el Sistema TF-IDF para que los tokens sean compatibles.

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt',     quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

stopwords_es = set(stopwords.words('spanish'))

def preprocesar_texto(texto: str) -> str:
    """
    Pipeline completo:
      1. Minúsculas
      2. Eliminar caracteres raros (solo letras españolas y números)
      3. Tokenizar
      4. Quitar stopwords ("de", "la", "que"...)
      5. Quitar tokens muy cortos
    Devuelve un string con los tokens limpios separados por espacios.
    """
    # 1. Minúsculas
    texto = texto.lower()
    # 2. Solo letras españolas y números
    texto = re.sub(r'[^a-záéíóúüñ0-9]+', ' ', texto)
    # 3. Tokenizar
    tokens = word_tokenize(texto, language='spanish')
    # 4 y 5. Quitar stopwords y tokens muy cortos
    tokens = [t for t in tokens if t not in stopwords_es and len(t) > 2]
    return " ".join(tokens)
