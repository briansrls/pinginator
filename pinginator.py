from rtping import quiet_ping
import matplotlib.pyplot as plt

#Arguments: ADDRESS, REALTIME PLOT, SEND DELAY, TIMEOUT (SECONDS), COUNT, PACKET-SIZE

plist = quiet_ping("192.168.1.1", 1, 1, 2, 200, 64)

#plot the final results
#fig = plt.figure()
#plt.plot(plist)
#fig.show()
plt.show()
