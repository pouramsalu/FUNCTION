# Take take user input,one for no of studentsn and another for expense per students .if total expense is 50000 or less,print within budget,else print over budget.
def student_expense(students,expense):
    total_expense=students*expense
    if total_expense>=50000:
        print(total_expense,"is over budget")
    else:
        print(total_expense,"is within budget")
student=int(input("enter number of students"))
expense=int(input("enter expense per student"))
student_expense(student,expense)