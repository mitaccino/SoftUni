numbers_as_string = input().split(", ")
beggars = int(input())
numbers = [int(s) for s in numbers_as_string]
start = 0
sum_beggars = []
for beggar in range(beggars):
    curr_sum = 0
    for s in range(start, len(numbers), beggars):
        curr_sum += numbers[s]
    sum_beggars.append(curr_sum)
    start += 1

print(sum_beggars)
