## 給定s:str，找到在s裡一開始的數字，並輸出出來。

s = "-91283472332"
s = s.strip() ##去掉頭尾空格

sets = set()
r = 0
m = 1 ##判斷正負號

n = ["0"] 
for i in range(10): ##讓sets收集1-9
    sets.add(str(i))

for i in range(len(s)):

    if r>=2:
        print(0)
            
    if s[i] == "-" and i <=1: ##如果有"-"，就令m = -1
        m = -1
        r += 1
    elif s[i] == "+" and i<=1:
        r += 1
            
    elif s[i] in sets: ##n收集數字
        n.append(s[i])
    else:
        break
                
    if i>=1 and (s[i] == "-" or s[i] == "+"):
        break

s = "".join(n)

ans = m*int(s)

if ans < -2**31:
    ans = - (2**31)
if ans > 2**31 - 1:
    ans = 2**31 - 1

print(ans)
