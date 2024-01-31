from flask import Flask, render_template, request
import requests
from urllib.parse import unquote

#Create the app and put in API
app = Flask(__name__)
API_KEY = '15556e5a557d4180886e83f9cb2712d5'

#search for recipes
def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    # send a GET request to the API with the query parameters
    response = requests.get(url, params=params)
    #API call is successful
    if response.status_code == 200:
        # parse the API response as JSON data
        data = response.json()
        return data['results']
    # API call is not successful
    return []


# routes
@app.route('/home', methods=['GET'])
def home():
    # empty list and search at home
    return render_template('index.html', recipes=[], search_query='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # when form is submitted, use given query to seach
        query = request.form.get('search_query', '')
        recipes = search_recipes(query)
        # render main page with the search results and the search query
        return render_template('index.html', recipes=recipes, search_query=query)
    
    # if GET request or no form submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    # search for recipes with the decoded search query
    recipes = search_recipes(decoded_search_query)
    # render main page
    return render_template('index.html', recipes=recipes, search_query=decoded_search_query)


# specific recipe with a given recipe ID
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    # get the search query from the URL query 
    search_query = request.args.get('search_query', '')
    # URL to get information about the recipe ID from API
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }

    # send GET request to the API to get the recipe information
    response = requests.get(url, params=params)
    # API call is successful
    if response.status_code == 200:
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404 #unsuccessful API call

if __name__ == '__main__':
    app.run(debug=True)