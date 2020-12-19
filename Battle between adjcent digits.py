"""
Starting from the left side of an string that consists only of digit, adjacent digits pair up in 'battle' and the larger
digit wins. If two digits are the same, they both lose. A lone digit automatically wins.

Write a program that takes a string of digits and returns the victorious digits. If all the numbers lose, return 'total carnage'.

Example
Sample Input 1:
578921445

Sample Output 1:
7925

Sample Input 2:
558899

Sample Output 2:
total carnage
"""

import time

# Method 1
input_string = input("Enter a numbers only...\n")
start_time = time.time()
count = 0
output = []
if input_string.isnumeric():
    for i in range(0, len(input_string) - 1, 2):
        if not input_string[i] == input_string[i + 1]:
            if input_string[i] > input_string[i + 1]:
                output.append(input_string[i])
                count += 1
            else:
                output.append(input_string[i + 1])
                count += 1
    if len(input_string) % 2 != 0:
        output.append(input_string[-1:])
    if count > 0:
        print("Output : ", ''.join(output))
    else:
        print('Output : total carnage')
else:
    print("Wrong input. Try again")
print("Time taken : ", time.time() - start_time)
