from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB setup
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['mydatabase']  # Change as needed
collection = db['mycollection']  # Change as needed

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html', error=None)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    try:
        collection.insert_one({'name': name, 'email': email})
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
