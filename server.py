import socket
from threading import Thread

SERVER = None
PORT = 5000
IP_ADDRESS = '127.0.0.1'



CLIENTS = {}





def accept_connections():
    global CLIENTS, SERVER

    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        print(player_name)
        if(len(CLIENTS.keys()) == 0):
            CLIENTS[player_name] = {'player_type': 'player1'}
        else:
            CLIENTS[player_name] = {'player_type': 'player2'}

        CLIENTS[player_name]['player_socket'] = player_socket
        CLIENTS[player_name]['address'] = addr
        CLIENTS[player_name]['player_name'] = player_name
        CLIENTS[player_name]['turn'] = False

        print(f'{player_name} connected to the server from {addr}')


def setup():
    print("\t\t\t\t\t\t**** Welcome to Tombola Game ****")
    global SERVER, PORT, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)
    print("\t\t\t\tServer is waiting for connections...")
    accept_connections()
    

setup()