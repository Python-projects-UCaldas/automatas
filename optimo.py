from transicion import *

class camino:
	pass

##########################GRAFO INICIAL##########################

def grafOveja():
	grafoOveja = []

	tran1 = Transicion('', (0,0,0,0), (1,0,0,0))
	tran2 = Transicion('', (0,0,0,0), (1,0,0,1))
	tran3 = Transicion('', (0,0,0,0), (1,0,1,0))
	tran4 = Transicion('', (1,0,0,0), (0,0,0,0))
	tran5 = Transicion('', (1,0,0,1), (0,0,0,1))
	tran6 = Transicion('', (1,0,0,1), (0,0,0,0))
	tran7 = Transicion('', (0,0,0,1), (1,1,0,1))
	tran8 = Transicion('', (0,0,0,1), (1,0,1,1))
	tran9 = Transicion('', (1,1,0,1), (0,1,0,0))
	tran10 = Transicion('', (1,1,0,1), (0,0,0,1))
	tran11 = Transicion('', (1,1,0,1), (0,1,0,1))
	tran12 = Transicion('',(0,1,0,0),(1,1,1,0))
	tran13 = Transicion('',(0,1,0,0),(1,1,0,1))
	tran14 = Transicion('',(0,1,0,0),(1,1,0,0))
	tran15 = Transicion('',(0,1,0,1),(1,1,0,1))
	tran16 = Transicion('',(0,1,0,1),(1,1,1,1))
	tran17 = Transicion('',(1,1,0,0),(0,1,0,0))
	tran18 = Transicion('',(1,1,0,0),(0,0,0,0))
	tran19 = Transicion('',(1,0,1,1),(0,0,0,1))
	tran20 = Transicion('',(1,0,1,1),(0,0,1,1))
	tran21 = Transicion('',(1,0,1,1),(0,0,1,0))
	tran22 = Transicion('',(1,1,1,0),(0,1,0,0))
	tran23 = Transicion('',(1,1,1,0),(0,0,1,0))
	tran24 = Transicion('',(0,0,1,0),(1,1,1,0))
	tran25 = Transicion('',(0,0,1,0),(1,0,1,1))
	tran26 = Transicion('',(0,1,1,1),(1,1,1,1))
	tran27 = Transicion('',(1,0,1,0),(0,0,1,0))

	for i in range(1, 28):
		variable = 'tran' + str(i)
		grafoOveja.append(vars()[variable])

	return grafoOveja

