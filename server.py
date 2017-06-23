from socket import *
from time import ctime
import wave

HOST = '192.168.0.105'
PORT = 1235
BUFSIZ = 2048
ADDR = (HOST, PORT)


def main():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    frames = b""
    EOL = "EOL".encode()
    flag = True

    while flag:
        print('Waiting for connection...')
        (tcpCliSock, addr) = tcpSerSock.accept()
        (IP, port) = addr
        print('...Connected from: %s:%d'%(IP, port))

        while True:
            unpacked_data = tcpCliSock.recv(BUFSIZ)
            if (unpacked_data[-3:] == EOL): #check to see if the end of the packet has 'eol!!'
                tcpCliSock.send("S".encode())
                unpacked_data_tokeep= unpacked_data[:-3]
                frames += unpacked_data_tokeep
            elif (unpacked_data.decode() == "NM"):
                print("End of data")
                flag=False
                tcpCliSock.close()
                break
            else:
                tcpCliSock.send("U".encode())  #if eol doesnt match ask to resend
                print("resend data")

    #save packed data to a .wav file
    

    #close socket tcpSerSockection
    tcpSerSock.close()

if __name__ == '__main__':
    main()