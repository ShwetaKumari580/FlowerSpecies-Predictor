# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from FlowerSpeciesPred import FlowerSpecies
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To my World!': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed

@app.post('/predict')
def predict_flowerspecies(data:FlowerSpecies):
    data = data.dict()
    Sepal_Length=data['Sepal_Length']
    Sepal_Width=data['Sepal_Width']
    Petal_Length=data['Petal_Length']
    Petal_Width=data['Petal_Width']
    prediction = classifier.predict([[Sepal_Length,Sepal_Width,Petal_Length,Petal_Width]])
    if prediction == "setosa":
        prediction="This flower belongs to Setosa species."
    elif prediction == "virginica":
        prediction="This flower belongs to Virgina species."
    else:
        prediction="This flower belongs to Versicolor species."
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload