# By using reverse function print the reverse order of the list.
# reverse_list=["Z","A","A","B","E","M","A","R","D"]
# output = ["D", "R", "A", "M", "E", "B", "A", "A", "Z"]

# def reverse_list(numbers):
#     i=0
#     while i<len(numbers):
#         numbers.reverse()
#         i+=1
#     print(numbers)
# numbers=["Z","A","A","B","E","M","A","R","D"]
# reverse_list(numbers)


# write a python program to reverse a string in function:
def reverse(string):
    i=-1
    while i>=-len(string):
        print(string[i],end=" ")
        i-=1
string=input("enter string")
reverse(string)

def string(num):
    i=1
    b=[]
    while i<=10:
        b.append(i)
        i+=1
    return b
num=int(input("enter the number"))
string(num)

