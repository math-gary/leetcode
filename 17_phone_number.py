dicts = {2:["a", "b", "c"],
 3:["d","e","f"],
 4:["g",'h',"i"],
 5:["j", "k", "l"],
 6:["m","n", "o"],
 7:["p", "q", "r", "s"],
 8:["t", "u", "v"],
 9:["w", "x", "y", "z"]}

def merge(A:list, B:list):
    A = A*len(B)
    B = B*len(A)
    A.sort()
    return list(map(lambda x:x[0]+x[1], zip(A,B)))
digits = "92"
A = dicts[int(digits[0])]
for i in range(1,len(digits)):
    B = dicts[int(digits[i])]

    A = merge(A, B)

print(len(A), A)