# SUM OF DIGIT

def sumofdigit(number):
    sum=0
    modulus=0
    while number!=0:
        modulus=number%10
        sum=sum+modulus
        number/=10
        return sum
print(sumofdigit(123))