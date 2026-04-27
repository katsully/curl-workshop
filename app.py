from flask import Flask, render_template
from cats import get_cat_gifs

# create a flask app
app = Flask(__name__)

@app.route("/")
def index():
	# call the function in cats.py
	cat_gifs = get_cat_gifs()
	# gifs is a variable set up in index.html
	return render_template('index.html', gifs=cat_gifs)