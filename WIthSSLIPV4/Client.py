import socket, ssl, pprint
 


#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#context.verify_mode = ssl.CERT_REQUIRED
#context.check_hostname = True
#context.load_default_certs()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# require a certificate from the server 
ssl_sock = ssl.wrap_socket(s,ca_certs="/export/home/mg2026/cert", cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('192.168.0.2', 1765))


#print(repr(ssl_sock.getpeername())) 
pprint.pprint(ssl_sock.getpeercert())
#print(pprint.pformat(ssl_sock.getpeercert()))


# Set a simple HTTP request -- use http.client in actual code. ssl_sock.sendall("Hello")
 
# Read a chunk of data.  Will not necessarily
# read all the data returned by the server. 
data = ssl_sock.read()
print data
# note that closing the SSLSocket will also close the underlying socket ssl_sock.close()
