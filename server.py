from socket import *
import os
from flask import Flask
class Server(object):
    def __init__(self,port):
        self.port=port
        self.bool= True;
    def ServerConnect(self,ip):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)
        print ("Server started")
        print("to finish your chat say 'exit'")
        client, addr = server.accept()
        def Connect():
            while True:
                data = client.recv(2048).decode()
                print("the message that Client send: {0}".format(data))
                if data == "exit":
                    client.close()
                    server.close()
                    break
                data = input("Server: ")
                client.sendall(data.encode())
        Connect()
    def getIp(self):
        r = os.popen("ipconfig")
        for line in r.readlines():
            line = str(line)
            if "IPv4 Address" in line:
                start = line.find(":")
                self.ip=line[start + 2:-1]
                return self.ip
    def getIptoWeb(self):
        app = Flask("getIptoWeb", static_url_path='')
        @app.route('/GivemyIp')
        def giveMyiptoWeb():
            return 'Hello that your ip address {0} you can shared now'.format(self.ip)
        debug = True
        app.run(host='0.0.0.0', port=self.port, debug=debug)
        giveMyiptoWeb(self.ip)


connect=Server(port)
myIp=connect.getIp() #get ip addres
#connect.ServerConnect(myIp) #to chat betteen client and server.


#connect.getIptoWeb() #to return look addres in webjjjff