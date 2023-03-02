## 看別人的解答，但其實跟我差不多，只不過他去看頭尾一致。
## 我來說一下，我的做法是建一個def去檢測是不是回文數，所以是去收集s[i:j]做判斷


s = "abbaabcdedcba" ##給一個s:str，要找出s中的substring，他是回文數。

s_max = "" ##收集最長的substring
max = 0 ##最長的substring的長度

for i in range(len(s)): ##針對每一個s都去跑一遍
    ##長度為奇數
    head = i
    tail = i
    while head >= 0 and tail < len(s) and s[head] == s[tail]: 
        ##如果頭尾都一樣的話，就收集起來
        if tail - head +1 > max:
            max = tail - head+1
            s_max = s[head:tail+1]
        head -= 1
        tail += 1

    ## 長度為偶數
    head = i
    tail = i+1
    while head >= 0 and tail < len(s) and s[head] == s[tail]:
        if tail - head +1 > max:
            max = tail - head+1
            s_max = s[head:tail+1]
        head -= 1
        tail += 1

print(s_max)
