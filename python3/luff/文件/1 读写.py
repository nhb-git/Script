# 写入文件内容
# with open('test.txt', 'w', encoding='utf-8') as f:
    # f.write("line00\n")
    # f.write("line02\n")

# 读取文件内容
# with open('test.txt', 'r') as f:
    # data = f.read()
    # f.seek(2)   # 单位是字节
    # print(f.tell())
    # data = f.readline()
    # data = f.readlines()
# print(data)

# 追加文件内容
# f = open('test.txt', 'a')
# f.write('append\n')
# f.close()


# 读写+
# f = open('test-rename1.txt', 'a+')
# f.write('test,r+\n')
# print(f.readline())
# print(f.readline())
# f.close()
f = open('test-rename1.txt', 'wb')
f.write('niu'.encode('utf-8'))
f.close()

