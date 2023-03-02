def create_btree(tree, data):
    for i in range(len(data)):
        level = 0
        if i == 0:
            tree[level] = data[i]
        else:
            while tree[level]:
                if data[i] > tree[level]:
                    level = 2*level +2 ##右子樹的level計算（用list存取）
                else:
                    level = 2*level +1 ##左子樹的level計算（用list存取）
        tree[level] = data[i] ##把data[i]存在tree[level]裡

btree = [0]*16 ##開啟一個btree_list，並利用上述的def將data存進此list裡 
data = [10,21,5,9,13,28] 
create_btree(btree, data)

for i in range(len(btree)):
    print(f"二元樹陣列btree[{i}] = {btree[i]}")
            