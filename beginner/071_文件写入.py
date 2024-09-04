# 文件操作的步骤：打开文件、读写文件、关闭文件
# 1. 打开文件：open()函数：open(file, mode='r',encoding)
# file: 文件的路径，可以是相对路径，也可以是绝对路径
# mode: 打开文件的模式，默认是'r'，只读模式, 'w'写入模式，'a'追加模式
# w: 如果文件不存在，创建文件，如果文件存在，清空文件内容。文件打开后，文件指针在文件的开头
# encoding: 文件的编码格式, 如果文件是二进制文件，不需要指定编码格式

fileObj = open('./a.txt', 'w', encoding='utf-8')
fileObj.write('hello world\n') 
fileObj.close()
# print(fileObj, type(fileObj))