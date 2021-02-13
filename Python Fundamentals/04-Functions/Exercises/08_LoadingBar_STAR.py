def loading(percent):
    array = ['%' if a <= percent // 10 else '.' for a in range(1, 11)]
    print(f"[{''.join(array)}]")


number = int(input())

if number < 100:
    print(f'{number}%', end=' ')
    loading(number)
    print('Still loading...')
elif number == 100:
    print(f'{number}% Complete!')
    loading(number)

