from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

apikey = "7YRWBT7DN78Q"

@app.route('/')
def index():
    """Return homepage."""
    section = 'WELCOME TO GIF SEARCH'
    subtitle = 'compliments of Tenor API'

    # TODO: Extract query term from url

    # TODO: Make 'params' dict with query term and API key

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results
    
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template('index.html', 
        section = section,
        subtitle = subtitle)

# @app.route('/gif')
# def get_gif():


if __name__ == '__main__':
    app.run(debug=True)
