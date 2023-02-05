from flask import Flask, jsonify, request
import csv

all_articles = []
liked_articles = []
not_liked_articles = []

with open('articles.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    }), 200

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/dislike-article", methods=["POST"])
def dislike_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }), 202

if __name__ == "__main__":
  app.run(debug=True)
