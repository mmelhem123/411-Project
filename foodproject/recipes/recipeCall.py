import spoonacular as sp
# import urllib3.request
import urllib
import json
from urllib.request import Request, urlopen
import requests

# api = sp.API("62398c3d538f461f977a1ad87dc9fe90")
# api = "62398c3d538f461f977a1ad87dc9fe90"
# url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "f6ee1d6b77mshae54a43ea97c4bap119f7ajsn0ce5699b5794"
}


def getRecipe(ingredient, number):
    querystring = {"number": str(number), "ranking": "1", "ignorePantry": "false", "ingredients": str(ingredient)}

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(type(response))
    # print(response.text)
    json_data = json.loads(response.text)
    with open("data_file.json", "w") as write_file:
        json.dump(json_data, write_file)
    structure = []
    with open("data_file.json", "r") as read_file:
        data_dict = json.load(read_file)
    for element in data_dict:
        #  "ingredients": element['missedIngredients'] for other uses
        data_set = {"model": "recipes.Recipe",
                    "fields": {"id": element['id'], "ingredient": ingredient, "recipe": element['title'],
                               "picture": element['image'],
                               }}
        print(data_set)
        structure.append(data_set)
        # print(element['id'])
    with open(ingredient + ".json", "w") as write_file:
        json.dump(structure, write_file)


getRecipe("beef", 20)