def grafoCanival():
	canibal = []

	tran1 = Transicion('', (0,0,0), (1,2,3))
	tran2 = Transicion('', (0,0,0), (1,3,2))
	tran3 = Transicion('', (0,0,0), (1,2,2))
	tran4 = Transicion('', (0,0,0), (1,1,2))
	tran5 = Transicion('', (0,0,0), (1,3,1))
	tran6 = Transicion('', (0,0,1), (1,0,0))
	tran7 = Transicion('', (0,0,2), (1,0,0))
	tran8 = Transicion('', (0,0,2), (1,0,1))
	tran9 = Transicion('', (0,0,3), (1,0,1))
	tran10 = Transicion('', (0,0,3), (1,0,2))
	tran11 = Transicion('', (0,1,0), (1,0,0))
	tran12 = Transicion('', (0,1,1), (1,1,0))
	tran13 = Transicion('', (0,1,1), (1,0,1))
	tran14 = Transicion('', (0,1,1), (1,1,1))
	tran15 = Transicion('', (0,1,2), (1,0,1))
	tran16 = Transicion('', (0,1,2), (1,1,0))
	tran17 = Transicion('', (0,1,3), (1,0,2))
	tran18 = Transicion('', (0,1,3), (1,1,2))
	tran19 = Transicion('', (0,2,0), (1,1,0))
	tran20 = Transicion('', (0,2,0), (1,0,0))
	tran21 = Transicion('', (0,2,1), (1,1,0))
	tran22 = Transicion('', (0,2,1), (0,0,1))
	tran23 = Transicion('', (0,2,1), (1,2,0))
	tran24 = Transicion('', (0,2,2), (1,0,2))
	tran25 = Transicion('', (0,2,2), (1,2,0))
	tran26 = Transicion('', (0,2,2), (1,1,1))
	tran27 = Transicion('', (0,2,2), (1,1,2))
	tran28 = Transicion('', (0,2,2), (1,2,1))
	tran29 = Transicion('', (0,2,3), (1,0,3))
	tran30 = Transicion('', (0,2,3), (1,1,3))
	tran31 = Transicion('', (0,2,3), (1,2,2))
	tran32 = Transicion('', (0,2,3), (1,2,1))
	tran33 = Transicion('', (0,2,3), (1,1,2))
	tran34 = Transicion('', (0,3,0), (1,2,0))
	tran35 = Transicion('', (0,3,0), (1,1,0))
	tran36 = Transicion('', (0,3,1), (1,2,1))
	tran37 = Transicion('', (0,3,1), (1,1,1))
	tran38 = Transicion('', (0,3,1), (1,3,0))
	tran39 = Transicion('', (0,3,1), (1,2,0))
	tran40 = Transicion('', (0,3,2), (1,2,2))
	tran41 = Transicion('', (0,3,2), (1,1,2))
	tran42 = Transicion('', (0,3,2), (1,3,1))
	tran43 = Transicion('', (0,3,2), (1,3,0))
	tran44 = Transicion('', (0,3,2), (1,2,1))
	tran45 = Transicion('', (0,3,3), (1,1,3))
	tran46 = Transicion('', (0,3,3), (1,2,3))
	tran47 = Transicion('', (0,3,3), (1,3,2))
	tran48 = Transicion('', (0,3,3), (1,3,1))
	tran49 = Transicion('', (0,3,3), (1,2,2))
	tran50 = Transicion('', (1,0,0), (0,1,0))
	tran51 = Transicion('', (1,0,0), (0,2,0))
	tran52 = Transicion('', (1,0,0), (0,0,1))
	tran53 = Transicion('', (1,0,0), (0,0,2))
	tran54 = Transicion('', (1,0,0), (0,1,1))
	tran55 = Transicion('', (1,0,1), (0,1,1))
	tran56 = Transicion('', (1,0,1), (0,2,1))
	tran57 = Transicion('', (1,0,1), (0,0,2))
	tran58 = Transicion('', (1,0,1), (0,0,3))
	tran59 = Transicion('', (1,0,1), (0,1,2))
	tran60 = Transicion('', (1,0,2), (0,1,2))
	tran61 = Transicion('', (1,0,2), (0,2,2))
	tran62 = Transicion('', (1,0,2), (0,0,3))
	tran63 = Transicion('', (1,0,2), (0,1,3))
	tran64 = Transicion('', (1,0,3), (0,1,3))
	tran65 = Transicion('', (1,0,3), (1,2,3))
	tran66 = Transicion('', (1,1,0), (0,2,0))
	tran67 = Transicion('', (1,1,0), (0,3,0))
	tran68 = Transicion('', (1,1,0), (0,1,1))
	tran69 = Transicion('', (1,1,0), (0,1,2))
	tran70 = Transicion('', (1,1,0), (0,2,1))
	tran71 = Transicion('', (1,1,1), (0,2,1))
	tran72 = Transicion('', (1,1,1), (0,3,1))
	tran73 = Transicion('', (1,1,1), (0,1,2))
	tran74 = Transicion('', (1,1,1), (0,1,3))
	tran75 = Transicion('', (1,1,1), (0,2,2))
	tran76 = Transicion('', (1,1,2), (0,2,2))
	tran77 = Transicion('', (1,1,2), (0,3,2))
	tran78 = Transicion('', (1,1,2), (0,1,3))
	tran79 = Transicion('', (1,1,2), (0,2,3))
	tran80 = Transicion('', (1,1,3), (0,2,3))
	tran81 = Transicion('', (1,1,3), (0,3,3))
	tran82 = Transicion('', (1,2,0), (0,3,0))
	tran83 = Transicion('', (1,2,0), (0,2,1))
	tran84 = Transicion('', (1,2,0), (0,2,2))
	tran85 = Transicion('', (1,2,0), (0,3,1))
	tran86 = Transicion('', (1,2,1), (0,3,1))
	tran87 = Transicion('', (1,2,1), (0,2,2))
	tran88 = Transicion('', (1,2,1), (0,2,3))
	tran89 = Transicion('', (1,2,1), (0,3,2))
	tran90 = Transicion('', (1,2,2), (0,3,2))
	tran91 = Transicion('', (1,2,2), (0,2,3))
	tran92 = Transicion('', (1,2,2), (0,3,3))
	tran93 = Transicion('', (1,2,3), (0,3,3))
	tran94 = Transicion('', (1,3,0), (0,3,1))
	tran95 = Transicion('', (1,3,0), (0,3,2))
	tran96 = Transicion('', (1,3,1), (0,3,2))
	tran97 = Transicion('', (1,3,1), (0,3,3))
	tran98 = Transicion('', (1,3,2),(0,3,3))

	
	for i in range(1, 99):
		variable = 'tran' + str(i)
		canibal.append(vars()[variable])
	
	return canibal

