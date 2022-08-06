# # find the max

# def max_two(a,b):
#     if a>b:
#         return a
#     return b
# def max_three(a,b,c):
#     return max_two(a,max_two(b,c))
# print(max_three(48,23,45))


# # 1 . You have to print the largest value out of the given list using the max function.
# # numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# def function_name(numbers):
#     i=0
#     a=[]
#     while i<len(numbers):
#         a=max(numbers)
#         i+=1
#     print(a)
# numbers=[3,5,7,34,2,89,2,5]
# function_name(numbers)


# # numbers=[50,40,23,70,56,12,5,10,7]
# def function_name(numbers):
#     i=0
#     s=0
#     b=0
#     while i<len(numbers):
#         if numbers[i]>b:
#             b=numbers[i]
#         if numbers[i]>s and numbers[i]!=b:
#             s=numbers[i]
#         i+=1
#     print(s)
# numbers=[50,40,23,70,56,12,5,10,7]
# function_name(numbers)


# num=[50,40,23,70,12,5,10,7]
# def check():
#     i=0
#     l=num[0]
#     s=num[0]
#     i=0
#     while i<len(num):
#         if num[i]<l:
#             l=num[i]
#         i+=1
#     i=0
#     while i<len(num):
#         if num[i]>s and num[i]!=l:
#             s=num[i]
#         i+=1
#     print(s)
# check()

