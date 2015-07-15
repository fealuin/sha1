
def rellenaTexto(texto):
	i=1
	while not len(texto)%64==56:
		if i:
			texto=texto+chr(0b10000000)
		else:
			texto=texto+chr(0b00000000)
		i=0
	texto=texto+chr(len(texto)/pow(256,3))+chr(len(texto)/pow(256,2))+chr(len(texto)/256)+chr(len(texto)%256)
	print '\"'+texto+'\"',len(texto)
	return texto

def textoABloque(texto):
	texto=rellenaTexto(texto)


rellenaTexto('')