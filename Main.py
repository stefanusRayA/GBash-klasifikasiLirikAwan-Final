#from normalization import normalize_corpus
from flask import Flask, jsonify, request
from flasgger import Swagger
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)
Swagger(app)



@app.route('/input/task', methods=['POST'])
def predict():
    """
    Ini Adalah Endpoint Untuk Mengklasifikasi Lirik Lagu
    ---
    tags:
      - Rest Controller
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Lirik
          required:
            - text
          properties:
            text:
              type: string
              description: Please input with valid text.
              default: 0
    responses:
        200:
            description: Success Input
    """
    new_task = request.get_json()
    text = new_task['text']
    X_New = np.array([text])
    #X_New=normalize_corpus(X_New)


    pipe = joblib.load('neuralNetworkClassifier.pkl')
    pipe2 = joblib.load('naiveBayesClassifier.pkl')

    resultGenrePredict = pipe[0].predict(X_New)
    resultEmosiPredict = pipe2[0].predict(X_New)



    return jsonify({'genre': format(resultGenrePredict),'emosi' : format(resultEmosiPredict)})


if __name__ == '__main__':
    app.run(debug=True) #debug=True kalau deploy ga usah pakai ini dia print error
