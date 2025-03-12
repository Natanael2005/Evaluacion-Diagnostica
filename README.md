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
