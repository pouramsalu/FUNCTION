


# def string(x):
#     i=0
#     b=[]
#     while i<len(x):
#         if x[i] not in b:
#             b.append(x[i])
#         i+=1
#     return b
# x=['A','A','A','A','B','B','B','C','C','D','A','A','B','B','B']
# print(string(x))

# def phone_no():
#     a=[[1,2,3,0,5,6,0,8,9]]
#     b=" "
#     c=" "
#     i=0
#     while i<len(a):
#         if i<3:
#             b=b+str(a[i])
#         elif i>=3 and i<=5:
#             c=c+str(a[i])
#         elif i>5 and i>=6:
#             d=d+str(a[i])
#         i+=1
#     y="("+b+")"
# print("phone_no:",y+c+d)
# phone_no( )

def string(list):
    i=0
    a=""
    while i<len(list)-1:
        if list[i]!=list[+1]:
            a=a+list[i]
        i+=1
    a=a+list[i]
    print(a)
list=['a','b','b','c','c','d','e','e','e','f','g']
string(list)

