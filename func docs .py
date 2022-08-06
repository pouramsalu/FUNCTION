def list(numbers):
    i=1
    square=0
    a=[]
    b=[]
    while i<=numbers:
        square=i**2
        a.append(square)
        i+=1
    x=(a[:5])
    y=(a[25:])
    b.append(x)
    b.append(y)
    print(b)
list(30)