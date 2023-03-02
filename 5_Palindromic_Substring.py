## Given a string s, return the longest palindromic substring in s.
## 想法是取中間的字往兩邊看，但這只能判斷奇數。失敗想不到（2/20）


s = "abba"

def palindromic(s:str): ##判斷是否為回文數
    if s == s[::-1]: ##是的話就回傳true，不是就回傳false
        return True
    else:
        return False
''' ##這是硬爆，但很爛，跑不動
s_max = ""
max = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if palindromic(s[i:j]):
            if j-i > max:
                max = j-i
                s_max = s[i:j]

print(s_max)
'''


'''
##多行註解的方法，想法是取中間的字往兩邊看，但這只能判斷奇數。
i = 1
s_max = ""
max = 0

while i< len(s)-1: 
    n = min(i, len(s)-i)
    for j in range(1,n+1):
        if palindromic(s[i-j:i+j+1]):
            if 2*j+1>max:
                max = 2*j+1
                s_max = s[i-j:i+j+1]
        else:
            a = j
            break
        a = j
    i = i +a
print(s_max)
'''

