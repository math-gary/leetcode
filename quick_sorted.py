import random

def quick_sorted(nLst): ##時間複雜度O(n^2)~O(nlog(n))，要看選到什麼基準點pivot
    ## 快速排序法

    if len(nLst) <= 1:
        return nLst

    left  = []
    right = []
    piv = []
    pivot = random.choice(nLst) ##從nLst中選一個當作中間點

    for i in nLst:
        if i == pivot:
            piv.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sorted(left) + piv + quick_sorted(right)

data = [6,1,5,7,3,9,4,2,8]
print("原始排列：", data)
print("快速排序法：", quick_sorted(data))