from datetime import datetime

def calcular_edad():
    print("Ingrese su fecha de nacimiento:")
    try:
        anio = int(input("Año (ej: 1990): "))
        mes = int(input("Mes (1-12): "))
        dia = int(input("Día (1-31): "))
        hora = int(input("Hora (0-23): "))
        fecha_nacimiento = datetime(anio, mes, dia, hora)
    except Exception as e:
        print("Error en la entrada de datos:", e)
        return

    ahora = datetime.now()
    if fecha_nacimiento > ahora:
        print("La fecha de nacimiento es en el futuro.")
        return

    diferencia = ahora - fecha_nacimiento

    años = diferencia.days // 365
    meses = diferencia.days // 30
    semanas = diferencia.days // 7
    dias = diferencia.days
    horas = diferencia.days * 24 + diferencia.seconds // 3600

    print("Edad aproximada:")
    print(f"Años: {años}")
    print(f"Meses: {meses}")
    print(f"Semanas: {semanas}")
    print(f"Días: {dias}")
    print(f"Horas: {horas}")

if __name__ == "__main__":
    calcular_edad()
# python edad.py