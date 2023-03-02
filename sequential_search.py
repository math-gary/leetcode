def sequential_search(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:
            return i
    return -1

data = [6,1,5,7,3,9,4,2,8]
key = eval(input("請輸入要搜尋的值："))
index = sequential_search(data)
if index != -1:
    print(f"找了{index + 1}次，找到值{data[index]}")
else:
    print(f"此值{key}不在data裡")