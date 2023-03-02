#Input: n = 4
#Output: "1211"
#Explanation:
#countAndSay(1) = "1"
#countAndSay(2) = say "1" = one 1 = "11"
#countAndSay(3) = say "11" = two 1's = "21"
#countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

def next_cas(strs):
    a = strs[0] ## 先將strs的第一個字母存下來
    m = 1 ##紀錄每一個字幕出現的次數
    ans = [] ##將m以及a按造順序存下來
    ans2 = "" 
    for i in range(1, len(strs)):
        if strs[i] == a:
            m+=1
        else:
            ans.append(str(m))
            ans.append(a)
            a = strs[i]
            m = 1 ##存下來之後要回歸m值
    ans.append(str(m)) ##要將最後的數值存下來
    ans.append(a)
    ans2 = "".join(ans) ##把ans合成一個str
    
    return ans2 ##輸出ans2

n = 4
strs = "1"

for i in range(n-1):
    strs = next_cas(strs) ##迭代
print(strs)
