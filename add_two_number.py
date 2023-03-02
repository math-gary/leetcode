n = 8124

a = []

print(n//100%10)
print(len(str(n)))

for i in range(len(str(n))):
    a.append(n//(10**i) %10)
print(a)

