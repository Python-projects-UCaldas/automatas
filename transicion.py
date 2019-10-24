class Transicion:
	def __init__(self, nombre,origen,destino):
		self.nombre=nombre
		self.origen=origen
		self.destino=destino

	def getNombre(self):
		return self.nombre

	def getOrigen(self):
		return self.origen

	def getDestino(self):
		return self.destino
