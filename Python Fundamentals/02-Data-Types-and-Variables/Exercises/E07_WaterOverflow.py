CAPACITY = 255
n = int(input())
curr_capacity = 0
for _ in range(n):
    curr = int(input())

    if curr_capacity + curr > CAPACITY:
        print("Insufficient capacity!")
    else:
        curr_capacity += curr
print(curr_capacity)