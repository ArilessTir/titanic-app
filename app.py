from flask import Flask, request
import pandas as pd
import pickle
from Model.monitoring import *

app = Flask(__name__)

model = pickle.load(open('Model.sav', 'rb'))

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Titanic Survived Prediction API!'

def readPostData(request):
    return pd.read_json(request, orient='index').transpose()

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return 'Welcome to predict Endpoint send a json with Pclass Sex and Age to get a prediction'
    elif request.method == 'POST':
        data = readPostData(request.data)
        pred = model.predict(data)
        data['prediction'] = pred
        predictionOverview(data)
        return f'{pred}'

if __name__ == '__main__':
    app.run()
