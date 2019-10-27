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

def grafoFamilia():
	familia = []
	tran1 = Transicion('', (0,0,0,0,0,0), (1,1,1,0,0,0))
	tran2 = Transicion('', (0,0,0,0,0,0), (1,1,0,1,0,0))
	tran3 = Transicion('', (0,0,0,0,0,0), (1,1,0,0,0,1))
	tran4 = Transicion('', (0,0,0,0,0,0), (1,1,0,0,1,0))
	tran5 = Transicion('', (0,0,0,0,0,0), (1,0,1,1,0,0))
	tran6 = Transicion('', (0,0,0,0,0,0), (1,0,1,0,1,0))
	tran7 = Transicion('', (0,0,0,0,0,0), (1,0,1,0,0,1))
	tran8 = Transicion('', (0,0,0,0,0,0), (1,0,0,1,1,0))
	tran9 = Transicion('', (0,0,0,0,0,0), (1,0,0,1,1,0))
	tran10 = Transicion('', (0,0,0,0,0,0), (1,0,0,0,1,1))
	tran11 = Transicion('', (0,0,0,0,0,1), (1,1,1,0,0,1))
	tran12 = Transicion('', (0,0,0,0,0,1), (1,1,0,1,0,1))
	tran13 = Transicion('', (0,0,0,0,0,1), (1,1,0,0,1,1))
	tran14 = Transicion('', (0,0,0,0,0,1), (1,0,1,1,0,1))
	tran15 = Transicion('', (0,0,0,0,0,1), (1,0,1,0,1,1))
	tran16 = Transicion('', (0,0,0,0,0,1), (1,0,0,1,1,1))
	tran17 = Transicion('', (0,0,0,0,1,0), (1,1,1,0,1,0))
	tran18 = Transicion('', (0,0,0,0,1,0), (1,1,0,1,1,0))
	tran19 = Transicion('', (0,0,0,0,1,0), (1,1,0,0,1,1))
	tran20 = Transicion('', (0,0,0,0,1,0), (1,0,1,1,1,0))
	tran21 = Transicion('', (0,0,0,0,1,0), (1,0,1,0,1,1))
	tran22 = Transicion('', (0,0,0,0,1,0), (1,0,0,1,1,1))
	tran23 = Transicion('', (0,0,0,0,1,1), (1,1,1,0,1,1))
	tran24 = Transicion('', (0,0,0,0,1,1), (1,1,0,1,1,1))
	tran25 = Transicion('', (0,0,0,0,1,1), (1,0,1,1,1,1))
	tran26 = Transicion('', (0,0,0,1,0,0), (1,1,1,1,0,0))
	tran27 = Transicion('', (0,0,0,1,0,0), (1,1,0,1,1,0))
	tran28 = Transicion('', (0,0,0,1,0,0), (1,1,0,1,0,1))
	tran29 = Transicion('', (0,0,0,1,0,0), (1,0,1,1,1,0))
	tran30 = Transicion('', (0,0,0,1,0,0), (1,0,1,1,0,1))
	tran31 = Transicion('', (0,0,0,1,0,0), (1,0,0,1,1,1))
	tran32 = Transicion('', (0,0,0,1,0,1), (1,1,1,1,0,1))
	tran33 = Transicion('', (0,0,0,1,0,1), (1,1,0,1,1,1))
	tran34 = Transicion('', (0,0,0,1,0,1), (1,0,1,1,1,1))
	tran35 = Transicion('', (0,0,0,1,1,0), (1,1,1,1,1,0))
	tran36 = Transicion('', (0,0,0,1,1,0), (1,1,0,1,1,1))
	tran37 = Transicion('', (0,0,0,1,1,0), (1,0,1,1,1,1))
	tran38 = Transicion('', (0,0,0,1,1,1), (1,1,1,1,1,1))
	tran39 = Transicion('', (0,0,1,0,0,0), (1,1,1,1,0,0))
	tran40 = Transicion('', (0,0,1,0,0,0), (1,1,1,0,1,0))
	tran41 = Transicion('', (0,0,1,0,0,0), (1,1,1,0,0,1))
	tran42 = Transicion('', (0,0,1,0,0,0), (1,0,1,1,1,0))
	tran43 = Transicion('', (0,0,1,0,0,0), (1,0,1,1,0,1))
	tran44 = Transicion('', (0,0,1,0,0,0), (1,0,1,0,1,1))
	tran45 = Transicion('', (0,0,1,0,0,1), (1,1,1,1,0,1))
	tran46 = Transicion('', (0,0,1,0,0,1), (1,1,1,0,1,1))
	tran47 = Transicion('', (0,0,1,0,0,1), (1,0,1,1,1,1))
	tran48 = Transicion('', (0,0,1,0,1,0), (1,1,1,1,1,0))
	tran49 = Transicion('', (0,0,1,0,1,0), (1,1,1,0,1,1))
	tran50 = Transicion('', (0,0,1,0,1,0), (1,0,1,1,1,1))
	tran51 = Transicion('', (0,0,1,0,1,1), (1,1,1,1,1,1))
	tran52 = Transicion('', (0,0,1,1,0,0), (1,1,1,1,1,0))
	tran53 = Transicion('', (0,0,1,1,0,0), (1,1,1,1,0,1))
	tran54 = Transicion('', (0,0,1,1,0,0), (1,0,1,1,1,1))
	tran55 = Transicion('', (0,0,1,1,0,1), (1,1,1,1,1,1))
	tran56 = Transicion('', (0,0,1,1,1,0), (1,1,1,1,1,1))
	tran57 = Transicion('', (0,0,1,1,1,1), (1,1,1,1,1,1))
	tran58 = Transicion('', (0,1,0,0,0,0), (1,1,1,1,0,0))
	tran59 = Transicion('', (0,1,0,0,0,0), (1,1,1,0,1,0))
	tran60 = Transicion('', (0,1,0,0,0,0), (1,1,1,0,0,1))
	tran61 = Transicion('', (0,1,0,0,0,0), (1,1,0,1,1,0))
	tran62 = Transicion('', (0,1,0,0,0,0), (1,1,0,1,0,1))
	tran63 = Transicion('', (0,1,0,0,0,0), (1,1,0,0,1,1))
	tran64 = Transicion('', (0,1,0,0,0,1), (1,1,1,1,0,1))
	tran65 = Transicion('', (0,1,0,0,0,1), (1,1,1,0,1,1))
	tran66 = Transicion('', (0,1,0,0,0,1), (1,1,0,1,1,1))
	tran67 = Transicion('', (0,1,0,0,1,0), (1,1,1,1,1,0))
	tran68 = Transicion('', (0,1,0,0,1,0), (1,1,1,0,1,1))
	tran69 = Transicion('', (0,1,0,0,1,0), (1,1,0,1,1,1))
	tran70 = Transicion('', (0,1,0,0,1,1), (1,1,1,1,1,1))
	tran71 = Transicion('', (0,1,0,1,0,0), (1,1,1,1,1,0))
	tran72 = Transicion('', (0,1,0,1,0,0), (1,1,1,1,0,1))
	tran73 = Transicion('', (0,1,0,1,0,0), (1,1,0,1,1,1))
	tran74 = Transicion('', (0,1,0,1,0,1), (1,1,1,1,1,1))
	tran75 = Transicion('', (0,1,0,1,1,0), (1,1,1,1,1,1))
	tran76 = Transicion('', (0,1,0,1,1,1), (1,1,1,1,1,1))
	tran77 = Transicion('', (0,1,1,0,0,0), (1,1,1,1,1,0))
	tran78 = Transicion('', (0,1,1,0,0,0), (1,1,1,1,0,1))
	tran79 = Transicion('', (0,1,1,0,0,0), (1,1,1,0,1,1))
	tran80 = Transicion('', (0,1,1,0,0,1), (1,1,1,1,1,1))
	tran81 = Transicion('', (0,1,1,0,1,0), (1,1,1,1,1,1))
	tran82 = Transicion('', (0,1,1,0,1,1), (1,1,1,1,1,1))
	tran83 = Transicion('', (0,1,1,1,0,0), (1,1,1,1,1,1))
	tran84 = Transicion('', (0,1,1,1,0,1), (1,1,1,1,1,1))
	tran85 = Transicion('', (0,1,1,1,1,0), (1,1,1,1,1,1))
	tran86 = Transicion('', (1,0,0,0,0,1), (0,0,0,0,0,0))
	tran87 = Transicion('', (1,0,0,0,1,0), (0,0,0,0,0,0))
	tran88 = Transicion('', (1,0,0,0,1,1), (0,0,0,0,0,1))
	tran89 = Transicion('', (1,0,0,0,1,1), (0,0,0,0,1,0))
	tran90 = Transicion('', (1,0,0,1,0,0), (0,0,0,0,0,0))
	tran91 = Transicion('', (1,0,0,1,0,1), (0,0,0,0,0,1))
	tran92 = Transicion('', (1,0,0,1,0,1), (0,0,0,1,0,0))
	tran93 = Transicion('', (1,0,0,1,1,0), (0,0,0,0,1,0))
	tran94 = Transicion('', (1,0,0,1,1,0), (0,0,0,1,0,0))
	tran95 = Transicion('', (1,0,0,1,1,1), (0,0,0,0,1,1))
	tran96 = Transicion('', (1,0,0,1,1,1), (0,0,0,1,0,1))
	tran97 = Transicion('', (1,0,0,1,1,1), (0,0,0,1,1,0))
	tran98 = Transicion('', (1,0,1,0,0,0), (0,0,0,0,0,0))
	tran99 = Transicion('', (1,0,1,0,0,1), (0,0,0,0,0,1))
	tran100 = Transicion('', (1,0,1,0,0,1), (0,0,1,0,0,0))
	tran101 = Transicion('', (1,0,1,0,1,0), (0,0,0,0,1,0))
	tran102 = Transicion('', (1,0,1,0,1,0), (0,0,1,0,0,0))
	tran103 = Transicion('', (1,0,1,0,1,1), (0,0,0,0,1,1))
	tran104 = Transicion('', (1,0,1,0,1,1), (0,0,1,0,0,1))
	tran105 = Transicion('', (1,0,1,0,1,1), (0,0,1,0,1,0))
	tran106 = Transicion('', (1,0,1,1,0,0), (0,0,1,0,0,0))
	tran107 = Transicion('', (1,0,1,1,0,0), (0,0,0,1,0,0))
	tran108 = Transicion('', (1,0,1,1,0,1), (0,0,0,1,0,1))
	tran109 = Transicion('', (1,0,1,1,0,1), (0,0,1,0,0,1))
	tran110 = Transicion('', (1,0,1,1,0,1), (0,0,1,1,0,0))
	tran111 = Transicion('', (1,0,1,1,1,0), (0,0,0,1,1,0))
	tran112 = Transicion('', (1,0,1,1,1,0), (0,0,1,0,1,0))
	tran113 = Transicion('', (1,0,1,1,1,0), (0,0,1,1,0,0))
	tran114 = Transicion('', (1,0,1,1,1,1), (0,0,0,1,1,1))
	tran115 = Transicion('', (1,0,1,1,1,1), (0,0,1,0,1,1))
	tran116 = Transicion('', (1,0,1,1,1,1), (0,0,1,1,0,1))
	tran117 = Transicion('', (1,0,1,1,1,1), (0,0,1,1,1,0))
	tran118 = Transicion('', (1,1,0,0,0,0), (0,0,0,0,0,0))
	tran119 = Transicion('', (1,1,0,0,0,1), (0,0,0,0,0,1))
	tran120 = Transicion('', (1,1,0,0,0,1), (0,1,0,0,0,0))
	tran121 = Transicion('', (1,1,0,0,1,0), (0,0,0,0,1,0))
	tran122 = Transicion('', (1,1,0,0,1,0), (0,1,0,0,0,0))
	tran123 = Transicion('', (1,1,0,0,1,1), (0,0,0,0,1,1))
	tran124 = Transicion('', (1,1,0,0,1,1), (0,1,0,0,0,1))
	tran125 = Transicion('', (1,1,0,0,1,1), (0,1,0,0,1,0))
	tran126 = Transicion('', (1,1,0,1,0,0), (0,0,0,1,0,0))
	tran127 = Transicion('', (1,1,0,1,0,0), (0,1,0,0,0,0))
	tran128 = Transicion('', (1,1,0,1,0,1), (0,0,0,1,0,1))
	tran129 = Transicion('', (1,1,0,1,0,1), (0,1,0,0,0,1))
	tran130 = Transicion('', (1,1,0,1,0,1), (0,1,0,1,0,0))
	tran131 = Transicion('', (1,1,0,1,1,1), (0,0,0,1,1,1))
	tran132 = Transicion('', (1,1,0,1,1,1), (0,1,0,0,1,1))
	tran133 = Transicion('', (1,1,0,1,1,1), (0,1,0,1,0,1))
	tran134 = Transicion('', (1,1,0,1,1,1), (0,1,0,1,1,0))
	tran135 = Transicion('', (1,1,1,0,0,0), (0,1,0,0,0,0))
	tran136 = Transicion('', (1,1,1,0,0,0), (0,0,1,0,0,0))
	tran137 = Transicion('', (1,1,1,0,0,1), (0,0,1,0,0,1))
	tran138 = Transicion('', (1,1,1,0,0,1), (0,1,0,0,0,1))
	tran139 = Transicion('', (1,1,1,0,0,1), (0,1,1,0,0,0))
	tran140 = Transicion('', (1,1,1,0,1,0), (0,0,1,0,1,0))
	tran141 = Transicion('', (1,1,1,0,1,0), (0,1,0,0,1,0))
	tran142 = Transicion('', (1,1,1,0,1,0), (0,1,1,0,0,0))
	tran143 = Transicion('', (1,1,1,0,1,1), (0,0,1,0,1,1))
	tran144 = Transicion('', (1,1,1,0,1,1), (0,1,0,0,1,1))
	tran145 = Transicion('', (1,1,1,0,1,1), (0,1,1,0,0,1))
	tran146 = Transicion('', (1,1,1,0,1,1), (0,1,1,0,1,0))
	tran147 = Transicion('', (1,1,1,1,0,0), (0,0,1,1,0,0))
	tran148 = Transicion('', (1,1,1,1,0,0), (0,1,1,0,0,0))
	tran149 = Transicion('', (1,1,1,1,0,0), (0,1,0,1,0,0))
	tran150 = Transicion('', (1,1,1,1,0,1), (0,0,1,1,0,1))
	tran151 = Transicion('', (1,1,1,1,0,1), (0,1,0,1,0,1))
	tran152 = Transicion('', (1,1,1,1,0,1), (0,1,1,0,0,1))
	tran153 = Transicion('', (1,1,1,1,0,1), (0,1,1,1,0,0))
	tran154 = Transicion('', (1,1,1,1,1,0), (0,0,1,1,1,0))
	tran155 = Transicion('', (1,1,1,1,1,0), (0,1,0,1,1,0))
	tran156 = Transicion('', (1,1,1,1,1,0), (0,1,1,0,1,0))
	tran157 = Transicion('', (1,1,1,1,1,0), (0,1,1,1,0,0))
	
	for i in range(1, 158):
		variable = 'tran' + str(i)
		familia.append(vars()[variable])
	
	return familia
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

