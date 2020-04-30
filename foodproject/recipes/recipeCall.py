import spoonacular as sp
# import urllib3.request
import urllib
import json
from urllib.request import Request, urlopen
import requests
from flask import Flask, render_template, request





# api = sp.API("62398c3d538f461f977a1ad87dc9fe90")
# api = "62398c3d538f461f977a1ad87dc9fe90"
# url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "f6ee1d6b77mshae54a43ea97c4bap119f7ajsn0ce5699b5794"
}



recipes = []
images = []
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
        recipes.append(element['title'])
        images.append(element['image'])
        structure.append(data_set)
        # print(element['id'])
    with open(ingredient + ".json", "w") as write_file:
        json.dump(structure, write_file)
     

app = Flask(__name__)


@app.route('/')
def FrontEnd():
    return render_template('FrontEnd.html')

@app.route('/', methods=['POST'])
def getValues():
    number = int(request.form['nRecipes'])
    ingredients = request.form['ingredients']
    getRecipe(ingredients, number)
    return render_template('FrontEnd2.html', rec = recipes, imgs = images)








