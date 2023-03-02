def fibonacci(i):
    if i == 0: return 0
    elif i == 1: return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2) ##要和def相同變數ˊ

n = eval(input("輸入費氏數列第幾項："))
for i in range(n+1):
    print("n = {}, fib({}) = {}".format(i,i,fibonacci(i))) ##注意一下變數操控的細節