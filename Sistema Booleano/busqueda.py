# busqueda.py
#
# Función de búsqueda booleana usando el índice Whoosh.
#
# Sintaxis soportada (operadores en MAYÚSCULAS):
#   AND  → ambos términos deben aparecer      "español AND oscar"
#   OR   → al menos uno debe aparecer         "terror OR suspense"
#   NOT  → el término NO debe aparecer        "americano NOT comedia"
#   ()   → agrupar condiciones                "oscar AND (español OR mexicano)"

from typing import List
import re
from whoosh.qparser import QueryParser

from indexacion import abrir_indice


def normalizar_consulta_booleana(consulta: str) -> str:
    """
    Normaliza los términos de la consulta sin romper AND/OR/NOT ni paréntesis.
    """
    tokens = re.findall(r"\(|\)|\bAND\b|\bOR\b|\bNOT\b|[^\s()]+", consulta, flags=re.IGNORECASE)
    normalizados: list[str] = []

    for token in tokens:
        token_mayus = token.upper()
        if token_mayus in {"AND", "OR", "NOT"}:
            normalizados.append(token_mayus)
        elif token in {"(", ")"}:
            normalizados.append(token)
        else:
            normalizados.append(token.lower())

    return " ".join(normalizados)


def buscar(consulta: str) -> List[str]:
    """
    Ejecuta una consulta booleana y devuelve la lista de IDs de documentos
    que cumplen la condición.

    Parámetros:
        consulta : cadena con la consulta booleana
                   Ejemplos:
                     "español AND oscar"
                     "terror OR suspense"
                     "coreano NOT comedia"
                     "oscar AND (español OR mexicano)"

    Retorna:
        Lista de nombres de archivo encontrados, ej: ["1.txt", "3.txt"]
        Lista vacía si no hay resultados.
    """
    ix = abrir_indice()

    with ix.searcher() as searcher:
        parser     = QueryParser("contenido", ix.schema)
        consulta   = normalizar_consulta_booleana(consulta)
        query      = parser.parse(consulta)
        hits       = searcher.search(query, limit=None)  # limit=None → todos los resultados
        resultados = [hit["id"] for hit in hits]

    return resultados
