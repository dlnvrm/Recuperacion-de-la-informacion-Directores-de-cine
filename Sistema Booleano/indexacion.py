# indexacion.py
#
# Construye el índice invertido con Whoosh.
#
# ¿Qué es un índice invertido?
#   Guarda "término → documentos que lo contienen".
#   Ejemplo:
#     "terror"    → {4.txt, 9.txt, 59.txt}
#     "español"   → {1.txt, 2.txt, 3.txt, 4.txt}
#     "terror AND español" → intersección = {4.txt}
#
# Whoosh construye y guarda este índice en disco (carpeta indice/).

import os
from pathlib import Path

from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.analysis import StandardAnalyzer

from preprocesado import preprocesar_texto

BASE            = Path(os.path.dirname(os.path.abspath(__file__)))
RUTA_DOCUMENTOS = BASE / "datos" / "documentos"
CARPETA_INDICE  = BASE / "indice"

# Esquema: cada documento tiene un ID (nombre de archivo) y un contenido (texto preprocesado)
SCHEMA = Schema(
    id       = ID(stored=True),
    contenido= TEXT(stored=False, analyzer=StandardAnalyzer())
)


def construir_indice() -> None:
    """
    Lee todos los .txt de datos/documentos/, los preprocesa y los indexa.
    Guarda el índice en la carpeta indice/.
    """
    CARPETA_INDICE.mkdir(exist_ok=True)

    ix     = index.create_in(str(CARPETA_INDICE), SCHEMA)
    writer = ix.writer()

    archivos = sorted(
        f for f in RUTA_DOCUMENTOS.iterdir()
        if f.suffix == ".txt" and f.stat().st_size > 0
    )

    for ruta in archivos:
        texto_prep = preprocesar_texto(ruta.read_text(encoding="utf-8"))
        writer.add_document(id=ruta.name, contenido=texto_prep)

    writer.commit()
    print(f"  ✓  Índice creado: {len(archivos)} documentos → '{CARPETA_INDICE.name}/'")


def abrir_indice():
    """Abre el índice ya creado en disco."""
    if not CARPETA_INDICE.exists():
        raise FileNotFoundError(
            f"No se encuentra '{CARPETA_INDICE}'.\n"
            "Ejecuta primero construir_indice()."
        )
    return index.open_dir(str(CARPETA_INDICE))
