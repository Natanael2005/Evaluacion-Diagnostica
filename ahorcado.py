import random

def juego_ahorcado():
    # Lista de palabras y selección aleatoria
    palabras = ["python", "programacion", "desarrollador", "computadora", "teclado"]
    palabra_oculta = random.choice(palabras)
    
    # Inicializar estado del juego
    letras_adivinadas = ["_"] * len(palabra_oculta)
    errores = 0
    max_errores = 5

    print("¡Bienvenido al juego del Ahorcado!")
    while errores < max_errores and "_" in letras_adivinadas:
        print("\nPalabra:", " ".join(letras_adivinadas))
        letra = input("Ingresa una letra: ").lower()

        # Verificar que solo se ponga una letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        # Actualizar estado del juego
        if letra in palabra_oculta:
            for idx, char in enumerate(palabra_oculta):
                if char == letra:
                    letras_adivinadas[idx] = letra
            print("¡Correcto!")
        else:
            errores += 1
            print(f"Incorrecto. Errores: {errores}/{max_errores}")

    # Mostrar resultado 
    if "_" not in letras_adivinadas:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_oculta)
    else:
        print("\nHas perdido. La palabra era:", palabra_oculta)

if __name__ == "__main__":
    juego_ahorcado()

# python ahorcado.py

