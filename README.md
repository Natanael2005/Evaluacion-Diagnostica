# Proyecto Evaluación Diagnóstica - Ozelot Technologies

Este repositorio contiene los algoritmos solicitados en la evaluación diagnóstica. Se muestra el pseudocódigo de cada módulo para explicar la lógica del programa.

## Contenido del Proyecto

- [Palíndromo](#palíndromo)
- [Edad](#edad)
- [Contraseña](#contraseña)
- [Ahorcado](#ahorcado)
- [Fibonacci](#fibonacci)
- [CRUD de Usuarios](#crud-de-usuarios)

---

## Palíndromo

```plaintext
FUNCION ValidarPalindromo:
    LEER "Ingresa una palabra:" -> palabra
    palabra <- Quitar Espacios(palabra) y Convertir a Minúsculas(palabra)
    SI palabra es Igual a Invertir(palabra) Entonces:
         IMPRIMIR "La palabra es un palíndromo (válido)."
    SI NO:
         IMPRIMIR "La palabra no es un palíndromo (inválido)."
FIN FUNCION

INICIAR:
    LLAMAR ValidarPalindromo
 ```

## Edad

```plaintext

FUNCION CalcularEdad:
    IMPRIMIR "Ingrese su fecha de nacimiento:"
    LEER "Año (ej: 1990):" -> anio
    LEER "Mes (1-12):" -> mes
    LEER "Día (1-31):" -> dia
    LEER "Hora (0-23):" -> hora

    fechaNacimiento <- Crear Fecha(anio, mes, dia, hora)
    fechaActual <- Fecha Actual()

    SI fechaNacimiento > fechaActual Entonces:
         Imprimir "La fecha de nacimiento es en el futuro."
         Terminar
    FIN SI

    diferencia <- fechaActual - fechaNacimiento
    años <- diferencia.dias Dividido Por 365
    meses <- diferencia.dias Dividido Por 30
    semanas <- diferencia.dias Dividido Por 7
    dias <- diferencia.dias
    horas <- (diferencia.dias * 24) + (diferencia.segundos Dividido Por 3600)

    IMPRIMIR "Edad aproximada:"
    IMPRIMIR "Años:", años
    IMPRIMIR "Meses:", meses
    IMPRIMIR "Semanas:", semanas
    IMPRIMIR "Días:", dias
    IMPRIMIR "Horas:", horas
FIN FUNCION

INICIAR:
    LLAMAR CalcularEdad
```

## Contraseña

```plaintext


FUNCION GenerarContrasena:
    LEER "Ingrese la longitud mínima de la contraseña (mínimo 8):" -> longitud
    SI longitud < 8 Entonces:
         IMPRIMIR "La longitud mínima es de 8 caracteres."
         TERMINAR
    FIN SI

    mayuscula <- Elegir Aleatoriamente(un_caracter_de "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digito    <- Elegir Aleatoriamente(un_caracter_de "0123456789")
    especial  <- Elegir Aleatoriamente(un_caracter_de "!@#$%^&*()-_=+[]{};:,.<>?/~`|")

    resto <- CADENA VACIA
    Para i Desde 1 hasta (longitud - 3) HACER:
         caracterAleatorio <- Elegir Aleatoriamente(un_caracter_de "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:,.<>?/~`|")
         CONCATENAR caracterAleatorio A resto
    FIN PARA

    contrasena <- Concatenar(mayuscula, digito, especial, resto)
    contrasena <- Mezclar los caracteres (contrasena)
    IMPRIMIR "Contraseña generada:", contrasena
FIN FUNCION

INICIAR:
    LLAMAR GenerarContrasena

```
## Ahorcado
```plaintext
FUNCION JuegoAhorcado:
    palabras <- ["python", "programacion", "desarrollador", "computadora", "teclado"]
    palabraOculta <- Elegir Aleatoriamente(palabras)
    letrasAdivinadas <- Lista de tamaño (Longitud de(palabraOculta)) con valor "_"
    errores <- 0
    maxErrores <- 5

    IMPRIMIR "¡Bienvenido al juego del Ahorcado!"

    MIENTRAS (errores < maxErrores) Y (Existe "_" en letrasAdivinadas) HACER:
         IMPRIMIR "Palabra:", Unir Con Espacios(letrasAdivinadas)
         LEER "Ingresa una letra:" -> letra
         letra <- Convertir a Minúsculas(letra)

         SI (Longitud(letra) ≠ 1) O (letra no es Alfabética) Entonces:
              IMPRIMIR "Por favor, ingresa solo una letra."
              CONTINUAR
         FIN SI

         SI letra está en palabraOculta Entonces:
              PARA CADA índice, caracter en palabraOculta HACER:
                   SI caracter = letra Entonces:
                        letrasAdivinadas[indice] <- letra
                   FIN SI
              FIN PARA
              IMPRIMIR "¡Correcto!"
         SI NO:
              errores <- errores + 1
              IMPRIMIR "Incorrecto. Errores:", errores, "/", maxErrores
         FIN SI
    FIN MIENTRAS

    SI no existe "_" en letrasAdivinadas Entonces:
         IMPRIMIR "¡Felicidades! Has adivinado la palabra:", palabraOculta
    SI NO:
         IMPRIMIR "Has perdido. La palabra era:", palabraOculta
    FIN SI
FIN FUNCION

INICIAR:
    LLAMAR JuegoAhorcado


```

## Fibonacci
```plaintext

FUNCION SucesionFibonacci:
    LEER "Ingrese la posición hasta la que desea la sucesión de Fibonacci:" -> n
    SI n <= 0 Entonces:
         IMPRIMIR "El número debe ser mayor a 0."
         Terminar
    FIN SI

    secuencia <- [0, 1]
    
    SI n = 1 Entonces:
         IMPRIMIR "Fibonacci hasta la posición 1:", [0]
    SI NO SI n = 2 Entonces:
         IMPRIMIR "Fibonacci hasta la posición 2:", secuencia
    SI NO:
         PARA i DESDE 2 HASTA (n - 1) HACER:
              nuevoNumero <- secuencia[i - 1] + secuencia[i - 2]
              AÑADIR nuevoNumero a secuencia
         FIN PARA
         IMPRIMIR "Sucesión de Fibonacci hasta la posición", n, ":", secuencia
    FIN SI
FIN FUNCION

INICIAR:
    LLAMAR SucesionFibonacci

```

