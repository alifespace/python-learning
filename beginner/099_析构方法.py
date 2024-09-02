## __del__方法: 析构方法，当对象被删除时，会自动调用该方法

# 对象销毁的几种情况：
# 1. 程序执行完毕，程序中的所有对象都会被销毁
# 2. 使用del删除一个对象
# 3. 对象不再被引用，即没有变量指向该对象

import time

class WriteLog:
    fileURL = './'
    fileName = str(time.strftime('%Y-%m-%d')) + '.log'

    def __init__(self):
        print(self.fileURL + self.fileName)
        self.objFile = open(self.fileURL + self.fileName, 'a', encoding='utf-8')

    def log(self, msg):
        self.objFile.write(str(time.strftime('%Y-%m-%d %H:%M:%S')) + ' ' + msg + '\n')
        pass

    def __del__(self):
        self.objFile.close()

log1 = WriteLog()
log1.log('hello')