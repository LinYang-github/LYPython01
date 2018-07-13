# 使用了select的简单服务器

import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
while True:
    # select函数需要3个序列作为它的必选参数
    # 还有一个可选的以秒为单位的超时时间作为第4个参数
    # 这些序列是文件描述符整数（或者是带有返回这样整数的fileno方法的对象）
    # 这些就是我们等待的连接
    # 3个序列用于输入、输出以及异常情况
    # 如果没有给定超时时间，select会阻塞，直到其中的一个文件描述符已经为行动做好了准备
    # 如果给定了超时时间，select最多阻塞给定的超时时间
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print 'Got connect from', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data

