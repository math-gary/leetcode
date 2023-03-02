strs = ["b", "a"]

for i in range(1, len(strs)):
    n = min(int(len(strs[0])), int(len(strs[i])))
    b = 0
    for j in range(n):
        if strs[0][:j+1] != strs[i][:j+1]:
            strs[0] = strs[0][:j]
        else:
            b+=1
            if b == n:
                strs[0] = strs[0][:b]
print(strs[0])
