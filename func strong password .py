def strong_password(password):
    digit="123456789"
    upper="A-Z"
    lower="a-z"
    special="@#$@"
    sum=0
    a=0
    x=0
    y=0
    z=0
    if len(password)> 6 or len(password)<=10:
        i=0
        while i<(len(password)):
            if password[i] in digit:
                a=1
            elif password[i] in upper:
                x=11
            elif password[i] in lower:
                y=21
            elif password[i] in special:
                z=1
            i+=1
        sum=x+y+z+a
        if sum<4:
            print("weak password")
        else:
            print("strong password")
password=input("enter the password")
strong_password(password)