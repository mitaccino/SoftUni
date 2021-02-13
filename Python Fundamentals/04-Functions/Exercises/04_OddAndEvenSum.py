def odd_even_sum(string):
    odd = [int(d) for d in string if not int(d) % 2 == 0]
    even = [int(d) for d in string if int(d) % 2 == 0]
    return [sum(odd), sum(even)]


res = odd_even_sum(input())

print(f'Odd sum = {res[0]}, Even sum = {res[-1]}')
