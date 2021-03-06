from socket import *
from wave_helper import *
from web_helper import *
from time import ctime

# Globals are evil
# Internet globals
HOST = '192.168.0.105'
PORT = 1235
BUF_SIZ = 2**11
ADDR = (HOST, PORT)
DISP_INT = 1000
EOL = b'EOL'

def main(path):
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(2)

    flag = True

    while flag:
        print('Waiting for connection...')
        (tcpCliSock, addr) = tcpSerSock.accept()
        (IP, port) = addr
        print('...Connected from: %s:%d'%(IP, port))
        print(ctime())
        data = recv_data(tcpCliSock, EOL, BUF_SIZ, DISP_INT)
        print(ctime())
        flag = False
    #save packed data to a .wav file
    if (data):
        write_sound(path, data)
    else:
        print('Failed to receive data')
    #close socket tcpSerSockection
    tcpSerSock.close()

if __name__ == '__main__':
    main('out.wav')