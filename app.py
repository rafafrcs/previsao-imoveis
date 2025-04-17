from flask import Flask, render_template, request
import pickle, json
import pandas as pd

app = Flask(__name__)

# Carregar modelo e médias
with open('modelo_imoveis.pkl', 'rb') as file:
    model = pickle.load(file)

with open('mean_values.json', 'r') as file:
    mean_values = json.load(file)

features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
            'waterfront', 'view', 'condition', 'grade', 'sqft_above',
            'sqft_basement', 'yr_built', 'yr_renovated', 'lat', 'long',
            'sqft_living15', 'sqft_lot15']

m2_to_sqft = 10.7639

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        input_data = {}
        for feature in features:
            valor = request.form.get(feature)
            if not valor:
                input_data[feature] = mean_values[feature]
            else:
                valor = float(valor)
                if feature in ['sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_living15', 'sqft_lot15']:
                    valor *= m2_to_sqft
                input_data[feature] = valor
        df_user = pd.DataFrame([input_data])
        prediction = model.predict(df_user)[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
