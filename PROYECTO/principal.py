from servicios.vehiculoServicio import VehiculoServicio
from servicios.usuarioServicio import UsuarioServicio

vs = VehiculoServicio()
v1 = vs.crearVehiculo()
print(v1.getTipo())
print(v1.getMarca())
print(v1.getModelo())
print(v1.getModeloAnio())
print(v1.getMatricula())
print(v1.getKm())
print(v1.getPrecio())

us = UsuarioServicio()
u1 = us.crearUsuario()
print(u1.getNombre())
print(u1.getApellido())
# print(u1.getCuil())
# print(u1.getCarnetConducir())
print(u1.getFechaNacimiento())
