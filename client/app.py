from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        # Get the list of songs from the form
        songs = request.form['songs'].split(', ')
        # Prepare the data for the POST request to the API
        data = {'songs': songs}
        headers = {'Content-Type': 'application/json'}
        
        # URL for the REST API endpoint, replace with the actual URL of your API
        api_url = "http://project-2-server-deployment-zz264:52007/api/recommend"
        
        # Send the POST request and get the response
        response = requests.post(api_url, json=data, headers=headers)
        
        # Convert the response to JSON
        recommendations = response.json()
        
        # Render the recommend.html template with the recommendations data
        return render_template('recommend.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)