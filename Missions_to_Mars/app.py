from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import requests

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def index():

    mars_facts = mongo.db.collection.find_one()

    return render_template("index.html", mars_facts=mars_facts)

@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape_info()

    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)