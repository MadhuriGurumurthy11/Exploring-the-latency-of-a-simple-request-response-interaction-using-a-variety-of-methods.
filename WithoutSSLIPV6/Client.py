import socket 
import time

sum=0.0 
timeValues=list() 
totalNoOfRuns=1000

#For TCP with IPv6
for i in range(totalNoOfRuns):
# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET6,socket.SOCK_STREAM,0)


# Connect as client to a selected server on a specified port
 
s.connect(("fd22:b0fd:7c46::2",1763,0,0))
#start the timer 
start = time.time()
#send a message to the server 
s.send("what is 2+3 ? \n\n")

#receive a response 
resp = s.recv(1024) if resp == "": break

# Close the connection when completed 
s.close()
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
