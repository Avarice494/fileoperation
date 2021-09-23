import queue
"""
对txt文件的读写操作
1.按行读取txt文件，将每行的数据加入到队列中
"""
class FileOperation():
    def __init__(self,name="mode.txt",method = "r"):
        self.type = "txt"
        self.name = name
        self.method = method
        self.line = queue.Queue(100)
    def txt_read(self):
        file = open(self.name, self.method)
        while file.readline():
            fl = file.readline()
            self.line.put(fl)
if __name__ == '__main__':
    FileOperation().txt_read()
