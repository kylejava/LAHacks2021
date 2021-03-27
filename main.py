from flask import Flask, render_template
import requests
import json
from pprint import pprint


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)
