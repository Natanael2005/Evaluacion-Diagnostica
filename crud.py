usuarios = []
next_id = 1

def agregar_usuario():
    global next_id
    nombre = input("Ingrese el nombre de el usuario: ")
    try:
        edad = int(input("Ingrese la edad: "))
    except Exception as e:
        print("Edad inválida.", e)
        return
    contrasena = input("Ingrese la contraseña: ")
    usuario = {"id": next_id, "nombre": nombre, "edad": edad, "contrasena": contrasena}
    usuarios.append(usuario)
    next_id += 1
    print("Usuario agregado.")
    listar_usuarios()

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("Lista de usuarios:")
    for usuario in usuarios:
        print(usuario)

def editar_usuario():
    try:
        uid = int(input("Ingrese el ID del usuario a editar: "))
    except Exception as e:
        print("ID inválido.", e)
        return
    for usuario in usuarios:
        if usuario["id"] == uid:
            usuario["nombre"] = input("Nuevo nombre de usuario: ")
            try:
                usuario["edad"] = int(input("Nueva edad: "))
            except Exception as e:
                print("Edad inválida.", e)
                return
            usuario["contrasena"] = input("Nueva contraseña: ")
            print("Usuario actualizado.")
            listar_usuarios()
            return
    print("Usuario no encontrado.")

def eliminar_usuario():
    try:
        uid = int(input("Ingrese el ID del usuario a eliminar: "))
    except Exception as e:
        print("ID inválido.", e)
        return
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != uid]
    print("Usuario eliminado (si existía).")
    listar_usuarios()

def crud_usuarios():
    while True:
        print("\n--- Menú CRUD de Usuarios ---")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("5. Salir del CRUD")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            editar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    crud_usuarios()

# python crud.py