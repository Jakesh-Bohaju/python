"""
Write a program that takes a string as an input and prints it after removing all consecutive occurrences of repeated
character that is non vowel.

Example
Sample Input 1:
Hello my fellow peeps

Sample Output 1:
Helo my felow peeps
"""

import time

# Method 1
input_string = input("Enter a string...\n")
start_time = time.time()
new_list = list()
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(len(input_string) - 1):
    if input_string[i].lower() in vowel:
        new_list.append(input_string[i])
    elif input_string[i].lower() != input_string[i + 1].lower():
        new_list.append(input_string[i])
new_list.append(input_string[-1:])
print("Output String (Method 1) : ", ''.join(new_list))
print("Time taken by Method 1 : ", time.time() - start_time)

# Method 2 (from https://www.geeksforgeeks.org/remove-consecutive-vowels-string/)
start_time = time.time()


def is_vow(c):
    return ((c == 'b') or (c == 'c') or
            (c == 'd') or (c == 'f') or
            (c == 'g') or (c == 'h') or
            (c == 'j') or (c == 'k') or
            (c == 'l') or (c == 'm') or
            (c == 'n') or (c == 'p') or
            (c == 'q') or (c == 'r') or
            (c == 'w') or (c == 't') or
            (c == 'v') or (c == 'w') or
            (c == 'x') or (c == 'y') or
            (c == 'z'))


def removeVowels(str):
    print("Output String (Method 2) : ", str[0], end="")
    for i in range(1, len(str)):
        if (is_vow(str[i - 1]) != True) or (is_vow(str[i]) != True):
            print(str[i], end="")


removeVowels(input_string)
print("\nTime taken by Method 2 : ", time.time() - start_time)
