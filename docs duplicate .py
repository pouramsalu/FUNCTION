# # Remove duplicate in list;
x=[1,2,2,3,3,3,3,4,5,6,6,7,8,8]
def duplicate(x):
    i=0
    b=[]
    while i<len(x):
        if x[i] not in b:
            b.append(x[i])
        i+=1
    return b
print(duplicate(x))