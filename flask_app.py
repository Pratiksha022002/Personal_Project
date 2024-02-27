# flask_app.py
import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load your machine learning model
pipe = pickle.load(open("RidgeModel.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Example: data = {"location": "some_location", "bhk": 3, "bath": 2, "total_sqft": 1500}
    input_df = pd.DataFrame(data, index=[0])
    prediction = pipe.predict(input_df)[0] * 1e5
    return jsonify({"prediction": round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
