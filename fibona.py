def fibo(n):
    if not isinstance(n, int):
        return None
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


for i in range(0, 5):
    print(fibo(i))
