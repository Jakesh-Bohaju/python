number = int(input('Enter number'))

counter = 1

while counter < number:
    if counter % 2 == 0:
        print(counter)

    counter = counter + 1  # counter += 1
