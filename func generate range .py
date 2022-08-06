# Implement a function name generate range(min,max,step),which takes three arguments 
# and generate a range of integers from mim to max,with the step.The first integers
# is the minimum value,yhe second is the maximum of the range and the third is the 
# step(min<max)

def generate_range(min,max,step):
    list=[]
    if min<max:
        for i in range(min,max+1,step):
            list.append(i)
        print(list)
    else:
        print("min is greater than max")
min=int(input("enter the number"))
max=int(input("enter te number"))
step=int(input("enter the number"))
generate_range(min,max,step)