# atributos de clase: le pertenecen a la misma clase

class Usuario:
    #attr de clase
    username = 'Username por default'
    email = ''

Usuario.username='User01'
Usuario.email='test@test.com'

noah = Usuario()
print(Usuario.username)
print(Usuario.email)