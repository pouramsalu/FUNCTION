# write a function call show number that takes a parameter calles limit.
# it should print all the number between 0 to limit with a label to identify the even and odd numbers.

def show_numbers(limit):
    i=1
    while i<=limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
limit=int(input("enter the number"))
show_numbers(limit)