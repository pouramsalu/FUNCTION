# output: 'my name is Salu'
# output: ['my','name','is','Salu']

def func(list1,list2):
    i=0
    j=0
    b=[]
    d=[]
    while i<len(list1) and j<len(list2):
        a=list1[i]+list2[j]
        b.append(a)
        i+=1
        j+=1
    c=" ".join(b)
    d.append(c)
    print(d)
    print(b)
list1=["m","na","i","Sa"]
list2=["y","me","s","lu"]
func(list1,list2)
