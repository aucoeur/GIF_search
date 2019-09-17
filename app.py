from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Returns homepage"""

    """Heading"""
    section = 'WELCOME TO GIF SEARCH'
    subtitle = 'compliments of Tenor API'
    
    url = "http://api.tenor.com/v1/"
    request_type = request.args.get('request')

    """'params' dictionary contains:
        a) our API key, 'key'
        b) how many GIFs to return, 'limit'
        c) and depending on situation, the search term, 'query'"""
    params = {
        'key': '7YRWBT7DN78Q',
        'limit': '10'}

    """Add correct link address"""
    if request_type == "trending":
        query_link = url + "trending"
    elif request_type == "rpdr":
        params.update({ 'q' : 'laganja' }) 
        query_link = url + "search"
    else:
        query = request.args.get('search')
        
        """Add query to params"""
        params.update({ 'q' : query })  
        
        if request_type == "random": 
            query_link = url + "random"
        else:
            query_link = url + "search"    

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
        gif_output = gif_output)

if __name__ == '__main__':
    app.run(debug = True)
