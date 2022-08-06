# Given a list of number,write a python program to count positive and negative in a list function.
def positive_negative(list):
    count_positive=0
    sum_negative=0
    a=[]
    i=0
    while i<len(list):
        if list[i]>0:
            count_positive+=1
        else:
            sum_negative+=list[i]
        i+=1
    a.append(count_positive)
    a.append(sum_negative)
    print(a)
list=[2,-4,8,6,-9,-12,5]
positive_negative(list)

# def positive_negative(list):
#     positive_count=0
#     negative_count=0
#     i=0
#     while i<len(list):
#         if list[i]>0:
#             positive_count+=1
#         else:
#             negative_count+=1
#         i+=1
#     print("number of positive:",positive_count)
#     print("number of negative_count:",negative_count)
# list=[2,-7,5,-64,-14]
# positive_negative(list)