

def fun(num):
    
    i=0
    while i<len(num):
        num.sort()
        i=i+1
    print("second max number=",num[-2])
fun([50,40,23,70,12,5,10,7])