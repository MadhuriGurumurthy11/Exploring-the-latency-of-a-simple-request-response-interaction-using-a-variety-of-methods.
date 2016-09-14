import socket


# Server example


# Establish a TCP/IP socket
s = socket.socket(socket.AF_INET6,socket.SOCK_STREAM,0)


# Bind to TCP port No. 1763 ... 
s.bind(("",1763))
# ... and listen for anyone to contact you
# queueing up to five requests if you get a backlog 
s.listen(5)

# Servers are "infinite" loops handling requests 
while True:

# Wait for a connection 
connect,address = s.accept()
 


# Typically fork at this point


# Receive up to 1024 bytes
resp = (connect.recv(1024)).strip()
# And if the user has sent a "SHUTDOWN"
# instruction, do so (ouch! just a demo) 
if resp == "SHUTDOWN": break
else: print resp


# Send an answer 
connect.send("it's 5!! \n")

# And there could be a lot more here!


# When done with a connection close it 
connect.close()
print "\ndone",address
