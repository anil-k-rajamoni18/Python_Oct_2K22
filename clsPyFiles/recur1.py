def fun(name,n):
    if(n<=0): #base condition to exit
        return 
    else:
        print(name,n)
        fun(name , n-2)

fun("AK",10)