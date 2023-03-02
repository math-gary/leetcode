#Input: dividend = 10, divisor = 3
#Output: 3
#explanation: 10/3 = 3.33333.. which is truncated to 3. 
##取高斯ceiling function符號的code

dividend = 1
divisor = -1

a = dividend // divisor
b = dividend / divisor

if a >=0:
    print(a)
else:
    if b - a != 0:
        print(a)
    else:
        print(int(b))


