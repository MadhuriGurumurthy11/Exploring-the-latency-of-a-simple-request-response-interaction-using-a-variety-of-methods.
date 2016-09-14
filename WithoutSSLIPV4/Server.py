import socket

# Server example


# Establish a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Bind to TCP port No. 1989 ... 
s.bind(("",1989))
# ... and listen for anyone to contact you
# queueing up to five requests if you get a backlog 
s.listen(5)

# Servers are "infinite" loops handling requests 
while True:
 
# Wait for a connection connect, 
address = s.accept()

# Typically fork at this point


# Receive up to 1024 bytes
resp = (connect.recv(1024)).strip()
# And if the user has sent a "SHUTDOWN" 
if resp == "SHUTDOWN": break
#else: print resp


# Send an answer
connect.send("Latency is the delay from input into a system to desired outcome; the term is understood slightly differently in various contexts and latency issues also vary from one system to another.Latency greatly affects how usable and enjoyable electronic and mechanical devices as well as communications are.Latency in communication is demonstrated in live transmissions from various points on the earth as the communication hops between a ground transmitter and a satellite and from a satellite to a receiver each take time. People connecting from distances to these live events can be seen to have to wait for responses. This latency is the wait time introduced by the signal travelling the geographical distance as well as over the various pieces of communications equipment. Even fiber optics are limited by more than just the speed of light, as the refractive index of
 
the cable and all repeaters or amplifiers along their length introduce delays. \n")


# When done with a connection close it 
connect.close()
print "\ndone",address
