# # find the minimum
# output\\ 7

# def min_two(a,b):
#     if a<b:
#         return a
#     return b
# def min_three(a,b,c):
#     return min_two(a,min_two(b,c))
# print(min_three(45,65,7))


# Use the min function and find the minimun value of the list
# list = [8, 6, 4, 8, 4, 50, 2, 7] 
# output\\2
def minimum(numbers):
    i=0
    a=[]
    while i<len(numbers):
        a=min(numbers)
        i+=1
    print(a)
numbers=[8,6,44,8,4,50,2,7]
minimum (numbers)
