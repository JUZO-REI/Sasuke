# client.py
import socket

client = socket.create_connection(("127.0.0.1",5050))#通过socket建立地址让两个文件链接
while True:#同一个用户发多条消息
    msg=input("请输入信息，直到回车结束：")
    if(msg==""):
        print("成功退出！")
        break
    client.sendall(msg.encode("utf-8"))

    response = client.recv(1024)
    print(response.decode("utf-8"))#接收回应解码并打印

client.close()   
#导入函数——建联系——发消息——接受回应并输出——关闭