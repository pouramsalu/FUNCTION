def prime(m,n):
    i=m
    while i<=n:
        j=2
        count=0
        while j<i:
            if i%j==0:
                count+=1
            j+=1
        if count==0:
            print(i,"prime")
        i+=1
m=int(input("enter the number"))
n=int(input("enter the number"))
prime(m,n)