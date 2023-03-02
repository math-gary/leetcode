class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data): ##建立二元樹
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def inorder(self): ##中序列印（自然會由小到大排列、左->根->右）
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self): ##前序列印（根->左->右）
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self): ##後序列印（左->右->根）
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def search(self, val): ##找到特定的val
        if val < self.data:
            if not self.left:
                return str(val)+"不存在"
            return self.left.search(val)
        elif val > self.data:
            if not self.right:
                return str(val)+"不存在"
            return self.right.search(val)
        else:
            return str(val) +"找到了"
        


tree = Node()
datas = [10, 21, 5, 9, 13, 28]
for i in datas:
    tree.insert(i)
print("中序列印")
tree.inorder()
print("前序列印")
tree.preorder()
print("後序列印")
tree.postorder()

n = eval(input("請輸入特定的搜尋資料："))
print(tree.search(n))