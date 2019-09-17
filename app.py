from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Returns homepage"""

    """Intro text"""

    section = 'WELCOME TO GIF SEARCH'
    subtitle = 'compliments of Tenor API'
    stuff = 'Dear Diary,<br /><br />It\'s me, Laganja.  <br /><br />Today all the girls sat separate from me and I lived alone under a table.<br /><br />'
    
    url = "http://api.tenor.com/v1/"
    request_type = request.args.get('request')

    """'params' dictionary contains:
    # a) the query term, 'q'
    # b) our API key, 'key'
    # c) how many GIFs to return, 'limit'"""
    params = {
        'key': '7YRWBT7DN78Q',
        'limit': '10'}

    if request_type == "trending":
        query_link = url + "trending"
    else:
        query = request.args.get('search')
        if request_type == "random": 
            """Extract the query term from url using request.args.get()"""
            query_link = url + "random"
        else:
            """Extract the query term from url using request.args.get()"""
            query_link = url + "search"

        """Add query to params"""
        params.update({ 'q' : query })      

    """Make an API call to Tenor using the 'requests' library. For reference on how to use Tenor, see: https://tenor.com/gifapi/documentation"""

    r = requests.get(query_link, params = params)

    """Uses '.json()' function to get the JSON of the returned response object"""

    gif_json = r.json()

    """Get the 'results' field of the JSON, containing requested GIFs in a list"""
    
    gif_output = gif_json['results']

    """Render the 'index.html' template, passing the list of gifs as a named parameter called 'gifs'"""

    return render_template('index.html', 
        section = section,
        subtitle = subtitle,
        stuff = stuff,
        gif_output = gif_output)

if __name__ == '__main__':
    app.run(debug = True)
