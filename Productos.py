class Productos:
    def __init__(self,nombre,precio,cantidad,total):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.total = total
   
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    
    def getTotal(self):
        return self.total

    def setNombre(self, nombre):
        self.name = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def setTotal(self,total):
        self.total = total
    
    