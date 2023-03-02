nums = [-1,0, 1,2, 0, -1, -4]

posi = []
zeros = []
nega = []

for i in nums:
    if i  > 0:
        posi.append(i)
    elif i < 0:
        nega.append(i)
    else:
        zeros.append(i)

print(posi)
print(zeros)
print(nega)