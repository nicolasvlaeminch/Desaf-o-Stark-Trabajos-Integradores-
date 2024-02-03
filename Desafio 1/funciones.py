"""Hola"""
def imprimir_heroes(lista):
    """"hola"""
    for i in lista:
        nombre = i["nombre"]
        identidad = i["identidad"]
        empresa = i["empresa"]
        altura = float(i["altura"])
        peso = float(i["peso"])
        genero = i["genero"]
        ojos = i["color_ojos"]
        pelo = i["color_pelo"]
        fuerza = i["fuerza"]
        inteligencia = i["inteligencia"]

        print(f"Nombre: {nombre} | "
            f"Identidad: {identidad} | "
            f"Empresa: {empresa} | "
            f"Altura: {altura:.2f} | "
            f"Peso: {peso:.2f} | "
            f"Genero: {genero} | "
            f"Color de ojos: {ojos} | "
            f"Color de pelo: {pelo} | "
            f"Fuerza: {fuerza} | "
            f"Inteligencia: {inteligencia}\n")

def imprimir_heroe_mayor_fuerza(lista, clave, tipo):
    heroe_mayor_fuerza = calcular_max_min(lista, clave, tipo)

    print(f"Los superheroes con mayor fuerza son los siguientes con un total de {heroe_mayor_fuerza} de fuerza: \n")
    for i in lista:
        if heroe_mayor_fuerza == float(i["fuerza"]):
            identidad = i["identidad"]
            peso = float(i["peso"])

            print(f"Identidad: {identidad} | Peso: {peso:.2f}\n")

def imprimir_heroe_mas_bajo(lista, clave, tipo):
    heroe_mas_bajo = calcular_max_min(lista, clave, tipo)

    print(f"El superheroe mas bajo es el siguiente con {heroe_mas_bajo}cm : \n")
    for i in lista:
        if heroe_mas_bajo == float(i["altura"]):
            nombre = i["nombre"]
            identidad = i["identidad"]

            print(f"Nombre: {nombre} | Identidad: {identidad}\n")

def imprimir_promedio_peso_masculino(lista, clave, genero):
    promedio_peso_masculino = calcular_promedio_genero(lista, clave, genero)

    print(f"El peso promedio de los superheroes masculinos es {promedio_peso_masculino:.2f}.\n")

def imprimir_superheroes_promedio_superior(lista, clave, genero):
    promedio_fuerza_femenino = calcular_promedio_genero(lista, clave, genero)

    print(f"El promedio de fuerza de las superheroes de genero femenino es "
        f"{promedio_fuerza_femenino:.2f} y los siguientes superheroes lo superan: \n")

    for i in lista:
        if promedio_fuerza_femenino < float(i["fuerza"]):
            nombre = i["nombre"]
            peso = float(i["peso"])

            print(f"Nombre: {nombre} | Peso: {peso:.2f}\n")


# Busca en la lista el maximo o el minimo de la clave ingresada.
def calcular_max_min(lista, clave, tipo):
    max_min = float(lista[0][clave])

    for i in lista:
        if tipo == "maximo":
            if float(i[clave]) > max_min:
                max_min = float(i[clave])
        else:
            if float(i[clave]) < max_min:
                max_min = float(i[clave])

    return max_min

def calcular_promedio_genero(lista, clave, genero):
    sumatoria_clave = 0
    contador_genero = 0

    for i in lista:
        if i["genero"] == genero:
            sumatoria_clave = sumatoria_clave + float(i[clave])
            contador_genero = contador_genero + 1

    promedio = sumatoria_clave / contador_genero

    return promedio

def menu_stark(lista):
    while True:
        opcion = input(
            "\n*************************************************************************\n"
            "*                      Bienvenido al Desafio Stark                      *\n"
            "*************************************************************************\n"
            "*  A: Mostrar todos los datos de los superheroes.                       *\n"
            "*  B: Mostrar la identidad y el peso del superheroe con mas fuerza.     *\n"
            "*  C: Mostrar nombre e identidad del superheroe mas bajo.               *\n"
            "*  D: Mostrar el peso promedio de los superheroes masculinos.           *\n"
            "*  E: Mostrar el nombre y peso de los superheroes que superen la fuerza *\n"
            "*  promedio de todas las superheroes de genero femenino.                *\n"                
            "*  Z: Salir del programa.                                               *\n"
            "*************************************************************************\n"
            "Ingrese una opcion: ").lower()
        while opcion not in ["a", "b", "c", "d", "e", "z"]:
            opcion = input(
                "\n*************************************************************************\n"
                "*                      Bienvenido al Desafio Stark                      *\n"
                "*************************************************************************\n"
                "*  A: Mostrar todos los datos de los superheroes.                       *\n"
                "*  B: Mostrar la identidad y el peso del superheroe con mas fuerza.     *\n"
                "*  C: Mostrar nombre e identidad del superheroe mas bajo.               *\n"
                "*  D: Mostrar el peso promedio de los superheroes masculinos.           *\n"
                "*  E: Mostrar el nombre y peso de los superheroes que superen la fuerza *\n"
                "*  promedio de todas las superheroes de genero femenino.                *\n"                
                "*  Z: Salir del programa.                                               *\n"
                "*************************************************************************\n"
                "ERROR: Ingrese una opcion: ").lower()
        match opcion:
            case "a":
                imprimir_heroes(lista)
            case "b":
                imprimir_heroe_mayor_fuerza(lista, "fuerza", "maximo")
            case "c":
                imprimir_heroe_mas_bajo(lista, "altura", "minimo")
            case "d":
                imprimir_promedio_peso_masculino(lista, "peso", "M")
            case "e":
                imprimir_superheroes_promedio_superior(lista, "peso", "F")
            case "z":
                print("Salio del programa")
                break
