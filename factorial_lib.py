def facto(f):
    temp = 1
    #using for loop
    for i in range(1,f+1):
        temp = temp * i
    return temp


    #using while loop
    counter = f
    while counter > 0:
        temp = temp * counter
        counter = counter - 1
    return temp
