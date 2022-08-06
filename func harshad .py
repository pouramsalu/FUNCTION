# HARSHAD NUMBER:number divisile by the sum of the digit
def harshad(num):
    n=num
    sum=0
    while n>0:
        a=n%10
        sum=sum+a
        n=n//10
    if num%sum==0:
        print(num,"is harshad number")
    else:
        print(num,"is not a harshad number")
num=int(input("enter number"))
harshad(num)
