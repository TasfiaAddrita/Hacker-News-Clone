from flask import render_template, request, jsonify
from config import db, app
from model import *

@app.route('/')
def home():
    return render_template(
        'home.html'
    )

if __name__ == "__main__":
    app.run(debug=True)
