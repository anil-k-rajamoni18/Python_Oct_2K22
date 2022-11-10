from Utils import *
def main():
  insertData({"name":"Kumar",
              "passwd":"Kumar123"})
  insertData({"name":"Ram",
              "passwd":"Ram123"})

  resData = encryptData()
  loginApp('Kumar',"Kumar123")
  print(resData)

if __name__ == '__main__':
  main()