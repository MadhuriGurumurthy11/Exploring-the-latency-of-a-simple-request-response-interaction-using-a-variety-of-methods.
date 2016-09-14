import socket, ssl


bindsocket = socket.socket() bindsocket.bind(('', 1765)) 
bindsocket.listen(5)
while True:
	newsocket, fromaddr = bindsocket.accept() 
	connstream = ssl.wrap_socket(newsocket, server_side=True,
				certfile="cert", keyfile="key",
				ssl_version=ssl.PROTOCOL_TLSv1) 
data = connstream.read()
 
# null data means the client is finished with us 
while data:
	if data == "SHUTDOWN": break 
	else: print data
# we'll assume do_something returns False
# when we're finished with client
#break 
connstream.send("Heyyyy!!! \n")
# finished with client 
connstream.close() 
print "\ndone",address
