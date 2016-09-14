import socket 
import time

sum1=0.0 
timeValues=list() 
totalNoOfRuns=1000

#For TCP with IPv4
for i in range(totalNoOfRuns):

#print start 
start=time.time()
# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Connect as client to a selected server on a specified port 
s.connect(("192.168.0.2",1989))

#send a message to the server 
s.send("what's latency? \n\n")
 
#receive a response 
resp = s.recv(1024) 

if resp == "": break

# Close the connection when completed 
s.close()

end=0.0
#stop the timer 
end = (time.time())
#print end,"-",start
#print end
#Calculate the total time taken 
totalTime=(end - start)
#print totalTime
print "totalTime=",totalTime timeValues.append(totalTime) 
sum1=sum1+totalTime
 
#Calculate the mean 
print "sum=",sum1
mean=((sum1)/totalNoOfRuns) 
print "mean=",(mean)
