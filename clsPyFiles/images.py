
import os

print(os.getcwd())
os.mkdir("IMAGES2")
os.chdir("./IMAGES2")

imageDict={
  "image1":("flower.jpg","https://images.unsplash.com/photo-1668248949793-12718a4dd485?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=392&q=80"),
   "image2":("sun.jpg","https://images.unsplash.com/photo-1668241282073-2cf47bae10d8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80")

}


import requests as r
for k in imageDict:
  res = r.get(imageDict[k][1])
  with open(imageDict[k][0],"wb") as f:
    f.write(res.content)


print(os.listdir())