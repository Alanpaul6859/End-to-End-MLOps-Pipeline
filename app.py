from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("models/model.pkl")

@app.route("/")
def home():
    return "MLOps Model API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    prediction = model.predict([data])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
