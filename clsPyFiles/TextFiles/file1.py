#writing 
data=open("list.py", mode="w")
data.write("""print("hello python lovers") \n""")
data.write("a=10\n")
data.write("b=10\n")
data.write("""print(int(a) + int(b))""")
data.close()

#reading
read_data=open("list.py")
print("***************", type(read_data))


for ch in read_data:
  print(f"charecters are: {ch}")