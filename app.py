from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)



@app.route('/')
def index():
    """Return homepage."""

    section = 'WELCOME TO GIF SEARCH'
    subtitle = 'compliments of Tenor API'
    stuff = 'Dear Diary,<br /><br />It\'s me, Laganja.  <br /><br />Today all the girls sat separate from me and I lived alone under a table.<br /><br />'
    

    # TODO: Extract query term from url
    query = 'laganja'
    # TODO: Make 'params' dict with query term and API key
    params = {'q': query,
        'key': '7YRWBT7DN78Q',
        'limit': '1'}
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search", params=params)
    # TODO: Get the first 10 results from the search results
    gif_json = r.json()
    gif_output = gif_json['results']

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template('index.html', 
        section = section,
        subtitle = subtitle,
        stuff = stuff,
        gif_output = gif_output)

# @app.route('/gif')
# def get_gif():


if __name__ == '__main__':
    app.run(debug=True)
