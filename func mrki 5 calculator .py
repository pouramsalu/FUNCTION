# Create a function named Calculator which takes three arguments - number_x, number_y, operation. number_x and number_y we will take two integers and operation parameter defines the type of mathematical operation to be performed on the two integers.
def calculator(number_x,number_y,op):
    if op=="sum":
        result=number_x+number_y
    elif op=="substract":
        result=number_x-number_y
    elif op=="multiply":
        result=number_x*number_y
    elif op=="divide":
        result=number_x%number_y
    return result

number_1=calculator(20,24,"sum")
number_2=calculator(50,60,"substract")
number_3=calculator(80,120,"multiply")
number_4=calculator(90,23,"divide")
print(number_1)
print(number_2)
print(number_3)
print(number_4)