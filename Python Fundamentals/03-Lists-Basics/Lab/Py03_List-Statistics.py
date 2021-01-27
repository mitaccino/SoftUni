# 03. Lab: Lists Basics
# ----------------------
# 03. List Statistics

n = int(input())
positives = []
negatives = []

for n in range(n):
    curr_num = int(input())
    if curr_num >= 0:
        positives.append(curr_num)
    else:
        negatives.append(curr_num)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')