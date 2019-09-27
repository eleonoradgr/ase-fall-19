def sum(m, n):
    if n < 0:
        for x in range(abs(n)):
            m -= 1
    else:
        for x in range(0, n):
            m += 1
    return m


def subtract(m, n):
    return sum(m, -n)


def divide(m, n):
    count = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    nabs = abs(n)
    mabs = abs(m)
    if n != 0:
        while (mabs >= nabs):
            mabs -= nabs
            count += 1
        if negativeResult:
            count = -count
    else:
        raise ZeroDivisionError()
    return count


def multiply(m, n):
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    result = 0
    for x in range(abs(n)):
        result += abs(m)
    if negativeResult:
        result = -result
    return result
