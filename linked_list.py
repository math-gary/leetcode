class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list(): ##建立linked_list
    def __init__(self):
        self.head = None ##第一個node
    def print_link(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def begining(self, newdata): ##在第一個節點插入心節點
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def ending(self, newdata): ##增加最後一個節點
        new_node = Node(newdata)
        if self.head == None: ##如果沒有head那就把head設成new_node
            self.head = new_node
        #return
        last_ptr = self.head
        while last_ptr.next: ##跑完last_ptr
            last_ptr = last_ptr.next
        last_ptr.next = new_node ##將最後一個節點指向new_node

    def between(self, pre_node, newdata): ##插入中間節點
        if pre_node == None:
            print("沒有前一個節點")
        
        new_node = Node(newdata)
        new_node.next = pre_node.next ##先把原本的pre_node.next接在new_node.next
        pre_node.next = new_node 

link = linked_list() ##給一個linked list叫做link

link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3

link.print_link()

print("新的串列")

link.begining(100)
link.print_link()

print("新的串列")

link.ending(101)
link.print_link()

print("插入中間串列")
link.between(n2, 102)
link.print_link()