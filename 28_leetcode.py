##太簡單了 哈啊
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.

haystack = "leetcode"
needle = "letto"

if needle == "":
    print("-1")
else:
    if needle in haystack:
        a = haystack.split(needle)
        print(len(a[0]) + 1)
    else:
        print("-1")


