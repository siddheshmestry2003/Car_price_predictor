from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# Ensure file path is correct
csv_path = os.path.join(os.path.dirname(__file__), 'clean_car_1.csv')
model_path = os.path.join(os.path.dirname(__file__), 'LinearRegressionModel.pkl')

# Load data and model
car = pd.read_csv(csv_path)
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    companies.insert(0, "select company")

    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        kms_driven = int(request.form.get('kilo_driven'))

        input_df = pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        prediction = model.predict(input_df)
        return str(np.round(prediction[0], 2))

    except Exception as e:
        return "Error: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
