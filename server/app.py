from flask import Flask, request, jsonify
import pickle
import os
import os.path
import time
import pandas as pd

docker_image_tag = os.environ.get('IMAGE_VERSION', 'Unknown')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/api/recommend", methods=["POST"])

def recommend():
    
    data = request.get_json(force=True)
    input_songs = data['songs']
    model_date = time.ctime(os.path.getmtime("/data/rules.pickle"))
    app.rules = pickle.load(open('/data/rules.pickle', 'rb'))

    recommend = set()
    
    for _, row in app.rules.iterrows():
        for i in input_songs:
            if i in row['antecedents']:
                for x in row['consequents']:
                    recommend.add(x)

    recommend -= set(input_songs)
    print(recommend)

    return jsonify({
            'songs': list(recommend),
            'model_date': model_date,
            'version': docker_image_tag
            })    

if __name__ == '__main__':
    app.run(debug=True)
