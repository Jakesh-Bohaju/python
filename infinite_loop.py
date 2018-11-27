while True:  # infinite loop, condition never break
    user_input = input("Do you want a transaction? Press Y")
    if user_input == 'y' or user_input == 'Y':
        print('Transaction made successfully')

    if user_input == 'exit':  # if user input exit condtion break
        break
