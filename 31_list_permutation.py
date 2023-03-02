##在數學上，給定一個排序，要去找到下一個合理的順序
##例如：[1,2,3,4]的下一個就是[1,2,4,3]，以此類推

nums = [3,2,1,2]

def next_permutation(nums:list): ##只顯示下一個permutation的list

    a = 0

    for i in range(1,len(nums)):
        if nums[-i] > nums[-i-1]:
            a = i ##紀錄最後一個peak
            break

    if a==0: ##如果已經完全逆序，就直接由小排到大
        nums.sort()
        return nums
    else:
        nums_1 = nums[:len(nums)-a-1] ##由peak分成兩個list
        nums_2 = nums[len(nums)-a-1:]

        b = nums_2[0] ##將peak前的那一個元素作紀錄

        nums_2.sort()

        b_i = nums_2.index(b)
        for j in range(b_i+1, len(nums_2)):
            if nums_2[j] > b:
                b_new = nums_2[j] ##找到在nums_2中比b大但比其他小的值，將其令為b_new
                nums_2.remove(b_new) ##接著把b_new拿掉
                break

        nums_1.append(b_new) 
        return nums_1+nums_2 ##此即為解答

def factorial(n:int): ##階乘函數（遞迴）
    if n>0:
        return factorial(n-1)*n
    else:
        return 1

def total_per(nums): ##列出全部的permutation並告訴我有幾種(重複的也可以)
    n = set()
    for i in range(factorial(len(nums))):
            n.add(tuple(nums))
            nums = next_permutation(nums)
        
    print(n)
    print(f"總共有{len(n)}個。")

total_per(nums)


