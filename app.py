from flask import render_template, request, jsonify
from config import db, app
from model import *

@app.route('/')
def home():
    posts = get_all_posts()
    return render_template(
        'home.html',
        posts = posts
    )

if __name__ == "__main__":
    app.run(debug=True)
