class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    def print_list(self): ##print list的val
        ptr = self.head
        n = 0
        while ptr:
            n +=1
            print(ptr.data)
            ptr = ptr.next
            if n > 10:
                break
    
    def length(self): ##list 的長度為何（前提是不循環）
        n = 0
        ptr = self.head
        while ptr:
            n += 1
            ptr = ptr.next
        print("the length of linked list is " ,n)
        print(f"the length of linked list is {n}") ##print的方法

    def search_times(self, val): ##找到list中val的次數
        n = 0
        ptr = self.head
        while ptr:
            if ptr.data == val:
                n += 1
            ptr = ptr.next
        print(f"the number {val} appears {n} times.")

    def times_datas(self): ## print出全部data的次數
        sets = set() ##建立set的方法
        ptr = self.head
        while ptr:
            sets.add(ptr.data)
            ptr = ptr.next
        for i in sets:
            self.search_times(i)
        print(sets)

    def linked_list_cycling(self): ##測試有無循環
        ptr = self.head
        ptr2 = self.head
        while ptr and ptr2 and ptr2.next:
            ptr = ptr.next
            ptr2 = ptr2.next.next
            if ptr == ptr2:
                print("此linked list為循環list")
                sys.exit()
        print("此linked list為不循環list")
            
import sys

list = linked_list()
list.head = Node(10)
n2 = Node(10)
n3 = Node(3)
n4 = Node(10)

list.head.next = n2
n2.next = n3
n3.next = n4
#n4.next = n2

list.print_list()
#list.length()
#list.search_times(10)
#list.times_datas()
list.linked_list_cycling()


