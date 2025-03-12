import random
import string

def generar_contrasena():
    try:
        longitud = int(input("Ingrese la longitud mínima de la contraseña (mínimo 8): "))
    except Exception as e:
        print("Debe ingresar un número válido.", e)
        return

    if longitud < 8:
        print("La longitud mínima es de 8 caracteres.")
        return

    # incluir al menos una letra mayúscula, un dígito y un carácter especial
    mayuscula = random.choice(string.ascii_uppercase)
    digito = random.choice(string.digits)
    especial = random.choice(string.punctuation)
    # el resto de la contraseña
    resto = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud - 3))

    # aqui mezclamos todo
    contrasena_lista = list(mayuscula + digito + especial + resto)
    random.shuffle(contrasena_lista)
    contrasena = ''.join(contrasena_lista)
    print("Contraseña generada:", contrasena)

    if __name__ == "__main__":
        generar_contrasena()
        
# python contrasena.py