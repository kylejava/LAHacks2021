from flask import Flask, render_template, request
import requests
import json
from pprint import pprint


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def results():
    businesses = []
    if(request.method == 'POST'):
        choice = request.form['choice']
        location = request.form['location']
        businesses = findBusiness(choice , location)

    return render_template('results.html' , businesses = businesses)

if __name__ == "__main__":
    app.run(debug=True)
