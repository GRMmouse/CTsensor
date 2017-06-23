from socket import *
from wave_helper import *
from web_helper import *

# Globals are evil
# Internet Globas
HOST = '192.168.0.105'#'139.196.182.136'
PORT = 1235
BUF_SIZ = 2048
ADDR = (HOST, PORT)
# Packet Globals
EOL= b'EOL'
RESEND_MAX = 5
DISP_INT = 1000

def main():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    data = read_sound('test.wav')
    send_data(tcpCliSock, data, EOL, BUF_SIZ, RESEND_MAX, DISP_INT)
    tcpCliSock.close()

if __name__ == '__main__':
    main()