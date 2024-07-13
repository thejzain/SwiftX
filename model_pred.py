''' # Imporiting libraries
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import pandas as pd

model = load_model('model.h5')

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# sample data to predict output from 'model.h5'
new_data = pd.DataFrame({
    'gender': ['M', 'F'],
    'year': [2024, 2024],
    'month': [1, 12],
    'day': [21, 21],
    'hour': [12, 12],
    'minute': [0, 60],
    'second': [0, 60],
    'amt': [150, 200],
    'dip': [1, 0]
})

new_data = pd.get_dummies(new_data, columns=['gender'], drop_first=True)

expected_columns = ['year', 'month', 'day', 'hour', 'minute', 'second', 'amt', 'dip', 'gender_M']
for col in expected_columns:
    if col not in new_data.columns:
        new_data[col] = 0  

# Scaling | normalization
new_data_scaled = scaler.transform(new_data)

# Prediction
predictions = model.predict(new_data_scaled)

predicted_classes = (predictions > 0.5).astype(int)

for i, prediction in enumerate(predictions):
    print(f"Data point {i+1}: Fraud probability: {prediction[0]}, Predicted class: {predicted_classes[i][0]}") 

'''

import tensorflow as tf
import tf2onnx
import onnx
from tensorflow import keras
from keras.models import load_model

model = load_model('model.h5')

# extraction
input_layer = model.input
output_layer = model.layers[-1].output
functional_model = Model(inputs=input_layer, outputs=output_layer)

onnx_model, _ = tf2onnx.convert.from_keras(functional_model)
onnx.save(onnx_model, 'model.onnx')