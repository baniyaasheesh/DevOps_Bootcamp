from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process():
    data = request.form.to_dict()
    # Process the data as needed
    return jsonify({'message': f"Received: {data}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
