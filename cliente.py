import socket
import sys
import sha1
import aes
import log

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=raw_input("Escriba host del servidor:")
try:
    sock.connect((host,8888))
except:
    print("host no encontrado")
    exit()
print("Se ha establecido conexion con el servidor, para salir ingrese un mensaje vacio")
def getMsg():
    return raw_input('Escriba su mensaje:')


def hashnormal():
    sock.sendall('op1')
    msg=getMsg()
    h=sha1.sha1(msg)
    msg=msg+h
    sock.sendall(msg)
    return 0
def hashClaveSimetrica():
    return 0
def hashValorSecreto():
    return 0
def salir():
    sock.sendall('0')
    print "Saliendo"
    sock.close()
    exit()
    return 0
def menu():
    sock.sendall('1')
    while True:
        print('\t1.- Hash normal\n\t2.- Hash con Clave Simetrica\n\t3.- Hash con Valor Secreto\n\t4.- Salir')
        try:
            opcion=int(raw_input('Seleccione Opcion:'))
            if opcion==1:
                hashnormal()
            elif opcion==2:
                hashClaveSimetrica()
            elif opcion==3:
                hashValorSecreto()
            elif opcion==4:
                salir()
            else:
                print("Por favor ingrese numeros del 1 al 4")
        except ValueError:
            print("Por favor ingrese numeros del 1 al 4")

menu()

while True:
    try:
        P=int(raw_input("Ingrese modulo:"))
        a=int(raw_input("Ingrese coeficiente a:"))
        b=int(raw_input("Ingrese coeficiente b:"))
        if not ecc.validaCoeficientes(a,b):
            print "Coeficientes a y b invalidos"
        elif P < 4:
            print "El Modulo debe ser mayor que 3"
        elif not ecc.esPrimo(P):
            print "El Modulo debe ser primo"
        else:
            break
    except ValueError:
        print("Por favor ingrese valores enteros")

while True:
    try:
        print("A continuacion se presentan los posibles puntos generadores, por favor seleccionar uno: ")
        ecc.puntosGeneradores(P,a,b)
        Gx=int(raw_input("Ingrese la coordenada en el eje X del punto generador: "))
        Gy=int(raw_input("Ingrese la coordenada en el eje y del punto generador: "))
        G=tuple((Gx,Gy))
        orden=ecc.validaGenerador(G,P,a,b)
        if orden==0:
            print("Numero generador invalido, favor seleccionar nuevamente")
        else:
            break
    except ValueError:
        print("Por favor ingrese valores enteros")

while True:
    try:
        n=int(raw_input("Ingrese su Clave Privada:"))
        if(n>orden or n<2):
            print("La clave debe ser mayor que 1 y menor que %d"%orden)
        else:
            break
    except ValueError:
        print("Por favor ingrese valores enteros")

clavePublica=ecc.multiplicaPunto(n,G,P,a)
print "Su clave publica es: %s"%str(clavePublica)
print "Esperando a Servidor"
sock.sendall('10')
while True:
    if sock.recv(1024)=='10':
        break
print "Intercambiando Clave Publica"

sock.sendall(str(clavePublica[0])+"|"+str(clavePublica[1]))

clave=sock.recv(1024)
clave=tuple(map(int,clave.split('|')))
print "Se ha recibido Clave %s"%str(clave)
claveCompartida=ecc.multiplicaPunto(n,clave,P,a)
print "La clave compartida es: %s"%str(claveCompartida)



    
sock.sendall('0')
print "Saliendo"
sock.close()