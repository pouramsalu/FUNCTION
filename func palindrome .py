


# def palindrome(a):
#     i=0
#     j=len(a)-1
#     while j>=i:
#         if not a[i]==a[j]:
#             return False
#             i+=1
#             j+=1
#         else:
#             return True
# print(palindrome("mom"))



# Write a python function that check whether a program in string is palindrome or not:
def palindrom():
    string_list=list(string)
    i=-1
    a=[]
    while  i>=-len(string):
        a.append(string[i])
        i-=1
        if string_list==1:
            print("palindrome")
        else:
            print("not palindrome")
string=input("enter string")
palindrom()

