def validar_palindromo():
    palabra = input("Ingresa una palabra: ").strip().lower()
    if palabra == palabra[::-1]:
        print("La palabra es un palíndromo (válido).")
    else:
        print("La palabra no es un palíndromo (inválido).")

if __name__ == "__main__":
    validar_palindromo()

# python palindromo.py