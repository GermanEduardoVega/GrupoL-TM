from entidades.usuario import Usuario
# Importa desde el modulo vehiculo la clase Vehiculo


class UsuarioServicio():
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

    def validarFecha(self, msj):

        while True:
            nroEntero = int(input(msj))
            if (nroEntero <= 0):
                print("Error!")
            else:
                break
        return nroEntero
        '''
        Función que crea un objeto de tipo Vehiculo, llamando a las funciones
        que validan sus atributos.
        Retorna un Vehiculo.
        '''

    def crearUsuario(self):
        us = UsuarioServicio()
        nombre = us.validarString("Ingrese el nombre: ")
        apellido = us.validarString("Ingrese el apellido: ")
        # cuil = us.validarInt("Ingrese el CUIL: ")
        # carnetConducir = us.validarInt("Ingrese el carnet de conducir: ")
        fechaNacimiento = us.validarFecha("Ingrese fecha:")

        return Usuario(nombre, apellido,
                       fechaNacimiento)
        print(Usuario)
