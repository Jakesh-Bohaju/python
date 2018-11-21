def interest(p, t, r):
    siinterest = p * t * r / 100
    print("Simple interest = ", siinterest)


def rate(p, t, i):
    sirate = (100 * i) / (p * t)
    print("Rate = ", sirate)


def time(p, r, i):
    sitime = (100 * i) / (p * r)
    print("Time = ", sitime)


def principal(i, r, t):
    siprincipal = (100 * i) / (r * t)
    print("Principal = ", siprincipal)


def amount(p, i):
    siamount = p + i
    print("Amount = ", siamount)
