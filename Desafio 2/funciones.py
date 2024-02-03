""" Funciones | Desafio Stark 2 """

def calcular_max_min(lista:list, clave:str, tipo:str)->float:
    """Calcular el Maximo o Minimo de una clave ingresada y lo retorna en un float."""

    max_min = float(lista[0][clave])

    for i in lista:
        if tipo == "maximo":
            if float(i[clave]) > max_min:
                max_min = float(i[clave])
        elif tipo == "minimo":
            if float(i[clave]) < max_min:
                max_min = float(i[clave])

    return max_min

def calcular_promedio_genero(lista:list, clave:str, genero:str)->float:
    """Calcular Promedio Clave del genero deseado y lo retorna en un float."""

    sumatoria_clave = 0
    contador_genero = 0

    for i in lista:
        if i["genero"] == genero:
            sumatoria_clave = sumatoria_clave + float(i[clave])
            contador_genero = contador_genero + 1

    promedio = sumatoria_clave / contador_genero

    return promedio

def crear_lista_superheroes_clave(lista:list, clave:str, dato:str)->list:
    """Filtra una lista de superhéroes por una clave y un dato específicos, lo guarda en una nueva
    lista y la retorna."""

    lista_superheroes_filtrada = []

    for i in lista:
        if i[clave] == dato:
            superheroe = {
                "nombre": i["nombre"],
                "identidad": i["identidad"],
                "empresa": i["empresa"],
                "altura": float(i["altura"]),
                "peso": float(i["peso"]),
                "genero": i["genero"],
                "color_ojos": i["color_ojos"],
                "color_pelo": i["color_pelo"],
                "fuerza": i["fuerza"],
                "inteligencia": i["inteligencia"]
            }

            lista_superheroes_filtrada.append(superheroe)

    return lista_superheroes_filtrada

def imprimir_superheroes_genero(lista:list, genero:str):
    """Imprime un listado de superheroes segun su genero."""

    print(f"Los superheroes {genero} son los siguientes:\n")

    for i in lista:
        if i["genero"] == genero:
            nombre = i["nombre"]
            print(f"Nombre: {nombre}\n")

def imprimir_superheroe_max_min_genero(lista:list, clave:str, genero:str, max_min:str):
    """Imprime el superheroe con la clave mas alta o mas baja ingresada."""

    lista_superheroes_genero = crear_lista_superheroes_clave(lista, "genero", genero)

    heroe_max_min = calcular_max_min(lista_superheroes_genero, clave, max_min)

    for i in lista_superheroes_genero:
        if heroe_max_min == float(i[clave]):
            nombre = i["nombre"]

            if max_min == "maximo":
                print(f"El superheroe genero {genero} con mas {clave} es: {nombre}"
                    f" con {heroe_max_min} de {clave}\n")
            else:
                print(f"El superheroe genero {genero} con menos {clave} es: {nombre}"
                    f" con {heroe_max_min} de {clave}\n")

def imprimir_superheroe_promedio_genero(lista:list, clave:str, genero:str):
    """Imprime el promedio del genero y clave deseada."""

    clave_promedio = calcular_promedio_genero(lista, clave, genero)

    print(f"El promedio de {clave} de los superheroes {genero} es {clave_promedio:.2f}")

def imprimir_contadores_clave(lista:list, clave:str):
    """Cuenta las cantidad de clave y las imprime."""

    contadores_clave = {}

    for i in lista:
        dato = i.get(clave)

        if dato in contadores_clave:
            contadores_clave[dato] += 1
        else:
            contadores_clave[dato] = 1

    for i, conteo in contadores_clave.items():
        print(f"{i}: {conteo}")

def imprimir_menu(mensaje:str, mensaje_error:str, opciones:list)->int:
    """Muestra un menu con el mensaje ingresado, pide un input verifica que el dato ingresado sea 
    correcto de lo contrario mostrara el mensaje_error ingresado y pediria nuevamente el input hasta 
    ingresar un dato correcto y lo retornara como un entero."""

    opcion = None
    while True:
        opcion = input(mensaje).lower()
        while opcion not in opciones:
            opcion = input(mensaje_error).lower()

        return opcion

