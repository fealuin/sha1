import socket
import sys
import aes
import sha1
import log

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (('', 8888))
print 'Iniciando servidor %s en puerto %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'Esperando por una conexion'
    connection, client_address = sock.accept()
    print "Se ha recibido una conexion desde la direccion:",client_address[0],":",client_address[1]
    break
    
def handleHn():
	hn=connection.recv(1024)
	print 'Se ha recibido el mensaje %s, el texto es %s y el hash %s'%(hn,hn[:-40],hn[-40:])
	hh=sha1.sha1(hn[:-40])
	print hh,len(hh)
	print 'Al calcular el hash sha1 del texto \"%s\"" se obtiene: %s que'%(hn[:-40],hh)+' ' if hh==hn[-40:] else ' no ', 'coincide'

while True:
    msg=connection.recv(1024)
    if msg=='op1':
    	handleHn()
    if msg:
        print 'Se ha recibido :%s'%msg    
print "Intercambiando Clave Publica"

connection.sendall(str(clavePublica[0])+"|"+str(clavePublica[1]))

clave=connection.recv(1024)
clave=tuple(map(int,clave.split('|')))
print "Se ha recibido Clave %s"%str(clave)

claveCompartida=ecc.multiplicaPunto(n,clave,P,a)
print "La clave compartida es: %s"%str(claveCompartida)

#while(True):
#    inicio=int(connection.recv(1024))
#    if inicio>0: #Inicia la conversacion con en largo del mensaje, si es 0 se sale
#        print("Se esta recibiendo un mensaje\n")
#        iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
#        k=(raw_input("Escriba clave:\n")+" "*16)[:16]
#        cfb.reccfb(k,iv,connection,inicio)
#    else:
#        break
#    if(inicio==0):break
                
print("El cliente se ha desconectado, saliendo..")
connection.close()
