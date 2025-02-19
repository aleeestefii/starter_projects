import math 

def euclidean():
    try: 
        x1, y1 = map(float, input("teclea (x1 y1): ").split())# tienes que poner 2 3 
        x2, y2 = map(float, input("teclea (x2 y2): ").split())
        distance = math.sqrt((x2-x1) **2 + (y2-y1)**2)
        print("La distancia euclidiana es:", distance)
    except ValueError:
        print("es incorrecto lo que teclaste,inetea again")


def quadraticsolver():
    while True:
        a = float(input("Teclea a: "))
        if a == 0:
            print("'a' no puede ser 0. Intenta de nuevo.")
            continue  

        b = float(input("Teclea b: "))
        c = float(input("Teclea c: "))

        d = b**2 - 4*a*c  

        if d >= 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print(f"las soluciones son reales: {x1:.2f}, {x2:.2f}")
        else:
            real_part = -b / (2*a)
            imag_part = math.sqrt(abs(d)) / (2*a)
            print(f"las soluciones son complejas: {real_part:.2f} ± {imag_part:.2f}i")

        break 

while True:
    print("\nElige una opción:")
    print("1. Calcular distancia euclidiana")
    print("2. Resolver ecuación cuadrática")
    print("3. Salir")

    opcion = input("Teclea 1, 2 o 3: ")

    if opcion == "1":
        euclidean()
    elif opcion == "2":
        quadraticsolver()
    elif opcion == "3":
        print("bye")
        break
    else:
        print("Opción no válida, intenta de nuevo.")