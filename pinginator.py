from ping import quiet_ping
import matplotlib.pyplot as plt

quiet_ping("192.168.1.1", 1, 2, 200, 64)

#plot the results
#fig = plt.figure()
#plt.plot(plist)
#plt.ylabel('Delay')
#fig.show()
#plt.show()
