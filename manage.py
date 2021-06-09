import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)#our flask app
model = pickle.load(open('weather_prediction2.pickle', 'rb')) #loading the model

@app.route('/')
def home():
    return render_template('home.html')#rendering html page

@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["Date"]
        #Converting date input to a dataframe
        a={"ds":[ds]}
        ds=pd.DataFrame(a)
        #predicting the temperature for the user given input date
        prediction = model.predict(ds)
        output=round(prediction.iloc[0,18],2)#rounding off the decimal values to 2
        print(output)
        return render_template('home.html',prediction_text="Temperature on selected date is. {} degree celsius".format(output))
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=False)
