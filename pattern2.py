"""
Program to print pattern as per user enter no of row of pattern

first pattern
*
**
***
****
*****

second pattern
*****
****
***
**
*

third pattern
     *
    **
   ***
  ****
 *****
******
"""


def patterns(rows):
    print("\nFirst pattern")
    for i in range(1, rows + 1):
        a = '*' * i
        print(a)

    print("\nSecond pattern")
    for i in range(rows, 0, -1):
        b = '*' * i
        print(b)

    print("\nThird pattern")
    n = 5
    for i in range(rows):
        for j in range(0, n):
            print(end=' ')
        n = n - 1
        for j in range(i + 1):
            print(end="*")
        print('\r')


row = int(input("Enter no of rows of pattern : "))
patterns(row)
