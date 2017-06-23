from socket import *
from time import ctime

# Globals are evil
HOST = '192.168.0.105'#'139.196.182.136'
PORT = 1235
BUFSIZ = 2048
ADDR = (HOST, PORT)
PACKET_LEN = BUFSIZ-20
START= 0
END= PACKET_LEN #or however many bytes to send
DISP_INT = 1000
EOL= "EOL".encode()





tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    while (END < len(frame)):
        if ((START//PACKET_LEN) % DISP_INT == 0):
            print(START/len(frame)*100)
        pack = frame[START:END] 
        tcpCliSock.send(pack + EOL) #send the segment and EOL
        reply_msg = tcpCliSock.recv(BUF_SIZ)
        counter=0
        while (reply_msg.decode() == "U"):
            tcpCliSock.send(pack + EOL)  #resend the data
            counter +=1
            if (counter > 10):  #if try to resend 10 times unsuccessfully, break
                print("Maximu retry failed")
                exit()

        START = END
        END = END + PACKET_LEN #or whatever increment you want to use
    last_pack = frame[START:]
    tcpCliSock.send(last_pack + EOL)
    reply_msg = tcpCliSock.recv(BUF_SIZ)
    counter=0
    while (reply_msg.decode() == "U"):
        tcpCliSock.send(last_pack + EOL)  #resend the data
        counter +=1
        if (counter > 10):
            print("M")
            exit()

    tcpCliSock.send("NM".encode()) #send a message signaling end of data
    print("end of data")
else:
    tcpCliSock.send(data.encode())
    dataIn = tcpCliSock.recv(BUFSIZ).decode()
    print('%s:%d[%s]>%s'%(HOST, PORT, ctime(), dataIn))

tcpCliSock.close()