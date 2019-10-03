def sum(m, n):
    if n < 0:
        for i in range(abs(n)):
            m -= 1
    else:
        for i in range(0, n):
            m += 1
    return m


def subtract(m, n):
    return sum(m, -n)


def divide(m, n):
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    nAbs = abs(n)
    mAbs = abs(m)
    if n != 0:
        while (mAbs >= nAbs):
            mAbs -= nAbs
            result += 1
        if negativeResult:
            result = -result
    else:
        raise ZeroDivisionError()
    return result


def multiply(m, n):
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    for i in range(abs(n)):
        result += abs(m)
    if negativeResult:
        result = -result
    return result


def MCD(m, n):
    while n != 0:
        m, n = n, m % n
    return m
