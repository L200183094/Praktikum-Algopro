#nama berkas: p_tcpser.py
#TCP Server untuk client p_tcpcli.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50004))
s.listen(5)
print "Menghitung luas persegi"
data = ''
while data.lower() != 'quit' :
       komm, addr = s.accept()
       sisi = 0
       while data.lower() != 'quit':
              data = komm.recv(1024)
              if data.lower() == 'quit' :
                     s.close()
                     break
              print'Command: ', data
              try:
                     sisi = int(data)
                     komm.send('data tersimpan')
              except ValueError:       
                     if data.lower() == 'hitung':
                            respon = 'luas persegi dengan sisi '+str(sisi)+' = '+str(sisi*sisi)
                            komm.send(respon)
              
                     else:
                            komm.send('unknown command') #data dikirim balik
