text = input().lower()
counter = 0
sample = ['sand', 'water', 'fish', 'sun']

for i in sample:
    if i in text:
        word_count = text.count(i)
        counter += word_count


print(counter)
