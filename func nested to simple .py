def simple(a):
    new_list=[]
    i=0
    while i<len(a):
        if type(a[i])is list:
            new_list:(a[i])
        else:
            new_list.append(a[i])
        i+=1
    print(new_list)
a=[1,2,[3,4],[5,6],7,8,[9,10]]
simple(a)