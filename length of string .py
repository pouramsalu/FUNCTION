def string(list):
    i=0
    count=0
    while i<len(list):
        if list[i][0]==list[i][-1]:
            count=count+1
        i+=1
    print(count)
list=["abc","xyz","aba","1221"]
string(list)

# def string(x):
#     i=0
#     b=[]
#     while i<len(x):
#         if x[i] not in b:
#             b.append(x[i])
#         i+=1
#     return b
# print(string)