"""
Write a program that will receive an input string of only 1s and 0s. Return 'yes' if all the counts of all consecutive 0s
is even and count of all consecutive 1s is odd. Otherwise return 'no',

Example
Sample Input 1:
0010000111

Sample Output 1:
yes

Sample Input 2:
0100111

Sample Output 2:
no
"""

import time

# Method 1
input_string = input("Enter 0s and 1s only...\n")
start_time = time.time()
count0s = 0
count1s = 0
l0 = []
l1 = []
flag0 = 0
flag1 = 0
try:
    if input_string.isnumeric() and int(input_string, 2):
        for i in input_string:
            if int(i) == 0:
                count0s += 1
            else:
                l0.append(count0s)
                count0s = 0
        for i in input_string:
            if int(i) == 1:
                count1s += 1
            else:
                l1.append(count1s)
                count1s = 0
        l0.append(count0s)
        l1.append(count1s)
        for j in l0:
            if j > 0 and j % 2 != 0:
                flag0 = 1
                break
        for k in l1:
            if k > 0 and k % 2 == 0:
                flag1 = 1
                break
        if flag0 == 0 and flag1 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print("Wrong input. Try again")
except:
    print("Wrong input. Try again")
print("Time taken : ", time.time() - start_time)
