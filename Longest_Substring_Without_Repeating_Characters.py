##卡住了 再想想看...
##是做完了，但很爛...
##給一個字串要找出最長子字串並且這個子字串是不重複的
##好的結果在leetcode3
a = "abcdefgh"


def repeat(strs:str): ##看str有沒有重複
    if len(list(strs)) == len(set(strs)): ##沒重複就寫true
        return True
    else:
        return False

n = []

if not a:
    n.append(0)

for i in range(len(list(a))):
    for j in range(i+1, len(list(a))+1):
        #print([i,j])
        if not repeat(a[i:j]):
            n.append(len(list(a[i:j-1])))
            #print(a[i:j-1])
            if len(set(a)) in n:
                print(f"最長子字串數為{len(set(a))}")
                break
            break
        if repeat(a[i:len(list(a))]):
            n.append(len(list(a[i:len(list(a))])))
            #print([i,len(list(a))])
            if len(set(a)) in n:
                print(f"最長子字串數為{len(set(a))}")
                
            break
print(max(n))