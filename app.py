import pandas as pd
import pickle
from flask import Flask, request, jsonify

# Creating a Flask app
app = Flask(__name__)

# Loading the machine learning model from a pickle file
model = pickle.load(open("model.pkl", "rb"))

# Define a route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get JSON data from the request
    json_ = request.json

    # Convert JSON data into a DataFrame
    df = pd.DataFrame(json_)

    # Use the loaded model to make predictions on the DataFrame
    prediction = model.predict(df)

    # Return the predictions as a JSON response
    return jsonify({"Prediction": list(prediction)})

# Run the Flask app when this script is executed
if __name__ == "__main__":
    app.run(debug=True)