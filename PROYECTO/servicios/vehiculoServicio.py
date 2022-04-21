# Importa el directorio alquilaya_entidades


from entidades.vehiculo import Vehiculo
# Importa desde el modulo vehiculo la clase Vehiculo


class VehiculoServicio():
    '''
        Función que valida que una cadena no este vacia.
        Retorna un String.
    '''

    def validarString(self, msj):
        while True:
            cadena = input(msj)
            if (not cadena):
                print("Error!")
            else:
                break
        return cadena
    '''
        Función que valida que un número entero sea positivo.
        Retorna un int.
    '''

    def validarInt(self, msj):
        while True:
            nroEntero = int(input(msj))
            if (nroEntero <= 0):
                print("Error!")
            else:
                break
        return nroEntero
    '''
        Función que valida que un número decimal sea positivo.
        Retorna un float.
    '''

    def validarFloat(self, msj):
        while True:
            nroDecimal = float(input(msj))
            if (nroDecimal <= 0.0):
                print("Error!")
            else:
                break
        return nroDecimal
    '''
        Función que valida que una cadena sea del tipo "AAA 111" o "AA 111 AA".
        Retorna un String.
    '''

    def validarMatricula(self, msj):
        vs = VehiculoServicio()
        band = False
        while True:
            cadena = vs.validarString(msj)
            if (len(cadena) == 6):
                band = True
            elif(len(cadena) == 7):
                band = True
            if(band):
                break
        return cadena
    '''
        Función que crea un objeto de tipo Vehiculo, llamando a las funciones
        que validan sus atributos.
        Retorna un Vehiculo.
    '''

    def crearVehiculo(self):
        vs = VehiculoServicio()
        tipo = vs.validarString("Ingrese el tipo: ")
        marca = vs.validarString("Ingrese la marca: ")
        modelo = vs.validarString("Ingrese el modelo: ")
        modeloAnio = vs.validarInt("Ingrese el año del vehiculo: ")
        matricula = vs.validarMatricula("Ingrese la matricula: ")
        km = vs.validarFloat("Ingrese los km del vehiculo: ")
        precio = vs.validarFloat("Ingrese el precio del vehiculo: ")
        return Vehiculo(tipo, marca, modelo, modeloAnio, matricula, km, precio)
        print(Vehiculo)
