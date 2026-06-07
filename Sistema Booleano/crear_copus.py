import os

import requests


BASE = os.path.dirname(os.path.abspath(__file__))
RUTA = os.path.join(BASE, "datos", "documentos")
os.makedirs(RUTA, exist_ok=True)


directores = [
    "Pedro_Almodóvar",
    "Luis_Buñuel",
    "Alejandro_Amenábar",
    "Álex_de_la_Iglesia",
    "Fernando_Trueba",
    "Icíar_Bollaín",
    "Carlos_Saura",
    "Víctor_Erice",
    "Bigas_Luna",
    "Juan_Antonio_Bayona",
    "Julio_Médem",
    "Isabel_Coixet",
    "Emilio_Martínez-Lázaro",
    "Fernando_León_de_Aranoa",
    "Montxo_Armendáriz",
    "Steven_Spielberg",
    "Martin_Scorsese",
    "Stanley_Kubrick",
    "Francis_Ford_Coppola",
    "Quentin_Tarantino",
    "Christopher_Nolan",
    "Alfred_Hitchcock",
    "Orson_Welles",
    "Billy_Wilder",
    "Woody_Allen",
    "Tim_Burton",
    "David_Lynch",
    "Ridley_Scott",
    "James_Cameron",
    "Clint_Eastwood",
    "Oliver_Stone",
    "Spike_Lee",
    "Wes_Anderson",
    "David_Fincher",
    "Sofia_Coppola",
    "Guillermo_del_Toro",
    "Alfonso_Cuarón",
    "Alejandro_González_Iñárritu",
    "Fernando_Meirelles",
    "Paolo_Sorrentino",
    "Lars_von_Trier",
    "Michael_Haneke",
    "Yorgos_Lanthimos",
    "Pedro_Costa",
    "Ken_Loach",
    "Jean-Luc_Godard",
    "François_Truffaut",
    "Federico_Fellini",
    "Ingmar_Bergman",
    "Akira_Kurosawa",
    "Hayao_Miyazaki",
    "Isao_Takahata",
    "Makoto_Shinkai",
    "Satoshi_Kon",
    "Bong_Joon-ho",
    "Park_Chan-wook",
    "Kim_Ki-duk",
    "Takashi_Miike",
    "John_Carpenter",
    "Wes_Craven",
    "George_A._Romero",
    "James_Wan",
    "Denis_Villeneuve",
    "Paul_Thomas_Anderson",
    "Robert_Eggers",
    "Greta_Gerwig",
    "Chloé_Zhao",
    "Jane_Campion",
    "Kathryn_Bigelow",
    "Sergio_Leone",
]


def crear_corpus() -> None:
    headers = {"User-Agent": "Sofia-IR-Project/1.0 (sofia@example.com)"}

    for i, nombre in enumerate(directores, start=1):
        url = "https://es.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": True,
            "format": "json",
            "titles": nombre,
        }

        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        datos = response.json()

        page = next(iter(datos["query"]["pages"].values()))
        texto = page.get("extract", "")

        ruta = os.path.join(RUTA, f"{i}.txt")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"Guardado: {ruta}")


if __name__ == "__main__":
    crear_corpus()
