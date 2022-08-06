def multiples(num):
    sum=0
    i=1
    while i<=num:
        if (i%3==0 or i%5==0):
            sum=sum+1
        i+=1
    print(sum)
multiples(10)