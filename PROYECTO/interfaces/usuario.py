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

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre




usuario = Usuario('ARAYA ALEJO', 25342534, 20-42749595-8, '123ads24213', 21,"FOTO")



print(usuario.get_nombre())
