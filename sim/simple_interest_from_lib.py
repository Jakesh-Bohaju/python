from simple_interest_lib import *


print("Simple Interest Calculator\n")
keys = int(input("Choose option\n1. Simple Interest\n2. Rate\n3. Time\n4. Principal\n5. Amount\n"))
if keys == 1:
    p = float(input("Enter Principal or investment amount : "))
    t = float(input("Enter Time in year : "))
    r = float(input("Enter Interest Rate : "))
    i = interest(p,t,r)
    print("Simple interest : ", i)
elif keys == 2:
    p = float(input("Enter Principal or investment amount : "))
    t = float(input("Enter Time in year : "))
    i = float(input("Enter Simple Interest : "))
    r = rate(p,t,i)
    print("Rate = ", r)
elif keys == 3:
    p = float(input("Enter Principal or investment amount : "))
    r = float(input("Enter Interest Rate : "))
    i = float(input("Enter Simple Interest : "))
    t = time(p,r,i)
    print("Time = ", t)
elif keys == 4:
    i = float(input("Enter Simple Interest : "))
    t = float(input("Enter Time in year : "))
    r = float(input("Enter Interest Rate : "))
    p = principal(i,r,t)
    print("Principal = ", p)
elif keys == 5:
    yn = input("Is principal and Simple Interest given? If yes enter 'y' otherwise enter 'n' : ")
    if yn == 'Y' or yn == 'y':
        p = float(input("Enter Principal or investment amount : "))
        i = float(input("Enter Simple Interest : "))
        a = amount(p,i)
        print("Amount = ", a)
    elif yn == 'N' or yn == 'n':
        p = float(input("Enter Principal or investment amount : "))
        t = float(input("Enter Time in year : "))
        r = float(input("Enter Interest Rate : "))
        i = interest(p, t, r)
        a = p + i
        print("Amount = ", a)
    else:
        print("Enter y or n.")
else:
    print("Enter correct option")

