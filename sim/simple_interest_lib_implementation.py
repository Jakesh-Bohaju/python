from simple_interest_lib import *


print("Simple Interest Calculator\n")
keys = int(input("Choose option\n1. Simple Interest\n2. Rate\n3. Time\n4. Principal\n5. Amount\n"))
if keys == 1:
    p = float(input("Enter Principal or investment amount : "))
    t = float(input("Enter Time in year : "))
    r = float(input("Enter Interest Rate : "))
    interest(p,t,r)
elif keys == 2:
    p = float(input("Enter Principal or investment amount : "))
    t = float(input("Enter Time in year : "))
    i = float(input("Enter Simple Interest : "))
    rate(p,t,i)
elif keys == 3:
    p = float(input("Enter Principal or investment amount : "))
    r = float(input("Enter Interest Rate : "))
    i = float(input("Enter Simple Interest : "))
    time(p,r,i)
elif keys == 4:
    i = float(input("Enter Simple Interest : "))
    t = float(input("Enter Time in year : "))
    r = float(input("Enter Interest Rate : "))
    principal(i,r,t)
elif keys == 5:
    yn = input("Is principal and Simple Interest given? If yes enter 'y' otherwise enter 'n' : ")
    if yn == 'Y' or yn == 'y':
        p = float(input("Enter Principal or investment amount : "))
        i = float(input("Enter Simple Interest : "))
        amount(p,i)
    elif yn == 'N' or yn == 'n':
        p = float(input("Enter Principal or investment amount : "))
        t = float(input("Enter Time in year : "))
        r = float(input("Enter Interest Rate : "))
        interest(p, t, r)
    else:
        print("Enter y or n.")
else:
    print("Enter correct option")

