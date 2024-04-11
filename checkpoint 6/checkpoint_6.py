class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        
super_usuario = Usuario("nanoprogr","jjj333rrr999")
print("Nombre de usuario:", super_usuario.usuario)
print("Contraseña:", super_usuario.contraseña)
