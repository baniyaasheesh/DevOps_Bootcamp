from flask import Flask, request, jsonify, render_template
from datetime import datetime
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
app = Flask(__name__)




client = MongoClient(MONGO_URI)
db = client.test
collection = db['testing']

@app.route('/')
def home():
    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day=day_of_week, time=current_time)


@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)

    return "Data inserted successfully"







@app.route('/secound', methods=['POST'])
def second():
    return "This is route 2 "

@app.route('/user_info')
def user_info():
    name = request.args.get('name')
    age = request.args.get('age')
    if age is not None:
        try:
            age = int(age)
        except ValueError:
            return "Invalid age value"
    result = {
        "name": name,
        "age": age
    }
    if age is not None and age > 17:
        return result
    else:
        return "you are not eligible to access this api"

if __name__ == '__main__':
    app.run(port=8080, debug=True)