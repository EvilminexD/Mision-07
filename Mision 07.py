# Autor: Ithan Alexis Pérez Sánchez
# Descripción: Misión 7 Ciclos While

# El codigo empieza después de esta linea

def dividir(divisor, dividendo):

    contador = 0
    residuo = 0

    while dividendo - divisor >= residuo:
        contador = contador + 1
        residuo = divisor * contador

    print(dividendo, "/", divisor, "=", contador, "sobra", dividendo - residuo)


def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")

    Mayor = 0
    Numeros = int(input("Tecla un número [-1 para salir]: "))
    if Numeros == -1 or Numeros <= 0:
        print("No hay valor mayor")

    else:
        while Numeros != -1:
            if Numeros > Mayor:
                Mayor = Numeros
            Numeros = int(input("Tecla un número [-1 para salir]: "))
        print("El Mayor es: ", Mayor)

def menu():
    print("Misión 07. Ciclos while")
    print("Autor: Ithan Alexis Pérez Sánchez")
    print("Matrícula: A01377717")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    print("¿Qué desea hacer?")
    Usuario = int(input("Escoge el número que desees saber: "))
    return Usuario


def main():

    Usuario = menu()
    while Usuario != 3:
        if Usuario == 1:
            dividendo = int(input("Ingresa un digito: "))
            divisor = int(input("Ingresa un digito: "))
            dividir(divisor, dividendo)
            Usuario = menu()

        elif Usuario == 2:
            encontrarMayor()
            Usuario = menu()

        elif Usuario > 3 or Usuario <= 0:
            print("ERROR, teclea 1, 2 o 3")
            Usuario = menu()

    print("Gracias por usar este programa, regresa pronto")

main()