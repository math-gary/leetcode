'''
此速度超級慢
將字串用index來排，並把他按順序輸出，如以下：0,6,12,1,5,7,11,13,2,4,8,10,3,9
0    6      12
1  5 7   11 13
2 4  8 10
3    9
'''
numRows = 3
s = "PAYPALISHIRING"

mod = 2*numRows -2
m = []
n = []
s_new = []
s_new2 = ""


if numRows == 1:
    print(s)
else:
    for i in range(len(s)):
        n.append(abs((i %mod) - int(mod/2)))
    #print(n) ##n是整理足碼
    while mod and mod >=-1:
        while mod-1 in n:
            #print(mod-1)
            a = n.index(mod-1)
            n[n.index(mod-1)] = mod
            m.append(a)
        mod = mod - 1
    #print(m) ##m則是根據n把index印出來
    for j in m:
        s_new.append(s[j])
    s_new2 = "".join(s_new)

print(s_new2)