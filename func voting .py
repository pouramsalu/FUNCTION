# # Create a funciton named eligibleforvote which tell the user if he/she is eligible to vote or not.( Consider minimum age of voting to be 18. )
def eligibleforvote(age):
    if age>=18:
        print("you are eligible")
    else:
        print("you are not eligible")
eligibleforvote(21)
eligibleforvote(3)
eligibleforvote(40)