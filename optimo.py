from transicion import *

class camino:
	pass


caminoCanibal = [
					(0,3,3),
					(1,3,1),
					(0,3,2),
					(1,3,0),
					(0,3,1),
					(1,1,1),
					(0,2,2),
					(1,0,2),
					(0,0,3),
					(1,0,1),
					(0,0,2),
					(1,0,0)
		]

def canibal():

	solucionCanibal = []

	tran1 = Transicion('Pasar dos canibales', (0,3,3), (1,3,1))
	tran2 = Transicion('Devolver un canibal', (1,3,1), (0,3,2))
	tran3 = Transicion('Pasar dos canibales', (0,3,2), (1,3,0))
	tran4 = Transicion('Devoler un canibal', (1,3,0), (0,3,1))
	tran5 = Transicion('Pasar dos monjes', (0,3,1), (1,1,1))
	tran6 = Transicion('Devolver un monje y un canibal', (1,1,1), (0,2,2))
	tran7 = Transicion('Pasar dos monjes', (0,2,2), (1,0,2))
	tran8 = Transicion('Devolver un canibal', (1,0,2), (0,0,3))
	tran9 = Transicion('Pasar dos canibales', (0,0,3), (1,0,1))
	tran10 = Transicion('Devolver un canibal', (1,0,1), (0,0,2))
	tran11 = Transicion('Pasar dos canibales', (0,0,2), (1,0,0))

	solucionCanibal.append(tran1)
	solucionCanibal.append(tran2)
	solucionCanibal.append(tran3)
	solucionCanibal.append(tran4)
	solucionCanibal.append(tran5)
	solucionCanibal.append(tran6)
	solucionCanibal.append(tran7)
	solucionCanibal.append(tran8)
	solucionCanibal.append(tran9)
	solucionCanibal.append(tran10)
	solucionCanibal.append(tran11)

	return solucionCanibal




