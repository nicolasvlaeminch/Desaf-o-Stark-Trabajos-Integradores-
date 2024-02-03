""" Funciones | Desafio Stark 3 """

def stark_normalizar_datos(lista:dict) -> dict:
    """Normaliza los datos del diccionario"""

    modificado = False

    for heroe in lista:
        if type(heroe["altura"] != float):
            heroe["altura"] = float(heroe["altura"])
        else:
            modificado = False
            break
        if type(heroe["peso"] != float):
            heroe["peso"] = float(heroe["peso"])
        else:
            modificado = False
            break
        if type(heroe["fuerza"] != int):
            heroe["fuerza"] = int(heroe["fuerza"])
        else:
            modificado = False
            break
        modificado = True

    if modificado:
        print("Datos Normalizados")
    else:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que "
            "los datos ya no se hayan normalizado anteriormente")

    return lista

def obtener_dato(lista: dict, clave: str) -> str:
    """Busca y devuelve el valor de la clave en el diccionario, si la clave existe 
    y el diccionario tambien y no esta vacio, de lo contrario retorna False."""
    retorno = False

    if isinstance(lista, dict) and isinstance(clave, str) and (len(lista) > 0):
        if (clave in lista) and ("nombre" in lista):
            retorno = lista[clave]

    return retorno

def obtener_nombre(lista:dict) -> str:
    """Esta funcion recibe por parametro un diccionario el cual representara a un heroe y devolvera
    un string el cual contenga su nombre formateado."""

    nombre = obtener_dato(lista, "nombre")

    if nombre is not False:
        retorno = f"Nombre: {nombre}"
    else:
        retorno = False

    return retorno

def obtener_nombre_y_dato(lista: dict, clave: str):
    """Obtiene el nombre y el dato de una clave en una lista de diccionarios, y los devuelve en una
    cadena, o False si la lista esta vacia o el dato o el nombre no existen."""

    nombre = obtener_nombre(lista)
    dato = obtener_dato(lista, clave)

    if (nombre != False) and (dato != False) and (len(lista) > 0):
        retorno = f"{nombre} | {clave}: {dato}"
    else:
        retorno = False

    return retorno

def calcular_max_min(lista:list, clave:str, tipo:str):
    """Calcular el Maximo o Minimo de una clave ingresada y lo retorna."""

    max_min = lista[0][clave]

    if (len(lista) > 0) and isinstance(lista, list) and isinstance(clave, str) and isinstance(tipo, str):
        if isinstance(max_min, int) or isinstance(max_min, float):
            for i in lista:
                if tipo == "maximo":
                    if i[clave] > max_min:
                        max_min = i[clave]
                elif tipo == "minimo":
                    if i[clave] < max_min:
                        max_min = i[clave]
        else:
            max_min = False

    return max_min

def obtener_dato_cantidad(lista:dict, valor, clave:str):
    """Busca y devuelve una lista de heroes que tienen un valor especifico en una clave dada en una
    lista de diccionarios."""

    lista_cantidad = []

    for heroe in lista:
        if valor == heroe[clave]:
            lista_cantidad.append(heroe)

    return lista_cantidad

def stark_imprimir_heroes(lista:list) -> list:
    """Imprime una lista de superheroes si el diccionario existe o no esta vacio."""
    if isinstance(lista, list) and (len(lista) > 0):
        for heroe in lista:
            nombre = heroe["nombre"]
            altura = heroe["altura"]
            peso = heroe["peso"]
            genero = heroe["genero"]
            color_ojos = heroe["color_ojos"]
            color_pelo = heroe["color_pelo"]
            fuerza = heroe["fuerza"]
            inteligencia = heroe["inteligencia"]

            print(f"\nNombre: {nombre} \
                    \nAltura: {altura:.2f}cm \
                    \nPeso: {peso:.2f}kg \
                    \nGenero: {genero} \
                    \nColor ojos: {color_ojos} \
                    \nColor pelo: {color_pelo} \
                    \nFuerza: {fuerza} \
                    \nInteligencia: {inteligencia}")
    else:
        return False

def sumar_dato_heroe_imprimir(lista:list, clave:str):
    """Calcula la suma de datos para cada valor unico de una clave específica y las muestra."""

    contadores_clave = {}

    for i in lista:
        dato = i.get(clave)

        if dato in contadores_clave:
            contadores_clave[dato] += 1
        else:
            contadores_clave[dato] = 1

    for i, conteo in contadores_clave.items():
        print(f"{i}: {conteo}")

