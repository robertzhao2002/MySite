from flask import Flask, jsonify, render_template, request
from flask import abort
from flask import make_response

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