# def grafoFamilia():
# 	familia = []

# 	tran1 = Transicion('', (), ())
	

	
# 	for i in range(1, ):
# 		variable = 'tran' + str(i)
# 		familia.append(vars()[variable])
	
# 	return familia
##########################CAMINOS##########################
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

caminoOveja=[	(0,0,0,0),
				(1,0,1,0),
				(0,0,1,0),  
				(1,0,1,1),
				(0,0,0,1),
				(1,1,0,1),
				(0,1,0,1),
				(1,1,1,1)
			]

caminoFamilia=[ (0,0,0,0,0,0),
				(1,1,1,0,0,0),
				(0,0,1,0,0,0),
				(1,0,1,0,1,1),
				(0,0,0,0,1,1),
				(1,1,0,1,1,1),
				(0,0,0,1,1,1),
				(1,1,1,1,1,1)
				]

##########################SOLUCION##########################
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

	for i in range(1, 12):
		variable = 'tran' + str(i)
		solucionCanibal.append(vars()[variable])

	return solucionCanibal


def familia():
	solucionFamilia=[]

	tran1=Transicion('Pasar flaco y gordo. Tiempo=3', (0,0,0,0,0,0), (1,1,1,0,0,0))
	tran2=Transicion('Devolver flaco. Tiempo=4',(1,1,1,0,0,0),(0,0,1,0,0,0))
	tran3=Transicion('Llevar anciano y hombre. Tiempo=16',(0,0,1,0,0,0),(1,0,1,0,1,1))
	tran4=Transicion('Devolver gordo. Tiempo=19',(1,0,1,0,1,1),(0,0,0,0,1,1))
	tran5=Transicion('Llevar flaco y mujer. Tiempo=25',(0,0,0,0,1,1),(1,1,0,1,1,1))
	tran6=Transicion('Devolver flaco. Tiempo=26',(1,1,0,1,1,1),(0,0,0,1,1,1))
	tran7=Transicion('Llevar flaco y gordo. Tiempo=29 ',(0,0,0,1,1,1),(1,1,1,1,1,1))

	for i in range(1, 8):
		variable = 'tran' + str(i)
		solucionFamilia.append(vars()[variable])

	return solucionFamilia

def oveja():
	solucionOveja=[]

	tran1=Transicion('Pasar Oveja', (0,0,0,0), (1,0,1,0))
	tran2=Transicion('Devolver Bote',(1,0,1,0),(0,0,1,0))
	tran3=Transicion('Llevar lobo',(0,0,1,0),(1,0,1,1))
	tran4=Transicion('Devolver Barca y oveja',(1,0,1,1),(0,0,0,1))
	tran5=Transicion('Llevar alimento',(0,0,0,1),(1,1,0,1))
	tran6=Transicion('Devolver bote',(1,1,0,1),(0,1,0,1))
	tran7=Transicion('Llevar oveja',(0,1,0,1),(1,1,1,1))
	
	for i in range(1, 8):
		variable = 'tran' + str(i)
		solucionOveja.append(vars()[variable])

	return solucionOveja



