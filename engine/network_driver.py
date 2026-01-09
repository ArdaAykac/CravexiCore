import socket
import requests




"""cls =class demek"""

class network:
    @classmethod
    def create_server(cls,server_ip,port,max_player=None,debug=True):
        if max_player is None:
            max_player = 4

        if not 1 <= max_player <5:
             raise ValueError("max_player 1 ile 4 arasında olmalı")
        
        if debug is None or debug==False:
            print("Debug:","Debug is False")
        elif debug ==True:
            print("Debug:","Debug is True")
            print("Server İp:",server_ip)
            print("Max Player:",max_player)
        else:
            return "Error" and None
        

        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((server_ip,port))
        print("Waiting Players")
        server.listen()
        client,addr = server.accept()
        print("Connection request from"+str(addr))