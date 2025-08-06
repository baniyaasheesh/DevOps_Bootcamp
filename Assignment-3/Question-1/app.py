from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

def read_data():
    if not os.path.exists(DATA_FILE):
        # Create file with default data if it doesn't exist
        with open(DATA_FILE, 'w') as f:
            json.dump(["Asheesh1", "Asheesh2", "Asheesh3"], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

@app.route('/api', methods=['GET'])
def api():
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
