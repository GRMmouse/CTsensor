# web_helper is a wrapper around built-in wave module developed for project CT sensor
# Performance of this module is not tested and guaranteed for any other purposes

def send_sound(sock, bytes, SOL, EOL, BUF_SIZ = 2048, RESEND_MAX = 5, DISP_INT = 1000):
    # Segmentize and send
    PACKET_LEN = BUF_SIZ - len(EOL) - len(SOL) - 1 #Just in case
    START= 0
    END= PACKET_LEN
    while (START < len(bytes)):
        if ((START//PACKET_LEN) % DISP_INT == 0):
            percent_done = START/len(bytes)*100;
            print("%02f%% sent"%percent_done)
        pack = bytes[START:END] 
        sock.send(SOL+ pack + EOL) # send the segment and EOL
        reply_msg = sock.recv(BUF_SIZ) # wait for server to reply
        counter=0
        while (reply_msg.decode() == "U"):
            sock.send(pack + EOL)
            counter +=1
            if (counter > RESEND_MAX):
                sock.send("F".encode()) 
                return False
        START = END
        END = END + PACKET_LEN
    sock.send("NM".encode()) # tell the server transmission is done
    return True

def recv_sound(sock, bytes, EOL, pack_count, BUF_SIZ = 2048, DISP_INT = 1000):
    frames = b""
    for i in range(pack_count)
        if (i % DISP_INT == 0):
            percent_done = i/pack_count * 100;
            print("%02f%% received"%percent_done)
        unpacked_data = sock.recv(BUFSIZ)
        
        if (unpacked_data[-len(EOL):] == EOL):
            sock.send("S".encode())
            unpacked_data_tokeep= unpacked_data[:-len(EOL)]
            frames += unpacked_data_tokeep
        elif (unpacked_data.decode() == "NM"):
            sock.close()
            return frames
        else:
            tcpCliSock.send("U".encode())  #if eol doesnt match ask to resend
            print("resend data")