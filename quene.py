##設計一個list是先進先出的資料結構

class queue():
    def __init__(self):
        self.queue = [] ##使用串列來模擬
    def enqueue(self, data): ##插入資料
        self.queue.insert(0, data)
        print("此序列為：",self.queue)
    def dequeue(self):
        if len(self.queue):
            a = self.queue.pop()
            print(f"從序列拿出{a}，目前序列為{self.queue}")
        else:
            print("此序列為空")
    def length(self):
        print(f"此序列長度為：{len(self.queue)}")

    def all_data_output(self): ##把全部的資料都輸出但不要改變原序列
        ori = self.queue
        for i in ori:
            print(i)
        print(self.queue)


a = queue()
a.dequeue()
a.enqueue(3)
a.enqueue(2)
a.enqueue(1)
a.dequeue()
a.length()
a.all_data_output()