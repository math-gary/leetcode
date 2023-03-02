x  = 12321222
a = list(str(x))
b = 0
print(a)
for i in range(int(len(a)/2)):
    if a[i] != a[-i-1]:
        print(f"{x}不是回文數")
        break
    else:
        b += 1
if b == int(len(a)/2):
    print(f"{x}為回文數")

##另解

c = str(x)
print(c[::-1]) ##直接倒過來
    
