##給一個字串要找出最長子字串並且這個子字串是不重複的

s = "qwertyuioubwiebpvbqvowsubdjcnqjnlqjenjncjk;lmdnfeneccjnveqifnlindlkl;j"

a = [] ##把str(s)一個一個記錄下來
n = 0 ##紀錄a的長度
max = 1 ##紀錄最長的子字串

for i in range(len(s)):
    if s[i] not in a: ##如果沒有s[i]就加到a裡
        a.append(s[i])
        n += 1 ##計算a的長度
    else:
        if len(a) > max: ##把a的最大長度給記錄下來
            max = len(a)
        
        a = a[a.index(s[i])+1:] ##如果說重複了，就把原本a裡的s[i]拿掉，並從下一個開始計算
        a.append(s[i]) ##再把s[i]加到a裡面
        n = len(a) ##因為a已經更新了，所以n也要隨之更新
if n > max:
    max = n

print(max)
