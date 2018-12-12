# nama berkas: p_tcpcli.py
# Client TCP untuk server p_tcpser.py
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
print "Automatic answering machine is ready"
while pesan.lower() != 'exit' :
    pesan = raw_input("Questions: ")
    s.send(pesan)
    if pesan.lower() != 'exit':
        response = s.recv(1024)
        print 'The answer: ', response
response = s.recv(1024)
print 'The answer: ', response
s.close()
