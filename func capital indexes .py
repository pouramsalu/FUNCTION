def capital_indexes(a):
    b=[]
    i=0
    while i<len(a):
        if a[i].isupper()==True:
            b.append(i)
        i+=1
    print (b)
capital_indexes("HeLlO")