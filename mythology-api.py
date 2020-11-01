from flask import *
from flask import jsonify
from flask import Response
from pymongo import MongoClient
from bson.json_util import dumps

mongoClient = MongoClient('mongodb+srv://zabi:zabi@cluster0.yvpfb.mongodb.net/greek-mythology?retryWrites=true&w=majority')
db = mongoClient['greek-mythology']
print(db.figures)

app = Flask(__name__)


@app.route('/figures',methods=["GET"])
def figures():
    cursor = db.figures.find()
    listFig = list(cursor)
    return render_template("gods.html",allFigures=listFig)
    return Response(allFigures,mimetype="application/json")

@app.route('/figures/<name>',methods=["GET"])
def figure(name):
    cursor = db.figures.find({"name":{"$in":[name]}})
    listFig = list(cursor)
    return render_template("figure.html",figure=listFig[0])

@app.route('/gods',methods=["GET"])
def gods():
    cursor = db.figures.find({"category":"major olympians"})
    listFig = list(cursor)
    return render_template("gods.html",allFigures=listFig)
    return Response(allFigures,mimetype="application/json")

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

if __name__ == '__main__':
    app.run(host="0.0.0.0")