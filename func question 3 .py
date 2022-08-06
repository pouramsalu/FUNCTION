# Write a function named add_numbers_list which takes 2 lists of two integers and then prints the sum of the integers with the same position.
# add two list in the same position

def add_number_list(a,b):
    i=0
    while i<len(a,b):
        sum=a[i]+ b[i]
        print(sum)
        i+=1
add_number_list([50,60,10]),([10,20,13])