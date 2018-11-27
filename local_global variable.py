hello = 10    ##global varuable


def even_or_odd(number):
    print(hello)   ## can print global variable but cant use operation like "hello = hello + 1"
    global hello  ## global keyword should use for operation

    hello = hello + 1
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')


even_or_odd(7)
even_or_odd(8)





####global can use in these case, here total function call count is done
even_or_old_call_count = 0


def even_or_odd(number):
    global even_or_old_call_count
    even_or_old_call_count += 1

    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')


even_or_odd(7)
even_or_odd(8)
even_or_odd(6)

print('Even or odd call count', even_or_old_call_count)