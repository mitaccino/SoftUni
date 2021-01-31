budget = float(input())
flour = float(input())
price = flour + flour * 0.75 + flour * 1.25 / 4
eggs = 0
count = 0
while budget >= price:
    eggs += 3
    count += 1
    if count % 3 == 0:
        eggs -= count - 2
    budget -= price
print(f'You made {count} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.')