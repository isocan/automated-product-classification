import requests
import pandas as pd

# URL de l'API Edamam Food and Grocery Database
url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

# Paramètres de la requête pour rechercher "champagne"
querystring = {"ingr": "champagne"}

# En-têtes de la requête avec la clé d'API RapidAPI
headers = {
    "X-RapidAPI-Key": "97d2e532a3msh172615c4013bd38p190045jsn3015f56fe96c",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

# Envoyer une requête GET à l'API
response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Vérifier si des données sont présentes dans la réponse
if "hints" in data:
    # Extraire les 10 premiers résultats
    hints = data["hints"][:10]

    # Créer une liste de dictionnaires contenant les colonnes souhaitées
    product_list = []
    for hint in hints:
        product = {
            "foodId": hint["food"]["foodId"],
            "label": hint["food"]["label"],
            "category": hint["food"]["category"]
        }
        if "foodContentsLabel" in hint["food"]:
            product["foodContentsLabel"] = hint["food"]["foodContentsLabel"]
        else:
            product["foodContentsLabel"] = None
        if "image" in hint["food"]:
            product["image"] = hint["food"]["image"]
        else:
            product["image"] = None
        product_list.append(product)

    # Convertir la liste de dictionnaires en un DataFrame
    df = pd.DataFrame(product_list)

    # Enregistrer le DataFrame dans un fichier CSV
    df.to_csv("produits_champagne.csv", index=False)

    print("Fichier CSV 'produits_champagne.csv' enregistré avec succès.")
else:
    print("Aucune donnée trouvée.")
