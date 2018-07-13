# 每当服务器收到一个请求（来自客户端的连接）时
# 就会实例化一个请求处理程序，并且它的各种处理方法会在处理请求时被调用

from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connect from', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()
