def sucesion_fibonacci():
    try:
        n = int(input("Ingrese la posición hasta la que desea la sucesión de Fibonacci: "))
    except Exception as e:
        print("Debe ingresar un número entero válido.", e)
        return

    if n <= 0:
        print("El número debe ser mayor a 0.")
        return

    fib = [0, 1]
    if n == 1:
        print("Fibonacci hasta la posición 1: [0]")
    elif n == 2:
        print("Fibonacci hasta la posición 2:", fib)
    else:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        print(f"Sucesión de Fibonacci hasta la posición {n}:")
        print(fib)
def sucesion_fibonacci():
    try:
        n = int(input("Ingrese la posición hasta la que desea la sucesión de Fibonacci: "))
    except Exception as e:
        print("Debe ingresar un número entero válido.", e)
        return

    if n <= 0:
        print("El número debe ser mayor a 0.")
        return

    fib = [0, 1]
    if n == 1:
        print("Fibonacci hasta la posición 1: [0]")
    elif n == 2:
        print("Fibonacci hasta la posición 2:", fib)
    else:
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        print(f"Sucesión de Fibonacci hasta la posición {n}:")
        print(fib)

if __name__ == "__main__":
    sucesion_fibonacci()

# python fibonacci.py
