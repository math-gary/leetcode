##這code和bst_test.py一模一樣，為什麼跑不動...
class Node:
    def __init__(self, value = None): ##一個Node可以儲存數字
        self.value = value
        self.left_child = None ##smaller
        self.right_child = None ##greater

class binary_searsh_tree:
    def __init__(self):
        self.root = None ##一開始二搜樹內是沒有資料的所以將 instructor 初始化為 self.root = None

    def insert(self, value):
        if self.root == None: ##判斷root是否為空
            self.root = Node(value)
        else:
            self._insert(value, self.root)
            
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child.value = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child.value = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("this value has existed")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node!= None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

def fill_tree(tree, num_elems = 10, max_int = 50):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_searsh_tree()
tree = fill_tree(tree)

tree.print_tree()

