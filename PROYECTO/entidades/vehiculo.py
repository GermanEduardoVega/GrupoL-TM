class Vehiculo():
    # Constructor
    def __init__(self, tipo, marca, modelo, modeloAnio, matricula, km, precio):
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__modeloAnio = modeloAnio
        self.__matricula = matricula
        self.__km = km
        self.__precio = precio
    # Getters (Métodos get)

    def getTipo(self):
        return self.__tipo

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getModeloAnio(self):
        return self.__modeloAnio

    def getMatricula(self):
        return self.__matricula

    def getKm(self):
        return self.__km

    def getPrecio(self):
        return self.__precio
    # Setters (Métodos set)

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setModeloAnio(self, modeloAnio):
        self.__modeloAnio = modeloAnio

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def serKm(self, km):
        self.__km = km

    def setPrecio(self, precio):
        self.__precio = precio
