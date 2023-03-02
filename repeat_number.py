def repeat(lists):
    a = {} ##給一個dict
    b = set() ##給一個set
    for i in range(len(lists)):
        if lists[i] not in a: ##如果list的值不在dict裡，把它存進dict
            a[lists[i]] = i
        else:
            b.add(lists[i]) ##如果在字典裡，就存進set
    print(b)

listss =  [1,1,1,2,2,23,4,5,65,23,65]
repeat(listss)
    
        