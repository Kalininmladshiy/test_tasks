import csv
from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)
fieldnames = ['id', 'title']
file = open('titles_market_news.csv', newline='')  
news = csv.DictReader(file, fieldnames=fieldnames)
class Quote(Resource):
    def get(self, id=0):
        for title in news:
            if(title["id"] == str(id)):
                return title['title'], 200
        return "Title not found", 404    

api.add_resource(Quote, "/market-news", "/market-news/", "/market-news/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
    file.close()