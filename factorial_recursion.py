# note update program is as incremental development
# leak of faith is checking some sample and conclude all is correct

def factorial(n):
    if not isinstance(n, int):  # type checking, it check whether the n is int or other data type
        return None
    if n == 1:  # brak condition
        return 1
    return factorial(n - 1) * n


# print(factorial('4.5'))

# print(factorial(4.5))

print(factorial(5))
