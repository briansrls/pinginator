from ping import quiet_ping
import matplotlib.pyplot as plt

#Arguments: ADDRESS, SEND DELAY, TIMEOUT (SECONDS), COUNT, PACKET-SIZE

quiet_ping("192.168.1.1", 1, 2, 200, 64)

