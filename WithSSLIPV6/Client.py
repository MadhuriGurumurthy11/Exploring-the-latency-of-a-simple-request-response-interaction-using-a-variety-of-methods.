import socket, ssl, pprint 
import time

sum=0.0 
timeValues=list() 
totalNoOfRuns=1000

#For TCP with IPv6
 
for i in range(totalNoOfRuns):
	s = socket.socket(socket.AF_INET6,socket.SOCK_STREAM,0)


# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself. 
	ssl_sock = ssl.wrap_socket(s,
			ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
			ssl_sock.connect(("fd22:b0fd:7c46::2",8834,0,0))


#print repr(ssl_sock.getpeername())
#print ssl_sock.cipher()
#print pprint.pformat(ssl_sock.getpeercert())
#start the timer 
start = time.time()
ssl_sock.write("What's your name?") 
data = ssl_sock.read()
#print data
if False: # from the Python 2.7.3 docs
# Set a simple HTTP request -- use httplib in actual code.
 
#ssl_sock.write("""GET / HTTP/1.0\r
#Host: www.verisign.com\n\n""") 
ssl_sock.write("Hello")
 
# Read a chunk of data.  Will not necessarily
# read all the data returned by the server. 
data = ssl_sock.read()
#print data
# note that closing the SSLSocket will also close the underlying
 
ssl_sock.close()
#stop the timer 
end = time.time()
#Calculate the total time taken 
totalTime=end - start
#print "totalTime=",totalTime 
timeValues.append(totalTime) 
sum=sum+totalTime

#Calculate the mean 
mean=sum/totalNoOfRuns 
print "sum=",sum
 
print "mean=",mean
