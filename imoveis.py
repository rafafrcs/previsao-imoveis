import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import pickle
import json

df = pd.read_csv('dataset/kc_house_data.csv')

features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
            'waterfront', 'view', 'condition', 'grade', 'sqft_above',
            'sqft_basement', 'yr_built', 'yr_renovated', 'lat', 'long',
            'sqft_living15', 'sqft_lot15']

X = df[features]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


with open('modelo_imoveis.pkl', 'wb') as arquivo_modelo:
    pickle.dump(model, arquivo_modelo)


mean_values = X.mean().to_dict()
with open('mean_values.json', 'w') as arquivo_medias:
    json.dump(mean_values, arquivo_medias)

print("Modelo treinado e exportado com sucesso!")
