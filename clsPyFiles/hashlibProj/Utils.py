userData = []
def genereteEn(passwd):
    import hashlib
    
    return hashlib.md5(passwd.encode()).hexdigest()

def insertData(data):
  global userData
  userData.append(data)

def encryptData():
  global userData
  for data in userData:
    for k in data:
      if k == "passwd":
        data[k] = genereteEn(data[k])

  return userData
  

def loginApp(inpusername,inppasswd):
  print("login appp....")
  flag = False
  for data in userData:
    for k in data:
      if data[k] == inpusername:
        flag = True
        if checkLoginPasswd(data,inppasswd):
          print("Login Success..")
        else:
          print("Invalid passwd...")
  if flag == False:
    print("Invalid username")
def checkLoginPasswd(data,inppasswd):
  for k in data:
    if data["passwd"]==genereteEn(inppasswd):
      return True

      

