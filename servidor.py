import socket
import sys
import aes
import sha1
import log





def getValorSecreto():
    return raw_input('Escriba el valor secreto:')

def getClave():
    return (raw_input('Escriba la clave compartida:')+" "*16)[:16]

def handleHn():
	hn=connection.recv(1024)
	print 'Se ha recibido el mensaje %s, el texto es %s y el hash %s'%(hn,hn[:-40],hn[-40:])
	hh=sha1.sha1(hn[:-40])
	print hh,len(hh)
	print 'Al calcular el hash sha1 del texto \"%s\" se obtiene: %s que'%(hn[:-40],hh)+' ' if hh==hn[-40:] else ' no ', 'coincide'

def handleHashClaveSimetrica():
	hn=connection.recv(1024)
	print 'Se ha recibido el mensaje %s, el texto es %s y el hash %s'%(hn,hn[:-48],hn[-48:])
	k=getClave()
	hh=sha1.sha1(hn[:-48])
	print hh,len(hh)
	dhh=(aes.aes('d',hn[-48:],k))[:40]
	print 'Al desenciptar %s se obtiene %s'%(hn[-48:],dhh)
	print 'Al calcular el hash sha1 del texto \"%s\" se obtiene: %s que'%(hn[:-48],hh)+' ' if hh==dhh else ' no ', 'coincide'

def handleHashValorSecreto():
	hvs=connection.recv(1024)
	print 'Se ha recibido el mensaje %s, el texto es %s y el hash %s'%(hvs,hvs[:-40],hvs[-40:])
	vs=getValorSecreto()
	hh=sha1.sha1(hvs[:-40]+vs)
	print hh,len(hh)
	print 'Al calcular el hash sha1 del texto \"%s\" mas el valor secreto %s se obtiene: %s que'%(hvs[:-40],vs,hh),' ' if hh==hvs[-40:] else ' no ', 'coincide'

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

while True:
    msg=connection.recv(1024)
    if msg:
        print 'Se ha recibido :%s'%msg    
    if msg=='hn':
    	handleHn()
    elif msg=='hcs':
    	handleHashClaveSimetrica()
    elif msg=='hvs':
    	handleHashValorSecreto()
    elif msg=='0':
    	print 'El cliente se ha desconectado, saliendo'
    	connection.close()
    	exit()