def sumar_dato_heroe(lista:dict, clave:str) -> float:
    """Recibe una lista de heroes y una clave de la que se requiere sumar. Retorna la suma de todos
    los datos segun la clave pasada por parametros y False en caso de error."""

    acumulador_dato = 0
    retorno = False

    for elemento in lista:
        if isinstance(elemento, dict):
            acumulador_dato += float(elemento[clave])
        retorno = acumulador_dato
    return retorno

def dividir(dividendo, divisor):
    """Esta funcion divide dos numeros enteros y lo retorna. En el caso de que el divisor sea '0'
    retorna False."""

    if divisor == 0:
        return False
    else:
        return dividendo / divisor

def calcular_promedio(lista:list, clave:str):
    """Calcula el promedio de una clave especifica y luego lo retorna."""
    retorno = False
    lista_numeros = []

    if isinstance(lista, list) and isinstance(clave, str) and len(lista) > 0:
        for elemento in lista:
            lista_numeros.append(float(elemento[clave]))

            if len(lista_numeros) > 0:
                suma = sumar_dato_heroe(lista, clave)
                retorno = dividir(suma, len(lista_numeros))

        return retorno

def mostrar_promedio_dato(lista:dict, clave:str):
    """Calcula y muestra el promedio de un dato numerico en una lista de elementos."""

    if isinstance(lista.get(clave), int) or isinstance(lista.get(clave), float) and (len(lista) > 0):
        promedio = calcular_promedio(lista, clave)
        print(f"El promedio de {clave} es: {promedio}")
    else:
        return False

def validar_entero(numero:str):
    """Esta funcion recibe por parametro un string de numero. Retornara True en caso de serlo,
    False caso contrario."""

    for elemento in numero:
        if not elemento.isdigit():
            return False
    return True

def heroe_max_min_clave(lista:dict, clave:str, tipo:str, genero:str):
    """Encuentra y muestra el superheroe con el valor maximo o minimo para una clave especifica y un
    genero dado."""

    lista_heroes_genero = obtener_dato_cantidad(lista, genero, "genero")

    heroe_valor = calcular_max_min(lista_heroes_genero, clave, tipo)

    heroe_mostrar = obtener_dato_cantidad(lista_heroes_genero, heroe_valor, clave)

    stark_imprimir_heroes(heroe_mostrar)

def promedio_clave_genero(lista:dict, clave:str, genero:str):
    """Calcula el promedio de una clave especifica para un grupo de superheroes de un genero dado y
    lo imprime."""

    lista_heroes_genero = obtener_dato_cantidad(lista, genero, "genero")

    promedio_clave = calcular_promedio(lista_heroes_genero, clave)

    print(f"El promedio de {clave} de los superheroes genero {genero} es: {promedio_clave:.2f}")

def ordenar_imprimir_clave(lista:dict, clave:str):
    """Ordena una lista por clave y la guarda en un diccionario para luego imprimir la clave de 
    forma ordenada."""

    ordenar_por_clave = {}

    for i in lista:

        dato_clave = i[clave]

        # Si no existe el dato de la clave, crea una nueva lista en el diccionario.
        if dato_clave not in ordenar_por_clave:
            ordenar_por_clave[dato_clave] = []

        # Agrega el nombre a la lista correspondiente.
        ordenar_por_clave[dato_clave].append(i["nombre"])

    print(ordenar_por_clave)
    for dato, lista_heroes in ordenar_por_clave.items():
        print(f"-> {clave}: {dato}:\n")
        print(dato)
        print(lista_heroes)
        for heroe in lista_heroes:
            print(f"{heroe}\n")

def imprimir_menu(mensaje:str, mensaje_error:str, opciones:list) -> int:
    """Muestra un menu con el mensaje ingresado, pide un input verifica que el dato ingresado sea 
    correcto de lo contrario mostrara el mensaje_error ingresado y pediria nuevamente el input hasta 
    ingresar un dato correcto y lo retornara como un entero."""

    opcion = None
    while True:
        opcion = input(mensaje).lower()
        while opcion not in opciones:
            opcion = input(mensaje_error).lower()

        return opcion