def ordenar_clave(lista:list, clave:str):
    """Ordena una lista por clave y la guarda en un diccionario para luego imprimir la clave de 
    forma ordenada"""

    ordenar_por_clave = {}

    for i in lista:
        dato_clave = i[clave]
        if dato_clave not in ordenar_por_clave:
            ordenar_por_clave[dato_clave] = []
        ordenar_por_clave[dato_clave].append(i["nombre"])

    for dato, lista_heroes in ordenar_por_clave.items():
        print(f"-> {clave}: {dato}:\n")
        for heroe in lista_heroes:
            print(f"{heroe}\n")

def menu_stark(lista:list):
    """Muestra el Menu Stark"""
    while True:
        opcion = imprimir_menu(
            "\n*************************************************************************\n"                    
            "*                      Bienvenido al Desafio Stark                      *\n"
            "*************************************************************************\n"
            "*  A: Mostrar superheroes genero no binario.                            *\n"
            "*  B: Mostrar superheroe mas alto genero femenino.                      *\n"
            "*  C: Mostrar superheroe mas alto de genero masculino.                  *\n"
            "*  D: Mostrar superheroe mas debil de genero masculino.                 *\n"
            "*  E: Mostrar superheroe mas debil de genero no binario.                *\n"
            "*  F: Mostrar fuerza promedio de los superheroes genero no binario.     *\n"
            "*  G: Mostrar cuantos superheroes tienen cada tipo de color de ojos.    *\n"
            "*  H: Mostrar cuántos superheroes tienen cada tipo de color de pelo.    *\n"
            "*  I: Listar todos los superheroes agrupados por color de ojos.         *\n"
            "*  J: Listar todos los superheroes agrupados por tipo de inteligencia   *\n"
            "*  Z: Salir del programa.                                               *\n"
            "*************************************************************************\n"
            "Ingrese una opcion: ",
            "\n*************************************************************************\n"
            "*                      Bienvenido al Desafio Stark                      *\n"
            "*************************************************************************\n"
            "*  A: Mostrar superheroes genero no binario.                            *\n"
            "*  B: Mostrar superheroe mas alto genero femenino.                      *\n"
            "*  C: Mostrar superheroe mas alto de genero masculino.                  *\n"
            "*  D: Mostrar superheroe mas debil de genero masculino.                 *\n"
            "*  E: Mostrar superheroe mas debil de genero no binario.                *\n"
            "*  F: Mostrar fuerza promedio de los superheroes genero no binario.     *\n"
            "*  G: Mostrar cuantos superheroes tienen cada tipo de color de ojos.    *\n"
            "*  H: Mostrar cuántos superheroes tienen cada tipo de color de pelo.    *\n"
            "*  I: Listar todos los superheroes agrupados por color de ojos.         *\n"
            "*  J: Listar todos los superheroes agrupados por tipo de inteligencia   *\n"
            "*  Z: Salir del programa.                                               *\n"
            "*************************************************************************\n"
        "ERROR: Ingrese una opcion: ", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "z"])
        match opcion:
            case "a":
                imprimir_superheroes_genero(lista, "NB")
            case "b":
                imprimir_superheroe_max_min_genero(lista, "altura", "F", "maximo")
            case "c":
                imprimir_superheroe_max_min_genero(lista, "altura", "M", "maximo")
            case "d":
                imprimir_superheroe_max_min_genero(lista, "fuerza", "M", "minimo")
            case "e":
                imprimir_superheroe_max_min_genero(lista, "fuerza", "NB", "minimo")
            case "f":
                imprimir_superheroe_promedio_genero(lista, "fuerza", "NB")
            case "g":
                imprimir_contadores_clave(lista, "color_ojos")
            case "h":
                imprimir_contadores_clave(lista, "color_pelo")
            case "i":
                ordenar_clave(lista, "color_ojos")
            case "j":
                ordenar_clave(lista, "inteligencia")
            case "z":
                print("Salio del programa")
                break
