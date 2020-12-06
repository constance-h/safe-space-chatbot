from flask import Flask, render_template, request, jsonify 
from chatbot import bot
import os
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@app.route('/get_response', methods=['POST'])
def get_bot_response():
   
    user_input = request.form.get("msg")
    bot_response = bot.get_response(user_input)
        
    return str(bot_response)

@app.route('/therapy_locator')
def therapy_locator():
    return render_template('locator.html')

@app.route('/therapy_data.json', methods =['POST'])
def compile_therapy_data():
    """Locate therapists via Yelp"""

    keywords = request.form.get('keywords-field')
    radius = request.form.get('radius-field')
    location = request.form.get('location-field')
    
    #if given radius, convert to meters for API
    #else use max range, 25 miles (40000 meters)
    if radius:
        radius = int(radius)
        radius *= 1609.34

    else:
        radius = 40000

    #split keyword into list and rejoin with commas in case user enters muliple keywords
    if keywords:
        keywords = ",".join(keywords.split())
    

    params = {
        'term': 'therapy %s' %keywords,
        'limit' : 50,
        'categories': 'c_and_mh, All',
        'radius' : int(radius),
        'location' : location 
    }
  
    yelp_key = os.environ['YELP_KEY']
   

    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization' : 'bearer %s' % yelp_key}

    res = requests.get(
        url = endpoint,
        params = params,
        headers = headers
    )
    
    data = res.json()

    if data['total'] > 0: 
        therapist_data = data['businesses']

        therapists = []
        
        for therapist in therapist_data:
            therapists.append(
                {
                    'name' : therapist['name'],
                    'url' : therapist['url'],
                    'coords' : {'lat' : therapist['coordinates']['latitude'], 'lng' : therapist['coordinates']['longitude']},
                    'phone' : therapist['display_phone'],
                    'address' : therapist['location']['display_address']

                }
            )
       
        return jsonify({'therapists' : therapists})
    else:
      
        return "error"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
