from socket import *
import os

class TcpConnect(object):
    def __init__(self,port):
        self.port=port
        self.bool=True
    def ConnectClient(self,ip):
        client = socket(AF_INET, SOCK_STREAM)
        print(self.ip)
        client.connect((self.ip,self.port))
        print("to finish your chat say 'exit'")
        def Connect():
            while self.bool:
                data = input("Client: ")
                client.sendall(data.encode())
                if data == "exit":
                    client.close()
                    self.bool=False
                    break
                    print(self.bool)
                data = client.recv(2048).decode()
                print ("the message that Server send: {0}".format(data))
        Connect()
    def getIp(self):
        r = os.popen("ipconfig")
        for line in r.readlines():
            line = str(line)
            if "IPv4 Address" in line:
                t = line.find(":")
                self.ip=line[t + 2:-1]
                return self.ip
port=int((input("you need choose that port in Server to connect ")))
connect1=TcpConnect(port)
myIpconfig=connect1.getIp()
connect1.ConnectClient(myIpconfig)