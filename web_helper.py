from socket import *
# wave_helper is a wrapper around built-in wave module developed for project CT sensor
# Performance of this module is not tested and guaranteed for any other purposes

def sendSound(sock, pack_len, EOL = "EOL"):