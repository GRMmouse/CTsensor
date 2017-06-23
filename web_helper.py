import wave
from myStruct import *

# web_helper is a wrapper around built-in wave module developed for project CT sensor
# Performance of this module is not tested and guaranteed for any other purposes

def send_pack(sock, pack, SOL, EOL, BUF_SIZ, RESEND_MAX):
    # Send the packet, resend if faile
    if (not (len(SOL) == 1)):
        return False
    sock.send(SOL+ pack + EOL) # send the segment and EOL
    reply_msg = sock.recv(BUF_SIZ) # wait for server to reply
    counter = 0
    while (reply_msg == b'U'):
        sock.send(SOL+ pack + EOL)
        reply_msg = sock.recv(BUF_SIZ)
        counter +=1
        if (counter > RESEND_MAX):
            sock.send(b'F') 
            return False
    return True

def send_data(sock, data, EOL, BUF_SIZ = 2048, RESEND_MAX = 5, DISP_INT = 1000):
    # SInitialize variables
    PACKET_LEN = BUF_SIZ - len(EOL) - 1 #Just in case
    START= 0
    END= PACKET_LEN
    bytes = data.bytes
    prmts = data.prmts

    # Send pack count
    prmts_byte = (str(prmts)).encode()
    if (not send_pack(sock, prmts_byte, b'P', EOL, BUF_SIZ, RESEND_MAX)):
        print('Failed to send prmts')
        return False

    # Send the data
    while (START < len(bytes)):
        if ((START//PACKET_LEN) % DISP_INT == 0):
            percent_done = START*100//len(bytes);
            print('%d%%'%percent_done)
        pack = bytes[START:END] 
        if (not send_pack(sock, pack, b'D', EOL, BUF_SIZ, RESEND_MAX)):
            print('Failed to send data')
            return False
        START = END
        END = END + PACKET_LEN
    # Tell the server transmission is done
    sock.send(b'NM') 
    print('Send Done')
    return True

def recv_data(sock, EOL, BUF_SIZ = 2048, DISP_INT = 1000):
    data = myStruct()
    frames = b''
    counter = 0
    while True: # Danger! Infinite Loop
        # Receive data
        unpacked_data = sock.recv(BUF_SIZ)
        # Interpret Data
        succ = True
        if (unpacked_data == b'F'):
            print('Resend Failed')
            return None
        elif (unpacked_data == b'NM'):
            break;
        elif (unpacked_data[0:1] == b'P' and (unpacked_data[-len(EOL):] == EOL)):
            prmts_byte = unpacked_data[1:-len(EOL)]
            data.prmts = eval('wave.%s'%prmts_byte.decode()) # Danger! Eval!!!
        elif (unpacked_data[0:1] == b'D' and (unpacked_data[-len(EOL):] == EOL)):
            unpacked_data_tokeep= unpacked_data[1:-len(EOL)]
            frames += unpacked_data_tokeep 
        else:
            succ = False
        # Reply to the client
        if succ:
            sock.send('S'.encode())
            # Anxiety relif
            if (counter % DISP_INT == 0):
                print('%d packets received'%counter)
            counter = counter + 1
        else:
            print('Requesting resend')
            sock.send('U'.encode())
    data.bytes = frames
    print('Recieve Done')
    return data