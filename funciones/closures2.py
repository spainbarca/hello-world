def saludar(username):
    mensaje = f'Hola {username}' # Variable local

    def mostrar_mensaje(): # Anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Noah'
respuesta = saludar(username)

username = 'Troll'

respuesta()