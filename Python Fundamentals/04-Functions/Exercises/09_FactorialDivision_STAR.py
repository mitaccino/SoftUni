def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fact_division(fac, division):
    res= factorial(fac) / factorial(division)
    return res


num = int(input())
div = int(input())

result = fact_division(num, div)
print(f'{result:.2f}')


