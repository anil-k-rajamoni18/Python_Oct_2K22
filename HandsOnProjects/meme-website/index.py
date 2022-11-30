from flask import Flask, render_template 

import json
import requests


app = Flask(__name__)


def get_meme():
  # src = /wholesomememes
  # url = https://meme-api.herokuapp.com/gimme + src

  url = "https://meme-api.herokuapp.com/gimme"

  response = requests.request("GET", url)
  if(response.status_code==200):
    data = response.json()
    meme_large = data["preview"][-2]

    subreddit = data["subreddit"]

    return meme_large, subreddit


@app.route("/")
def home():
  return "<h2> Hello Welcome to Memes Page </h2>"

@app.route("/meme")
def getmeme():
  meme_pic, subreddit = get_meme()

  print(meme_pic, subreddit)

  return render_template("meme_index.html",meme_pic = meme_pic , subreddit = subreddit) 



if __name__ == '__main__':
  app.run(host='0.0.0.0',port=1122)

  