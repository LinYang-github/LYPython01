# ÿ���������յ�һ���������Կͻ��˵����ӣ�ʱ
# �ͻ�ʵ����һ����������򣬲������ĸ��ִ��������ڴ�������ʱ������

from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connect from', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()
