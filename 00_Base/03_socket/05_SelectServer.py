# ʹ����select�ļ򵥷�����

import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
while True:
    # select������Ҫ3��������Ϊ���ı�ѡ����
    # ����һ����ѡ������Ϊ��λ�ĳ�ʱʱ����Ϊ��4������
    # ��Щ�������ļ������������������Ǵ��з�������������fileno�����Ķ���
    # ��Щ�������ǵȴ�������
    # 3�������������롢����Լ��쳣���
    # ���û�и�����ʱʱ�䣬select��������ֱ�����е�һ���ļ��������Ѿ�Ϊ�ж�������׼��
    # ��������˳�ʱʱ�䣬select������������ĳ�ʱʱ��
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

