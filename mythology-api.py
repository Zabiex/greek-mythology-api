from flask import *
from flask import jsonify
from flask import Response
from pymongo import MongoClient
from bson.json_util import dumps
import os

mongoClient = MongoClient('mongodb+srv://zabi:zabi@cluster0.yvpfb.mongodb.net/greek-mythology?retryWrites=true&w=majority')
db = mongoClient['greek-mythology']

app = Flask(__name__)


@app.route('/figures',methods=["GET"])
def figures():
    cursor = db.figures.find()
    listFig = list(cursor)
    return render_template("gods.html",allFigures=listFig)

@app.route('/figures/<name>',methods=["GET"])
def figure(name):
    name = name.lower()
    name = name.capitalize()
    cursor = db.figures.find({"name":{"$in":[name]}})
    listFig = list(cursor)
    return render_template("figure.html",figure=listFig[0])

@app.route('/gods',methods=["GET"])
def gods():
    cursor = db.figures.find({"category":"major olympians"})
    listFig = list(cursor)
    return render_template("gods.html",allFigures=listFig)

@app.route('/titans',methods=["GET"])
def titans():
    cursor = db.figures.find({"category":"titan"},{"name":1, "_id":0})
    listFig = list(cursor)
    allFigures = dumps(listFig)
    return Response(allFigures,mimetype="application/json")


@app.route('/12titans',methods=["GET"])
def titans12():
    cursor = db.figures.find({"category":"twelve titan"},{"name":1, "_id":0})
    listFig = list(cursor)
    allFigures = dumps(listFig)
    return Response(allFigures,mimetype="application/json")


## Put the timestamp to the css files to override cached ones
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(host="0.0.0.0")