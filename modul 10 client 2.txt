# nama berkas: p_tcpcli.py
# Client TCP untuk server p_tcpser.py
import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50004))
print "Menghitung Luas Persegi"
while pesan.lower() != 'quit' :
    pesan = raw_input("Command: ")
    s.send(pesan)
    if pesan.lower() != 'quit':
        response = s.recv(1024)
        print 'Output: ', response
s.close()
