age = int(input())
drink = 'whisky'
if age <= 14:
    drink = 'toddy'
elif 18 >= age > 14:
    drink = 'coke'
elif 21 >= age > 18:
    drink = 'beer'


print(f'drink {drink}')