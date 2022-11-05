def fun(num):
    if(num>0): #base condition
        print(num) # 4 3 2 1 
        fun(num-1)
        print(num ,end=" ") # 1 2 3 4
        

        
#calling function        
fun(4)