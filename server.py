from socket import *
from wave_helper import *
from web_helper import *

# Globals are evil
# Internet globals
HOST = '192.168.0.105'
PORT = 1235
BUF_SIZ = 2048
ADDR = (HOST, PORT)
DISP_INT = 1000
EOL = b'EOL'

def main():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(1)

    flag = True

    while flag:
        print('Waiting for connection...')
        (tcpCliSock, addr) = tcpSerSock.accept()
        (IP, port) = addr
        print('...Connected from: %s:%d'%(IP, port))
        data = recv_data(tcpCliSock, EOL, BUF_SIZ, DISP_INT)
        flag = False
    #save packed data to a .wav file
    if (data):
        write_sound('test_internet.wav', data)
    else:
        print('Failed to receive data')
    #close socket tcpSerSockection
    tcpSerSock.close()

if __name__ == '__main__':
    main()