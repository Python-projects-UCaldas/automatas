class Transicion:
	def __init__(self, nombre,origen,destino,condicion):
		self.nombre=nombre
		self.origen=origen
		self.destino=destino
		self.condicion=condicion

	def getNombre(self):
		return self.nombre

	def getOrigen(self):
		return self.origen

	def getDestino(self):
		return self.destino

	def getCondicion(self):
		return self.condicion
