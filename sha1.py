
#Vectores Iniciales





def int64ToStr(numero):
	numero=numero%pow(2,64)
	texto=''
	for i in range(8):
		texto=chr((numero/pow(256,i))%256)+texto
	return texto


def rellenaTexto(texto):
	i=1
	largoOriginal=len(texto)*8
	while not len(texto)%64==56:
		if i:
			texto=texto+chr(0b10000000)
		else:
			texto=texto+chr(0b00000000)
		i=0
	texto=texto+int64ToStr(largoOriginal)
	return texto


def textoABloques(texto):
	texto=rellenaTexto(texto)
	#print texto,len(texto)
	bloques=[]
	bloque=[]
	for i in range(len(texto)/4):
		bloque.append(int(texto[i*4:i*4+4].encode('hex'),16)) 
		if(i+1)%16==0:
			bloques.append(bloque)
			bloque=[]
	#print len(bloques)
	return bloques

def rotar32(numero,n):
	return ((numero<<n)|(numero>>(32-n)))&0xFFFFFFFF

def sha1(texto):
	h0 = 0x67452301
	h1 = 0xEFCDAB89
	h2 = 0x98BADCFE
	h3 = 0x10325476
	h4 = 0xC3D2E1F0
	bloques=textoABloques(texto)
	(a,b,c,d,e)=(h0,h1,h2,h3,h4) #Inicializando vectores
	#expandiendo
	for bloque in bloques:
		for i in range(16,80):
			bloque.append(rotar32(bloque[i-3]^bloque[i-8]^bloque[i-14]^bloque[i-16],1))
	#Ronda principal
	for bloque in bloques:
		for i in range(80):
			if 0<=i<=19:
				f=(b&c)|((~b)&d)
				k=0x5A827999
			elif 20<=i<=39:
				f=b^c^d
				k=0x6ED9EBA1
			elif 40<=i<=59:
				f=(b&c)|(b&d)|(c&d) 
				k=0x8F1BBCDC
			elif 60<=i<=79:
				f=b^c^d
				k=0xCA62C1D6
			temp=(rotar32(a,5)+f+e+k+bloque[i])&0xFFFFFFFF
			(e,d,c,b,a)=(d,c,rotar32(b,30),a,temp)
		(h0,h1,h2,h3,h4)=(h0+a&0xFFFFFFFF,h1+b&0xFFFFFFFF,h2+c&0xFFFFFFFF,h3+d&0xFFFFFFFF,h4+e&0xFFFFFFFF)
	return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


print sha1('A Test')
#print map(hex,map(ord,list(rellenaTexto('SHA1 es una funcion hash.'))))
#print list(int64ToStr(0b11001000))