def stark_menu_principal() -> chr:
    """Muestra el Menu Stark y retorna un char si esta dentro de la lista de verificacion, de lo
    contrario enviaria un mensaje de error y pedira una opcion nuevamente."""

    opcion = imprimir_menu(
        "\n********************************************************************************************\n"                    
        "*                               Bienvenido al Desafio Stark                                *\n"
        "********************************************************************************************\n"
        "*  A: Normalizar datos.                                                                    *\n"
        "*  B: Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB  *\n"
        "*  C: Recorrer la lista y determinar cuál es el superhéroe más alto de género F.           *\n"
        "*  D: Recorrer la lista y determinar cuál es el superhéroe más alto de género M.           *\n"
        "*  E: Recorrer la lista y determinar cuál es el superhéroe más débil de género M.          *\n"
        "*  F: Recorrer la lista y determinar cuál es el superhéroe más débil de género NB.         *\n"
        "*  G: Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB.   *\n"
        "*  H: Determinar cuántos superhéroes tienen cada tipo de color de ojos.                    *\n"
        "*  I: Determinar cuántos superhéroes tienen cada tipo de color de pelo.                    *\n"
        "*  J: Listar todos los superhéroes agrupados por color de ojos.                            *\n"
        "*  K: Listar todos los superhéroes agrupados por tipo de inteligencia.                     *\n"
        "*  Z: Salir del programa.                                                                  *\n"
        "********************************************************************************************\n"
        "Ingrese una opcion: ",
        "\n********************************************************************************************\n"
        "*                               Bienvenido al Desafio Stark                                *\n"
        "********************************************************************************************\n"
        "*  A: Normalizar datos.                                                                    *\n"
        "*  B: Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB. *\n"
        "*  C: Recorrer la lista y determinar cuál es el superhéroe más alto de género F.           *\n"
        "*  D: Recorrer la lista y determinar cuál es el superhéroe más alto de género M.           *\n"
        "*  E: Recorrer la lista y determinar cuál es el superhéroe más débil de género M.          *\n"
        "*  F: Recorrer la lista y determinar cuál es el superhéroe más débil de género NB.         *\n"
        "*  G: Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB.   *\n"
        "*  H: Determinar cuántos superhéroes tienen cada tipo de color de ojos.                    *\n"
        "*  I: Determinar cuántos superhéroes tienen cada tipo de color de pelo.                    *\n"
        "*  J: Listar todos los superhéroes agrupados por color de ojos.                            *\n"
        "*  K: Listar todos los superhéroes agrupados por tipo de inteligencia.                     *\n"
        "*  Z: Salir del programa.                                                                  *\n"
        "********************************************************************************************\n"
    "ERROR: Ingrese una opcion: ", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "z"])

    return opcion

def stark_marvel_app(lista:dict):
    """Recibe por parametro la lista de heroes y se encargara de la ejecucion principal de nuestro
    programa. Valida que la opcion ingresada sea correcta si no tira un mensaje de error y pide que
    se ingrese una nueva opcion."""

    activar_opciones = False

    while True:
        opcion = stark_menu_principal()

        match opcion:
            case "a":
                activar_opciones = stark_normalizar_datos(lista)
            case "b":
                if activar_opciones:
                    heroes_genero_nb = obtener_dato_cantidad(lista, "NB", "genero")
                    for heroes in heroes_genero_nb:
                        print(obtener_nombre(heroes))
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "c":
                if activar_opciones:
                    heroe_max_min_clave(lista, "altura", "maximo", "F")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "d":
                if activar_opciones:
                    heroe_max_min_clave(lista, "altura", "maximo", "M")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "e":
                if activar_opciones:
                    heroe_max_min_clave(lista, "fuerza", "minimo", "M")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "f":
                if activar_opciones:
                    heroe_max_min_clave(lista, "fuerza", "minimo", "NB")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "g":
                if activar_opciones:
                    promedio_clave_genero(lista, "fuerza", "NB")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "h":
                if activar_opciones:
                    sumar_dato_heroe_imprimir(lista, "color_ojos")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "i":
                if activar_opciones:
                    sumar_dato_heroe_imprimir(lista, "color_pelo")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "j":
                if activar_opciones:
                    ordenar_imprimir_clave(lista, "color_ojos")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "k":
                if activar_opciones:
                    ordenar_imprimir_clave(lista, "inteligencia")
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case "z":
                print("Salio del programa")
                break
