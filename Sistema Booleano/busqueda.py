# busqueda.py
#
# Función de búsqueda booleana usando el índice Whoosh.
#
# Sintaxis soportada (operadores en MAYÚSCULAS):
#   AND  → ambos términos deben aparecer      "español AND terror"
#   OR   → al menos uno debe aparecer         "animación OR anime"
#   NOT  → el término NO debe aparecer        "coreano NOT comedia"
#   ()   → agrupar condiciones                "óscar AND (español OR mexicano)"

import re
from typing import List
from whoosh.qparser import QueryParser

from indexacion import abrir_indice


def normalizar_consulta(consulta: str) -> str:
    """
    Garantiza que los operadores AND/OR/NOT queden en mayúsculas
    y que los términos queden en minúsculas, manteniendo los acentos
    tal como están en el índice (el preprocesado de este sistema
    conserva los acentos).
    """
    tokens = re.findall(r'\(|\)|\bAND\b|\bOR\b|\bNOT\b|[^\s()]+',
                        consulta, flags=re.IGNORECASE)
    resultado = []
    for token in tokens:
        upper = token.upper()
        if upper in {'AND', 'OR', 'NOT'}:
            resultado.append(upper)
        elif token in {'(', ')'}:
            resultado.append(token)
        else:
            resultado.append(token.lower())
    return ' '.join(resultado)


def buscar(consulta: str) -> List[str]:
    """
    Ejecuta una consulta booleana y devuelve la lista de IDs de documentos
    que cumplen la condición.

    Parámetros:
        consulta : cadena con la consulta booleana
                   Ejemplos:
                     "español AND terror"
                     "animación OR anime"
                     "coreano OR surcoreano"
                     "óscar AND (español OR mexicano)"

    Retorna:
        Lista de nombres de archivo, ej: ["1.txt", "3.txt"]
        Lista vacía si no hay resultados.
    """
    ix = abrir_indice()
    consulta_norm = normalizar_consulta(consulta)

    with ix.searcher() as searcher:
        parser     = QueryParser('contenido', ix.schema)
        query      = parser.parse(consulta_norm)
        hits       = searcher.search(query, limit=None)
        resultados = [hit['id'] for hit in hits]

    return resultados
