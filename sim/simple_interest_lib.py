#note: if not exist return in function then it is call void function,
# if function is with return then it is call fruitfull function


def interest(p, t, r):
    siinterest = p * t * r / 100
    return siinterest


def rate(p, t, i):
    sirate = (100 * i) / (p * t)
    return sirate


def time(p, r, i):
    sitime = (100 * i) / (p * r)
    return sitime


def principal(i, r, t):
    siprincipal = (100 * i) / (r * t)
    return siprincipal


def amount(p, i):
    siamount = p + i
    return siamount
