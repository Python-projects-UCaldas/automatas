import sys, os, time, itertools, pygame
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic, QtCore, Qt
#from grafo import *
from transicion import *
from pygame.locals import *

global lista
global dictEstados
global Grafo
dictEstados = {}
lista = []

class Ventana(QMainWindow):
	
	def __init__(self):
	
		#iniciar pbjeto QMainWindow
		QMainWindow.__init__(self)
		#Cargar archivo
		uic.loadUi("VentanaMain.ui",self)
		
		self.initUI()


	def initUI(self):
		self.btAgregarTransicion.clicked.connect(
			lambda: self.generarTransicion(self.txtNombreT.text(), self.nombreVresultado.text(), 
				self.valorVresultado.text(), self.txtCondicion.text()))
		self.btFin.clicked.connect(lambda: self.generarArchivo(dictEstados))
		self.btAgregEstados.clicked.connect(lambda: self.agregarEstado())
		self.btFin.clicked.connect(lambda: self.dibujar())

	def generarTransicion(self, nombre, origen, destino, condicion):
		nueva = Transicion(nombre, origen, destino, condicion)
		lista.append(nueva)

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
		nx.draw_shell(Grafo, with_labels=True, node_color='pink', font_size= 5, node_size=500)
		plt.savefig('graph.png',dpi=(140))#transparent=True, facecolor="w"
		plt.clf()

	def generarArchivo(self, dictEstados):
		file = open("condicionales.py", "a")
		file.write('dictEstados = ')
		file.write(str(dictEstados))
		file.write('\n')
		file.write('	')
		for x in lista:
			file.write('if ' + x.getCondicion() + ':')
			file.write('\n')
			file.write('	')
			file.write('	')
			file.write('dictEstados[\'' + x.getOrigen() + '\']' + ' = ' + x.getDestino())
			file.write('\n')
			file.write('	')
		file.close()

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
		            if event.key == K_a:
		                draw_edges()
		            elif event.key == K_d:
		                delete_edges()
		    pygame.display.update()
#Iniciar Aplicacion
app=QApplication(sys.argv)
#Crear objeto clase
_ventana=Ventana() 
#Mostrar ventana
_ventana.show()
app.exec_() 
