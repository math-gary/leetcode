class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        self.inorder(root, res)
        return res
        
    def inorder(self, root: TreeNode, res: list[int]) -> None:
        if not root:  # path1
            print("path 1:", "root is null")
            return
        print("INIT: ", root.val, res)
        self.inorder(root.left, res)
        print("path 2:", res)
        res.append(root.val)
        print("path 3:", res)
        self.inorder(root.right, res)
        print("path 4:", res)





# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.right= a2
a2.left= a3

a = Solution() # new instance
a.inorderTraversal(a1)
