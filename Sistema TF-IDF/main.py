# main.py

from indexacion import construir_indice
from busqueda import buscar
from evaluacion import mean_average_precision

def main():
    print("Construyendo índice TF-IDF...")
    vectorizador, matriz_tfidf, ids_documentos = construir_indice()
    print(f"Índice construido con {len(ids_documentos)} documentos.")

    # Ejemplo de búsqueda
    consulta = "directores españoles de terror"
    print(f"\nConsulta: {consulta}")
    resultados = buscar(consulta, vectorizador, matriz_tfidf, ids_documentos, k=10)

    print("\nTop 10 documentos:")
    for doc_id, sim in resultados:
        print(f"{doc_id}\t{sim:.4f}")

    # Evaluación MAP
    print("\nCalculando MAP sobre todas las necesidades de información...")
    map_score = mean_average_precision(vectorizador, matriz_tfidf, ids_documentos)
    print(f"MAP = {map_score:.4f}")

if __name__ == "__main__":
    main()