caminoRana = [
				 ('BF5','BF4','BF3','BF2','BF1','V','GF1','GF2','GF3','GF4','GF5'),
				 ('BF5','BF4','BF3','BF2','V','BF1','GF1','GF2','GF3','GF4','GF5'),
				 ('BF5','BF4','BF3','BF2','GF1','BF1','V','GF2','GF3','GF4','GF5'),
				 ('BF5','BF4','BF3','BF2','GF1','BF1','GF2','V','GF3','GF4','GF5'),
				 ('BF5','BF4','BF3','BF2','GF1','V','GF2','BF1','GF3','GF4','GF5'),
				 ('BF5','BF4','BF3','V','GF1','BF2','GF2','BF1','GF3','GF4','GF5'),
				 ('BF5','BF4','V','BF3','GF1','BF2','GF2','BF1','GF3','GF4','GF5'),
				 ('BF5','BF4','GF1','BF3','V','BF2','GF2','BF1','GF3','GF4','GF5'),
				 ('BF5','BF4','GF1','BF3','GF2','BF2','V','BF1','GF3','GF4','GF5'),
				 ('BF5','BF4','GF1','BF3','GF2','BF2','GF3','BF1','V','GF4','GF5'),
				 ('BF5','BF4','GF1','BF3','GF2','BF2','GF3','BF1','GF4','V','GF5'),
				 ('BF5','BF4','GF1','BF3','GF2','BF2','GF3','V','GF4','BF1','GF5'),
				 ('BF5','BF4','GF1','BF3','GF2','V','GF3','BF2','GF4','BF1','GF5'),
				 ('BF5','BF4','GF1','V','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),
				 ('BF5','V','GF1','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),
				 ('V','BF5','GF1','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),
				 ('GF1','BF5','V','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),
				 ('GF1','BF5','GF2','BF4','V','BF3','GF3','BF2','GF4','BF1','GF5'),
				 ('GF1','BF5','GF2','BF4','GF3','BF3','V','BF2','GF4','BF1','GF5'),
				 ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','V','BF1','GF5'),
				 ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','GF5','BF1','V'),
				 ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','GF5','V','BF1'),
				 ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','V','GF5','BF2','BF1'),
				 ('GF1','BF5','GF2','BF4','GF3','V','GF4','BF3','GF5','BF2','BF1'),
				 ('GF1','BF5','GF2','V','GF3','BF4','GF4','BF3','GF5','BF2','BF1'),
				 ('GF1','V','GF2','BF5','GF3','BF4','GF4','BF3','GF5','BF2','BF1'),
				 ('GF1','GF2','V','BF5','GF3','BF4','GF4','BF3','GF5','BF2','BF1'),
				 ('GF1','GF2','GF3','BF5','V','BF4','GF4','BF3','GF5','BF2','BF1'),
				 ('GF1','GF2','GF3','BF5','GF4','BF4','V','BF3','GF5','BF2','BF1'),
				 ('GF1','GF2','GF3','BF5','GF4','BF4','GF5','BF3','V','BF2','BF1'),
				 ('GF1','GF2','GF3','BF5','GF4','BF4','GF5','V','BF3','BF2','BF1'),
				 ('GF1','GF2','GF3','BF5','GF4','V','GF5','BF4','BF3','BF2','BF1'),
				 ('GF1','GF2','GF3','V','GF4','BF5','GF5','BF4','BF3','BF2','BF1'),
				 ('GF1','GF2','GF3','GF4','V','BF5','GF5','BF4','BF3','BF2','BF1'),
				 ('GF1','GF2','GF3','GF4','GF5','BF5','V','BF4','BF3','BF2','BF1'),
				 ('GF1','GF2','GF3','GF4','GF5','V','BF5','BF4','BF3','BF2','BF1')
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
	solucionFamilia = []

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
	solucionOveja = []

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


def rana():
	solucionRana = []

	tran1=Transicion('Salto rana azul Nº1', ('BF5','BF4','BF3','BF2','BF1','V','GF1','GF2','GF3','GF4','GF5'),('BF5','BF4','BF3','BF2','V','BF1','GF1','GF2','GF3','GF4','GF5'))
	tran2=Transicion('Salto rana verde Nº1', ('BF5','BF4','BF3','BF2','V','BF1','GF1','GF2','GF3','GF4','GF5'),('BF5','BF4','BF3','BF2','GF1','BF1','V','GF2','GF3','GF4','GF5'))
	tran3=Transicion('Salto rana verde Nº2', ('BF5','BF4','BF3','BF2','GF1','BF1','V','GF2','GF3','GF4','GF5'),('BF5','BF4','BF3','BF2','GF1','BF1','GF2','V','GF3','GF4','GF5'))
	tran4=Transicion('Salto rana azul Nº1', ('BF5','BF4','BF3','BF2','GF1','BF1','GF2','V','GF3','GF4','GF5'),('BF5','BF4','BF3','BF2','GF1','V','GF2','BF1','GF3','GF4','GF5'))
	tran5=Transicion('Salto rana azul Nº2', ('BF5','BF4','BF3','BF2','GF1','V','GF2','BF1','GF3','GF4','GF5'),('BF5','BF4','BF3','V','GF1','BF2','GF2','BF1','GF3','GF4','GF5'))
	tran6=Transicion('Salto rana azul Nº3', ('BF5','BF4','BF3','V','GF1','BF2','GF2','BF1','GF3','GF4','GF5'),('BF5','BF4','V','BF3','GF1','BF2','GF2','BF1','GF3','GF4','GF5'))
	tran7=Transicion('Salto rana verde Nº1', ('BF5','BF4','V','BF3','GF1','BF2','GF2','BF1','GF3','GF4','GF5'),('BF5','BF4','GF1','BF3','V','BF2','GF2','BF1','GF3','GF4','GF5'))
	tran8=Transicion('Salto rana verde Nº2', ('BF5','BF4','GF1','BF3','V','BF2','GF2','BF1','GF3','GF4','GF5'),('BF5','BF4','GF1','BF3','GF2','BF2','V','BF1','GF3','GF4','GF5'))
	tran9=Transicion('Salto rana verde Nº3', ('BF5','BF4','GF1','BF3','GF2','BF2','V','BF1','GF3','GF4','GF5'),('BF5','BF4','GF1','BF3','GF2','BF2','GF3','BF1','V','GF4','GF5'))
	tran10=Transicion('Salto rana verde Nº4', ('BF5','BF4','GF1','BF3','GF2','BF2','GF3','BF1','V','GF4','GF5'),('BF5','BF4','GF1','BF3','GF2','BF2','GF3','BF1','GF4','V','GF5'))
	tran11=Transicion('Salto rana azul Nº1', ('BF5','BF4','GF1','BF3','GF2','BF2','GF3','BF1','GF4','V','GF5'),('BF5','BF4','GF1','BF3','GF2','BF2','GF3','V','GF4','BF1','GF5'))
	tran12=Transicion('Salto rana azul Nº2', ('BF5','BF4','GF1','BF3','GF2','BF2','GF3','V','GF4','BF1','GF5'),('BF5','BF4','GF1','BF3','GF2','V','GF3','BF2','GF4','BF1','GF5'))
	tran13=Transicion('Salto rana azul Nº3', ('BF5','BF4','GF1','BF3','GF2','V','GF3','BF2','GF4','BF1','GF5'),('BF5','BF4','GF1','V','GF2','BF3','GF3','BF2','GF4','BF1','GF5'))
	tran14=Transicion('Salto rana azul Nº4', ('BF5','BF4','GF1','V','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),('BF5','V','GF1','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'))
	tran15=Transicion('Salto rana azul Nº5', ('BF5','V','GF1','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),('V','BF5','GF1','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'))
	tran16=Transicion('Salto rana verde Nº1', ('V','BF5','GF1','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),('GF1','BF5','V','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'))
	tran17=Transicion('Salto rana verde Nº2', ('GF1','BF5','V','BF4','GF2','BF3','GF3','BF2','GF4','BF1','GF5'),('GF1','BF5','GF2','BF4','V','BF3','GF3','BF2','GF4','BF1','GF5'))
	tran18=Transicion('Salto rana verde Nº3', ('GF1','BF5','GF2','BF4','V','BF3','GF3','BF2','GF4','BF1','GF5'),('GF1','BF5','GF2','BF4','GF3','BF3','V','BF2','GF4','BF1','GF5'))
	tran19=Transicion('Salto rana verde Nº4', ('GF1','BF5','GF2','BF4','GF3','BF3','V','BF2','GF4','BF1','GF5'),('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','V','BF1','GF5'))
	tran20=Transicion('Salto rana verde Nº5', ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','V','BF1','GF5'),('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','GF5','BF1','V'))
	tran21=Transicion('Salto rana azul Nº1', ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','GF5','BF1','V'),('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','GF5','V','BF1'))
	tran22=Transicion('Salto rana azul Nº2', ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','BF2','GF5','V','BF1'),('GF1','BF5','GF2','BF4','GF3','BF3','GF4','V','GF5','BF2','BF1'))
	tran23=Transicion('Salto rana azul Nº3', ('GF1','BF5','GF2','BF4','GF3','BF3','GF4','V','GF5','BF2','BF1'),('GF1','BF5','GF2','BF4','GF3','V','GF4','BF3','GF5','BF2','BF1'))
	tran24=Transicion('Salto rana azul Nº4', ('GF1','BF5','GF2','BF4','GF3','V','GF4','BF3','GF5','BF2','BF1'),('GF1','BF5','GF2','V','GF3','BF4','GF4','BF3','GF5','BF2','BF1'))
	tran25=Transicion('Salto rana azul Nº5', ('GF1','BF5','GF2','V','GF3','BF4','GF4','BF3','GF5','BF2','BF1'),('GF1','V','GF2','BF5','GF3','BF4','GF4','BF3','GF5','BF2','BF1'))
	tran26=Transicion('Salto rana verde Nº2', ('GF1','V','GF2','BF5','GF3','BF4','GF4','BF3','GF5','BF2','BF1'),('GF1','GF2','V','BF5','GF3','BF4','GF4','BF3','GF5','BF2','BF1'))
	tran27=Transicion('Salto rana verde Nº3', ('GF1','GF2','V','BF5','GF3','BF4','GF4','BF3','GF5','BF2','BF1'),('GF1','GF2','GF3','BF5','V','BF4','GF4','BF3','GF5','BF2','BF1'))
	tran28=Transicion('Salto rana verde Nº4', ('GF1','GF2','GF3','BF5','V','BF4','GF4','BF3','GF5','BF2','BF1'),('GF1','GF2','GF3','BF5','GF4','BF4','V','BF3','GF5','BF2','BF1'))
	tran29=Transicion('Salto rana verde Nº5', ('GF1','GF2','GF3','BF5','GF4','BF4','V','BF3','GF5','BF2','BF1'),('GF1','GF2','GF3','BF5','GF4','BF4','GF5','BF3','V','BF2','BF1'))
	tran30=Transicion('Salto rana azul Nº3', ('GF1','GF2','GF3','BF5','GF4','BF4','GF5','BF3','V','BF2','BF1'),('GF1','GF2','GF3','BF5','GF4','BF4','GF5','V','BF3','BF2','BF1'))
	tran31=Transicion('Salto rana azul Nº4', ('GF1','GF2','GF3','BF5','GF4','BF4','GF5','V','BF3','BF2','BF1'),('GF1','GF2','GF3','BF5','GF4','V','GF5','BF4','BF3','BF2','BF1'))
	tran32=Transicion('Salto rana azul Nº5', ('GF1','GF2','GF3','BF5','GF4','V','GF5','BF4','BF3','BF2','BF1'),('GF1','GF2','GF3','V','GF4','BF5','GF5','BF4','BF3','BF2','BF1'))
	tran33=Transicion('Salto rana verde Nº4', ('GF1','GF2','GF3','V','GF4','BF5','GF5','BF4','BF3','BF2','BF1'),('GF1','GF2','GF3','GF4','V','BF5','GF5','BF4','BF3','BF2','BF1'))
	tran34=Transicion('Salto rana verde Nº5', ('GF1','GF2','GF3','GF4','V','BF5','GF5','BF4','BF3','BF2','BF1'),('GF1','GF2','GF3','GF4','GF5','BF5','V','BF4','BF3','BF2','BF1'))
	tran35=Transicion('Salto rana azul Nº5', ('GF1','GF2','GF3','GF4','GF5','BF5','V','BF4','BF3','BF2','BF1'),('GF1','GF2','GF3','GF4','GF5','V','BF5','BF4','BF3','BF2','BF1'))
	
	for i in range(1, 36):
		variable = 'tran' + str(i)
		solucionRana.append(vars()[variable])

	return solucionRana
