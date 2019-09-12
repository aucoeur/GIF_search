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
    
    # TODO: Extract the query term from url using request.args.get()
    query = request.args.get('search')

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'

    params = {'q': query,
        'key': '7YRWBT7DN78Q',
        'limit': '10'}

    # TODO: Make an API call to Tenor using the 'requests' library. For reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    r = requests.get("https://api.tenor.com/v1/search", params=params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    gif_json = r.json()

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    
    gif_output = gif_json['results']

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template('index.html', 
        section = section,
        subtitle = subtitle,
        stuff = stuff,
        query =  query,
        gif_output = gif_output)

# @app.route('/gif')
# def get_gif():
#     query = request.args.get('search')

#     return render_template('gif.html',
#     query = query,
#     gif_output = gif_output)

if __name__ == '__main__':
    app.run(debug=True)
