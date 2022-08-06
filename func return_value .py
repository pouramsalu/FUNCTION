# We used some functions which returned some values, that is, returned some data.we've written functions that don't return anything.

# def add(number_x,number_y):
#     sum=number_x+number_y
#     return sum
# sum1=add(20,40)
# print(sum1)
# sum2=add(560,23)
# a=1234
# b=12
# sum3=(a,b)
# print(sum2)
# print(3)
# number_a=(add(20,40)/add(5,1)) 
# print(number_a)


# def add_numbers_print(number_x, number_y):
#     number_sum=number_x+number_y
#     print(number_sum)
# sum4 = add_numbers_print(4, 5)
# print(sum4)
# print(type(sum4))



def menu(day):
    if day=="monday":
        return "Butter chicken"
    elif day=="tuesday":
        return "mutton chaap"
    else:
        return "chole bhature"
    print("will i be able to print?:-(")
mon_menu=menu("monday")
print(mon_menu)
tues_menu=menu("tuesday")
print(tues_menu)
fri_menu=menu("friday")
print(fri_menu)