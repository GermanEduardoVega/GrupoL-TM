class Usuario():

    # Constructor
    def __init__(self, nombre, apellido,
                 fechaNacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        # self.__cuil = cuil
        # self.__carnetConducir = carnetConducir

    # Getters (Métodos get)

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

        '''
    def getCuil(self):
        return self.__cuil

    def getCarnetConducir(self):
        return self.__carnetConducir
        '''

    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    # Setters (Métodos set)

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setCuil(self, cuil):
        self.__cuil = cuil

    def setCarnetConducir(self, carnetConducir):
        self.__carnetConducir = carnetConducir

    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento
