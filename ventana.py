import sys, os, time, itertools, pygame
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic, QtCore, Qt
from optimo import *
from transicion import *
from pygame.locals import *

global lista
global dictEstados
global Grafo
global camino
dictEstados = {}
lista = []
Grafo = nx.DiGraph()

class Ventana(QMainWindow):
	
	def __init__(self):
	
		#iniciar pbjeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar archivo
		uic.loadUi("VentanaMain.ui",self)
		
		self.initUI()


	def initUI(self):
		self.btFin.clicked.connect(lambda:self.dibujar())
		self.btAgregEstados.clicked.connect(lambda: self.agregarEstado())
		self.btEstadoInicial.clicked.connect(lambda: self.estadoInicial.setText('Usted ha ingresado el' +
			' estado inicial: ' + self.txtInicial.text()))
		self.btEstadoAceptacion.clicked.connect(lambda: self.eAceptacion.setText('Usted ha ingresado el' +
			' estado de aceptación: ' + self.txtAceptacion.text()))
		self.btAgregarTransicion.clicked.connect(lambda: self.transicion.setText('Usted ha ingresado el' +
			' la transición: ' + self.txtNombreT.text() + ' con la condición: ' + self.txtCondicion.text()))

	def agregarEstado(self):
		listaDiccionario = []
		listaEstados = []
		n = 0
		for i in range(0,(int(self.rango.text()) + 1)):
			listaDiccionario.append(n)
			n += 1
		dictEstados[self.nombreVariable.text()] = listaDiccionario
		for combo in itertools.product(*[dictEstados[k] for k in sorted(dictEstados.keys())]):
			listaEstados.append(combo)
		Grafo = nx.DiGraph()
		for i in listaEstados:
			Grafo.add_node(i)
		if (len(listaEstados[0]) == 4):
			lista = grafOveja()
			for i in lista:
				Grafo.add_edge(i.getOrigen(), i.getDestino())
		elif (len(listaEstados[0]) == 3):
			lista = grafoCanival()
			for i in lista:
				Grafo.add_edge(i.getOrigen(), i.getDestino())
		#elif (len(listaEstados[0]) == 6):
			#lista = grafoFamilia()	
			# for i in lista:
			# 	Grafo.add_edge(i.getOrigen(), i.getDestino())
		nx.draw_shell(Grafo, with_labels=True, node_color='red', font_size= 5, node_size=500)
		plt.savefig('graph.png',dpi=(140))#transparent=True, facecolor="w"
		plt.clf()


	# def generarArchivo(self, dictEstados):
	# 	file = open("condicionales.py", "a")
	# 	file.write('dictEstados = ')
	# 	file.write(str(dictEstados))
	# 	file.write('\n')
	# 	file.write('	')
	# 	for x in lista:
	# 		file.write('if ' + x.getCondicion() + ':')
	# 		file.write('\n')
	# 		file.write('	')
	# 		file.write('	')
	# 		file.write('dictEstados[\'' + x.getOrigen() + '\']' + ' = ' + x.getDestino())
	# 		file.write('\n')
	# 		file.write('	')
	# 	file.close()

	def dibujarAristas(self,lista):
		camino = []
		listaDiccionario = []
		listaEstados = []
		n = 0
		for i in range(0,(int(self.rango.text()) + 1)):
			listaDiccionario.append(n)
			n += 1
		dictEstados[self.nombreVariable.text()] = listaDiccionario
		for combo in itertools.product(*[dictEstados[k] for k in sorted(dictEstados.keys())]):
			listaEstados.append(combo)
		Grafo = nx.DiGraph()
		for i in listaEstados:
			Grafo.add_node(i)
		for i in lista:
			Grafo.add_edge(i.getOrigen(), i.getDestino())
			camino.append('Desde el vertice: ' + str(i.getOrigen()) + ' Hasta el vertice: ' + str(i.getDestino()) +
				' con la transición: ' + i.getNombre() + '         ')
			time.sleep(1)
			nx.draw_networkx_edge_labels(Grafo,{i.getOrigen(): ([0, 0.6]), i.getDestino(): ([0, 0.6])}, 
				edge_labels={(i.getOrigen(),i.getDestino()):i.getNombre()},font_color='red')
			nx.draw_circular(Grafo, with_labels=True, node_color='red', font_size= 5, node_size=500)
			plt.savefig('graph.png',dpi=(140))#transparent=True, facecolor="w"
			plt.clf()
			pygame.init()
			window = pygame.display.set_mode((896,672))
			pygame.display.set_caption("Grafo completo")
			My_image = pygame.image.load("graph.png")
			window.blit(My_image,(0,0))
			pygame.display.update()
			plt.clf()
		
		self.mostraCamino(camino)
		
	def mostraCamino(self,lista):
		n = 1
		for i in lista:
			self.caminoSolucion.append(str(n) + ' -> ' + str(i))
			n += 1

	def dibujar(self):
		pygame.init()
		window = pygame.display.set_mode((896,672))
		pygame.display.set_caption("Grafo completo")
		My_image = pygame.image.load("graph.png")
		window.blit(My_image,(0,0))
		pygame.display.update()
		plt.clf()

		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            pygame.quit()
		            sys.exit()
		        elif event.type == pygame.KEYDOWN:
		            if event.key == K_k:
		            	lista = canibal()
		            	self.dibujarAristas(lista)
		            elif event.key == K_f:
		                lista = familia()
		                self.dibujarAristas(lista)
		            elif event.key == K_o:
		            	lista = oveja()
		            	self.dibujarAristas(lista)
		            elif event.key == K_r:
		            	pass
		    pygame.display.update()
#Iniciar Aplicacion
app=QApplication(sys.argv)
#Crear objeto clase
_ventana=Ventana() 
#Mostrar ventana
_ventana.show()
app.exec_() 
