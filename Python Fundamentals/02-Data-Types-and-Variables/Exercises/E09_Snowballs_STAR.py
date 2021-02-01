n_snowballs = int(input())
max_value = -1
max_snow = -1
max_time = -1
max_quality = -1

for _ in range(n_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if max_value < snowball_value:
        max_value = snowball_value
        max_time = snowball_time
        max_snow = snowball_snow
        max_quality = snowball_quality

print(f'{max_snow} : {max_time} = {int(max_value)} ({max_quality})')