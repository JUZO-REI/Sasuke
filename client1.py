import socket

client1=socket.create_connection(("127.0.0.1",5050))
while True:
    msg=input("请输入，以回车结尾：")
    if not msg:
        break
    client1.sendall(msg.encode("utf-8"))
    respond=client1.recv(1024)
    print(respond.decode("utf-8"))
client1.close()


