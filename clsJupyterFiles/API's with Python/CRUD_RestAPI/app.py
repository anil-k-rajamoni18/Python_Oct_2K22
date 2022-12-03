from flask import Flask , request
from DBModules.CLient import *

app = Flask(__name__)

mycoll  = CreateConnection('Restaurant','fooditems')

print("COnnection successfull...")

@app.route("/")
def index():
  return "<h2><center> Greetings from rest mirco services... </center></h2>"


@app.route("/foods")
def getFoods():
    data = mycoll.find()
    responseData = []
    for dt in data:
      responseData.append(dt)
    return {"data":responseData}

@app.route("/foods/<id>")
def getOneFoodItem(id):
  data = mycoll.find({'_id': int(id)})
  if data:
    responseData = []
    for dt in data:
      responseData.append(dt)
    return {"data":responseData}
  return {"data":"no record found."}


@app.route("/foods",methods=["POST"])
def getDrinks():
  if request.method=="POST":
    data = request.get_json()
    print(type(data))
    data = mycoll.insert_one(data)

    return {"data":data.inserted_id}



if __name__ == '__main__':
  app.run(port='1122',debug=True)
