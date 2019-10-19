import sys, os, time
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic, QtCore, Qt
#from grafo import *
from transicion import *
#from pygame.locals import *

global lista
global dictEstados
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
		#self.btAgregarTransicion.clicked.connect(lambda: self.agregarTransicion())
   		# self.btEstadoInicial.clicked.connect(lambda: self.agregarInicial(self.guardarVariables()))
   		# self.btEstadoAceptacion.clicked.connect(lambda: self.estadosAceptacion())
   		# self.btFin.clicked.connect(lambda: self.dibujar())

	def agregarEstado(self):
   		dictEstados[self.nombreVariable.text()] = int(self.valorIni.text())
   		print(dictEstados)
	
	def generarTransicion(self, nombre, origen, destino, condicion):
		nueva = Transicion(nombre, origen, destino, condicion)
		lista.append(nueva)

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
#Iniciar Aplicacion
app=QApplication(sys.argv)
#Crear objeto clase
_ventana=Ventana() 
#Mostrar ventana
_ventana.show()
app.exec_() 
