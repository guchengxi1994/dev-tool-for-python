import socket
import threading
import time
from utils import __end_mark__


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    resp = ""
    while True:
        data = sock.recv(1024)
        # time.sleep(1)
        resp += data.decode('utf-8')
        if not data :
            break
        if __end_mark__ in data.decode('utf-8') :
            sock.send(('Hello, %s!' % resp).encode('utf-8'))
            resp = ""
    sock.close()
    print('Connection from %s:%s closed.' % addr)




def initial():
    #建立一个socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #监听9999端口
    s.bind(('127.0.0.1', 3334))
    #紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接: 返回的sock用来通信，addr是客户机的地址
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()