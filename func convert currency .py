def usd_to_rupees(rupees):
    rs=rupees*75
    return rs
def rupees_to_usd(dollar):
    usd=dollar*0.014
    return usd
def main(choice):
    print(choice)
    user=int(input("enter choice:"))
    if user==1:
        dollar=int(input("enter amount in dollars:"))
        print(dollar,"$ in Rs.:",usd_to_rupees(dollar),"rupees")
    elif user==2:
        rupees=int(input("enter amount in rs:"))
        print(rupees,"Rs. in $:",rupees_to_usd(rupees),"dollars")
choice=["1.USD to Rs","2.Rs to USD"]
main(choice)