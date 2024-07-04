# app.py
from flask import Flask, request, jsonify, render_template
from model import predict_rank

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    rank = predict_rank(data)
    return jsonify({"data":data,'rank': rank})

if __name__ == '__main__':
    app.run(debug=True)
