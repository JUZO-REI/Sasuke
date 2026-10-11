import socket
server=socket.socket()#不写东西默认TCP
server.bind(("127.0.0.1",5050))
server.listen(5)#等待队列的最大长度，最大允许几个人排队
while True:
    connection, addr = server.accept() #接收客户端 connection获得server接受的socket对象，用于收发数据
    print("client", addr)#addr用于获得地址与端口
    while True:#内层循环可以重复处理一个用户的信息
         data = connection.recv(1024)#接收数据并回显   1024代表最多接受1024个！字节！
         if not data:
              print(f"client:{addr}已断开")
              break
         name= data.decode("utf-8")#输入进来的用de解码，成中文
         reply=f"Hello {name} "
         print(b"server received:"+data)
         connection.sendall(reply.encode("utf-8"))#输出去的用en编码
    connection.close()
    #总结流程：server 负责等客上门->accept()接到客->把客人交给专属客服 connection ->客服跟客人聊天(recv 和sendall) ->聊完挂断(close)。