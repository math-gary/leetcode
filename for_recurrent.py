## 1加到5用for loop
a = 0
for i in range(1,6):
    a+=i
print(a)


## a加到b，公差為1，用recurrent
def sum(start, end):
    if start == end: 
        return start
    else:
        return sum(start, end - 1) + end
print(sum(4,10))