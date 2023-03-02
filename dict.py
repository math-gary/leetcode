dicts_1 = {
    1:"peter",
    2:"jack"
}

print(dicts_1)

dicts_2 = {
    1:["a", "b"],
    2:["c", "d"], ##可視為單向圖，要雙向的話就還要再補
    "c":2
}

print(dicts_2)
print(dicts_2[2], dicts_2["c"])

sets = {1,2,3}
sets.add(4)

for i in sets:
    print(i)

dict_3 = {}
dict_3[1] = 2
dict_3[4] = 3
dict_3[1] = dict_3[1] +1

if 2 in dict_3:
    print(True)
else:
    print(False)

for i in dict_3:
    print(i)

print(dict_3)