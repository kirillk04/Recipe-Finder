# Recipe Finder

Summary:
A Flask web application designed to search and display recipes using the Spoonacular API. The app allows users to submit search queries, fetches recipe data from the Spoonacular API, and presents the results on the main page. Additionally, users can view detailed information about a specific recipe by navigating to a dedicated recipe view.

Key Components:
1. Flask Application Setup:

- Import necessary modules, including Flask, render_template, and requests.
- Create a Flask app instance.

2. Spoonacular API Integration:

- Utilize the Spoonacular API for recipe data.
- Replace the placeholder 'API_KEY' with a valid Spoonacular API key.

3. Routes:

- Home Route: Renders the main page with an empty recipe list and search query.
- Index Route: Handles both GET and POST requests.
 - - On POST, performs a recipe search based on the submitted form data.
 - - On GET, fetches and displays recipes based on the provided or decoded search query.

4. Search Functionality:

- search_recipes(query): Performs a GET request to the Spoonacular API's complexSearch endpoint with specified parameters.
- Parses the API response, returning a list of recipe results.

5. Recipe View:

- /recipe/<int:recipe_id> Route: Displays detailed information about a specific recipe.
- Fetches recipe data using the Spoonacular API with the given recipe ID.
