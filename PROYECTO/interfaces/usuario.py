class Usuario:
    def __init__ (self, _nombre, _pasaporte, _cuil, _licencia, _edad, _foto):
        self._nombre = _nombre
        self._pasaporte = _pasaporte
        self._cuil = _cuil
        self._licencia = _licencia
        self._edad = _edad
        self._foto = _foto


    def get_nombre(self):
        return self._nombre

    def get_pasaporte(self):
        return self._pasaporte

    def get_cuil(self):
        return self._cuil

    def get_licencia(self):
        return self._licencia

    def get_edad(self):
        return self._edad

    def get_foto(self):
        return self._foto


    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

    def set_pasaporte(self, new_pasaporte):
        self._pasaporte = new_pasaporte

    def set_cuil(self, new_cuil):
        self._cuil = new_cuil

    def set_licencia(self, new_licencia):
        self._licencia = new_licencia

    def set_edad(self, new_edad):
        self._edad = new_edad

    def set_foto(self, new_foto):
        self._foto = new_foto
