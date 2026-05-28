# busqueda.py

from typing import List, Tuple
from sklearn.metrics.pairwise import cosine_similarity

from preprocesado import preprocesar_texto

def buscar(
    query: str,
    vectorizador,
    matriz_tfidf,
    ids_documentos: List[str],
    k: int | None = None
) -> List[Tuple[str, float]]:
    """
    Dada una consulta en texto libre, devuelve una lista de tuplas:
    (id_documento, similitud), ordenada de mayor a menor similitud.

    Si k no es None, devuelve solo los k primeros.
    """
    query_preprocesada = preprocesar_texto(query)
    vector_q = vectorizador.transform([query_preprocesada])

    similitudes = cosine_similarity(vector_q, matriz_tfidf)[0]  # array de tamaño n_docs

    # Ordenamos índices de mayor a menor similitud
    indices_ordenados = similitudes.argsort()[::-1]

    resultados = [
        (ids_documentos[i], float(similitudes[i]))
        for i in indices_ordenados
    ]

    if k is not None:
        resultados = resultados[:k]

    return resultados
