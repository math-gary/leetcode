import numpy as np

list1 = [10,20,30,40]
list2 = [11,12,13,14]

x = 2
y = 2

np1 = np.array(list1)
np2 = np.array(list2)

np2 = np2.reshape([2,2]) ##把array轉換成2*2的矩陣
#print(np2)

np2 = np2.astype("int64") ##把np2轉換成int64的格式（也可以轉成float64）
#print(np2)

np3 = np.zeros([5]) ##建立一個有五個0的一維陣列
#print(np3)

np4 = np.zeros([2,5]) ##建立一個有10個0的二維陣列
#print(np4)

np5 = np.ones([5]) ##建立一個有五個1的一維陣列
#print(np5)

np7 = np.arange(1,10) ##建立一個1到9的一維陣列
#print(np7)

np1 = np.append(np1, [15,16,17,18]) ##在np1後面增加[15,16,17,18]
#print(np1)

np1 = np.delete(np1, [3,5]) ##把np1的第3個和第5個刪掉
#print(np1)

np6 = np.ones([4,5])
#print(np6)

np6 = np.delete(np6, [1,3], axis=0) ##刪除第1和3列
#print(np6)

np6 = np.delete(np6, [0], axis=1) ##刪除第0行
#print(np6)

np6_sum0 = np6.sum(axis=0) ##垂直加總
#print(np6_sum0)

np6_sum1 = np6.sum(axis=1) ##水平加總
#print(np6_sum1)

np8 = np.array([1,3,5,7,9])
np9 = np.array([2,4,6,8,10])

np10 = np8 +np9
#print(np10)

#print(np8 > 3) ##回傳bool值

#print(np8[np8 > 3]) ##回傳np8中大於3的那些值




