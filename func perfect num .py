# Perfect Number?
# A perfect number is the one which is equal to the sum of all it's factors(including 1 and excluding itself).



def perfect(x):
    i=1
    while i<=x:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum+=j
            j+=1
        if sum==i:
            print(i,"is perfect number")
        i+=1
perfect(1000)