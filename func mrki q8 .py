# Create a function which takes one argument (a positive integer) and returns a dictionary which has numbers from 1 to the integer (passed as parameter) as the keys and their respective squares as the values as shown in the examble below.
def function_num(numbers):
    i=1
    while i<=numbers:
        print(i,":",i*i,end=",")
        i+=1
function_num(20)