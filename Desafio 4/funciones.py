""" Funciones | Desafio Stark 4 """

import re

def extraer_iniciales(nombre_heroe:str) -> str:
    """
    Esta funcion extrae la iniciales de un string. 
    Retorna: Las inciales separadas por '.' y en el caso de que sea un string vacio
    retorna N/A  
    """

    iniciales = ""

    if nombre_heroe == "":
        iniciales = "N/A"

    nombre_heroe = nombre_heroe.replace("-", " ")
    # Divide el nombre en dos elementos de la lista
    nombre_modificado = nombre_heroe.split()

    for e_nombre in nombre_modificado:
        if e_nombre.lower() != "the":
            iniciales += e_nombre[0].upper() + '.'

    return iniciales

def obtener_dato_formato(dato:str) -> bool:
    """
    Esta función toma un dato y lo convierte en formato booleano.
    Si el dato no es una cadena, se devuelve False.
    Si el dato es una cadena, se convierte a minúsculas y se reemplazan espacios
    y guiones con guiones bajos.
    Retorna: El dato en formato booleano o False si el dato no es una cadena.
    """

    if not isinstance(dato, str):
        dato = False
    else:
        dato = dato.lower().replace(" ", "_")
        dato = dato.lower().replace("-", "_")

    return dato

def stark_imprimir_nombre_con_iniciales(nombre_heroe:str) -> bool:
    """
    Esta función toma el nombre de un héroe, lo formatea y agrega sus iniciales.
    Si el nombre no es una cadena o no se pueden obtener iniciales, se devuelve False.
    Si el nombre es válido, se formatea y se agrega entre asteriscos y las iniciales se 
    colocan entre paréntesis.
    Retorna el nombre formateado con iniciales o False si el nombre no es una cadena o las 
    iniciales no se pueden obtener.
    """

    if isinstance(nombre_heroe, str):
        nombre = obtener_dato_formato(nombre_heroe)
        iniciales = extraer_iniciales(nombre_heroe)
        if nombre is not False:
            retorno = f"* {nombre} ({iniciales})"
    else:
        retorno = False

    return retorno


def stark_imprimir_nombres_con_iniciales(lista:list):
    """
    Esta funcion imprime la lista completa de los nombres de los personajes seguido de las 
    iniciales de los mismos.
    Retorna: Esta funcion no tiene retorno. 
    """

    if (isinstance(lista, list)) and (len(lista) > 0):
        for heroe in lista:
            if 'nombre' in heroe:
                nombre = stark_imprimir_nombre_con_iniciales(heroe['nombre'])
                if nombre is not False:
                    retorno = True
                    print(nombre)
            else:
                retorno = False
    else:
        retorno = False

    return retorno

def verificar_numerico(dato) -> bool:
    """
    Esta funcion recibe un dato y verifica si es de tipo numerico.
    Retorna: booleano 
    """

    retorno = False

    if isinstance(dato, (int, float)):
        retorno = True

    return retorno


def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> bool:
    """
    Esta función genera un string concatenando el genero y el id ingresado
    Retorna: N/A en caso de error, de lo contrario retorna el codigo generado
    """

    verifiacion = verificar_numerico(id_heroe)

    retorno = 'N/A'

    if verifiacion is True:
        if genero_heroe == 'M' or genero_heroe == 'F':
            if id_heroe in range(0,10000000):
                retorno = f"{genero_heroe}-{id_heroe:0>8}"
        elif genero_heroe == 'NB':
            if id_heroe in range(0,1000000):
                retorno = f"{genero_heroe}-{id_heroe:0>7}"

    return retorno

def agregar_codigo_heroe(heroe:dict, id_heroe:int) -> bool:
    """
    Esta función agrega una nueva clave llamada "codigo_heroe" al diccionario "heroe" recibido
    como parámetro y le asigna como valor el código
    generado por la funcion "generar_codigo_heroe"
    Retorna: True si paso todas las validaciones, de lo contrario retorna False
    """

    if len(heroe) > 0 and 'genero' in heroe:
        codigo = generar_codigo_heroe(id_heroe, heroe['genero'])
        heroe['codigo_heroe'] = codigo
        return True
    else:
        return False

def validar_dic_clave(lista:list, clave:str) -> bool:
    """
    Esta funcion valida si el elemento es un dic y valida que los diccionarios contengan la
    clave pasada por parametro
    Retorna: booleano   
    """

    for elemento in lista:
        if isinstance(elemento, dict) and elemento.get(clave) is None:
            return False

    return True


def stark_generar_codigos_heroes(lista:dict) -> bool:
    """
    Esta función agregara el código a cada uno de los personajes.
    Retorna: En caso de error, informar: "El origen de datos no contiene el formato correcto".
    """

    retorno = False

    i = 1
    if len(lista) == 0 and validar_dic_clave(lista, 'genero'):
        print('El origen de datos no contiene el formato correcto')
    else:

        for elemento in lista:
            codigo = agregar_codigo_heroe(elemento, i)
            i += 1

    if codigo is not False:
        retorno = True

    return retorno

def imprimir_nombres_codigos_heroes(lista:dict) -> bool:
    """
    Esta función toma una lista de héroes representados como un diccionario y genera y muestra sus
    nombres formateados con iniciales y códigos correspondientes.
    Si no se pueden generar códigos para los héroes, la función retorna False y no imprime nada.
    Si se pueden generar códigos, la función formatea el nombre del héroe y muestra el nombre junto
    con el código en el formato "nombre_formateado - código_heroe".
    Retorna: False si no se pueden generar códigos para los héroes, de lo contrario,
    retorna la lista de códigos generados.
    """

    retorno = stark_generar_codigos_heroes(lista)

    if retorno is not False:
        for heroe in lista:
            nombre = stark_imprimir_nombre_con_iniciales(heroe['nombre'])
            codigo = heroe['codigo_heroe']
            if nombre is not False:
                print(f'{nombre} - {codigo}')

    return retorno

def sanitizar_entero(numero_str:str):
    """
    Esta funcion recibe un string y evalua si ese estring contiene un posible dato numerico
    entero y positivo.
    Retorna: El numero convertido en entero si supera las validaciones.
    -1 si contiene carácteres no numéricos.
    -2 si el número es negativo.
    -3 si ocurren otros errores que no permiten convertirlo a entero.
    """

    retorno = -3

    if isinstance(numero_str, str):
        numero_str = numero_str.strip()

        if re.match(r"^[a-zA-Z]+$", numero_str):
            retorno = -1
        elif re.match(r"^-[0-9]+$", numero_str):
            retorno = -2
        elif re.match(r"^[0-9]+$", numero_str):
            numero = int(numero_str)

            if numero >= 0:
                retorno = numero

    return retorno

def sanitizar_flotante(numero_str:str):
    """
    Esta funcion recibe un string y evalua si ese estring contiene un posible dato
    numerico flotante y positivo.
    Retorna: El numero convertido en flotante si supera las validaciones.
    -1 si contiene carácteres no numéricos.
    -2 si el número es negativo.
    -3 si ocurren otros errores que no permiten convertirlo a entero.
    """

    retorno = -3

    if isinstance(numero_str, str):
        numero_str = numero_str.strip()

        if re.match(r"^[a-zA-Z]+$", numero_str):
            retorno = -1
        elif re.match(r"^-[0-9]+.[0-9]+$", numero_str):
            retorno = -2
        elif re.match(r"^[0-9]+.[0-9]+$", numero_str):
            numero = float(numero_str)

            if numero >= 0:
                retorno = numero

    return retorno

def sanitizar_string(valor_str:str, valor_por_defecto='-'):
    """
    Esta función analizara el string recibido y determinara si es solo texto (sin números). 
    Retorno: En caso de encontrarse números retornar “N/A”. En caso que se verifique que 
    el parámetro recibido es solo texto, retornara el mismo convertido todo a minúsculas.
    En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor 
    por defecto, entonces retornar el valor por defecto convertido a minúsculas.
    """

    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if re.search(r'\d', valor_str):
        return "N/A"
    elif re.search(r'/', valor_str):
        valor_str = valor_str.replace("/", " ")
    else:
        valor_str = valor_str.lower()
    if valor_str == "":
        return valor_por_defecto.lower()

    return valor_str

def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    """
    Esta función sanitizara el valor del diccionario correspondiente a la clave y al tipo
    de dato recibido.
    Retorna:  True en caso de haber sanitizado algún dato y False en caso contrario.
    """

    modificado = False

    if clave in heroe:

        if isinstance((tipo_dato, clave), str):
            clave = clave.lower()
            tipo_dato = tipo_dato.lower()

            if tipo_dato == 'flotante':
                heroe[clave] = sanitizar_flotante(heroe[clave])
                modificado = True
            elif tipo_dato == 'entero':
                heroe[clave] = sanitizar_entero(heroe[clave])
                modificado = True
            elif tipo_dato == 'string':
                heroe[clave] = sanitizar_string(heroe[clave])
                modificado = True
            else:
                modificado = 'Tipo de dato no válido'

            if heroe[clave] in [-1, -2, -3]:
                modificado = False
    else:
        modificado = 'La clave especificada no existe en el héroe'

    return modificado

def stark_normalizar_datos(lista_heroes:list) -> bool:
    """ 
    La función deberá recorrer la lista y sanitizar los valores de las siguientes claves:
    "altura", "peso", "color_ojos", "color_pelo", "fuerza" e "inteligencia"
    Retorna: Un string de confirmacion o error 
    """
    retorno = False

    if lista_heroes != "":
        for elemento in lista_heroes:
            sanitizar_dato(elemento, 'altura', 'flotante')
            sanitizar_dato(elemento, 'peso', 'flotante')
            sanitizar_dato(elemento, 'color_ojos', 'string')
            sanitizar_dato(elemento, 'color_pelo', 'string')
            sanitizar_dato(elemento, 'fuerza', 'entero')
            sanitizar_dato(elemento, 'inteligencia', 'string')
        retorno = lista_heroes
        print('Datos normalizados')
    else:
        print('Error: Lista de héroes vacía')

    return retorno

def generar_indice_nombres(lista_heroes:list):
    """
    Esta función itera una lista y genera una lista donde cada elemento es cada palabra que 
    componen los nombres encontrados.
    Retorna: En caso de error retorna un mensaje. De los contrario retorna la lista generada
    """

    lista_nueva = []

    if len(lista_heroes) == 0:
        retorno = 'ERROR! La lista esta vacia'

    for elemento in lista_heroes:

        if (isinstance(elemento, dict)) and 'nombre' in elemento:
            nombre = elemento['nombre']
            palabras = nombre.split()
            lista_nueva += palabras
        else:
            retorno = 'El origen de datos no contiene el formato correcto'
    retorno = lista_nueva

    return retorno

def stark_imprimir_indice_nombre(lista_heroes:list):
    """
    Esta funcion imprime todos los nombres separados por '-' y omite los "the".
    """

    indice = '-'
    indice = indice.join(generar_indice_nombres(lista_heroes))
    indice = indice.replace("-the", "")
    print(indice)

def generar_separador(patron:str, largo:int, imprimir=True) -> str:
    """
    Esta función genera un string que contiene un patrón especificado repitiendo tantas veces 
    como la cantidad recibida como parámetro.
    Retorna: "N/A" en caso de error. De lo contrario, retorna el separador generado 
    """

    if len(patron) > 0 and len(patron) <= 2 and largo > 0 and largo <= 236:
        separador = patron * largo
        retorno = separador
        if imprimir is False:
            return patron
    else:
        retorno = 'N/A'

    return retorno

def generar_encabezado(titulo:str):
    """
    Esta funcion genera un encabezado con el titulo en mayuscula que le pasemos como parametro 
    """

    titulo = titulo.upper()
    separador = generar_separador('**', 90)

    print(f"\n{separador} \n {titulo} \n{separador}\n")

def imprimir_ficha_heroe(heroe:dict):
    """
    Esta función generara la ficha de un heroe de la lista
    """

    nombre = stark_imprimir_nombre_con_iniciales(heroe['nombre'])

    generar_encabezado('principal')
    print(f"NOMBRE DEL HEROE: {nombre} \nIDENTIDAD SECRETA: {heroe['identidad']} \n"
        "CONSULTORA: {heroe['empresa']} \nCODIGO DE HEROE: {heroe['codigo_heroe']}")

    generar_encabezado('fisico')
    print(f"ALTURA: {heroe['altura']} cm \nPESO: {heroe['peso']} kg. \nFUERZA: {heroe['fuerza']} N")

    generar_encabezado('señas particulares')
    print(f"COLOR DE OJOS: {heroe['color_ojos']} \nCOLOR DE PELO: {heroe['color_pelo']} \n")

def stark_navegar_fichas(lista_heroes:list):
    """
    Imprime las fichas de los heroes y una barra para navegar entre las diferentes fichas  
    """
    verificacion = stark_generar_codigos_heroes(lista_heroes)

    if verificacion is not False:
        imprimir_ficha_heroe(lista_heroes[0])

        i = 0
        largo_lista = len(lista_heroes) - 1
        largo_lista_negativa = largo_lista * -1

        opcion = input("""[1] Ir a la izquierda [2] Ir a la derecha [3] Salir \n\n--> """)
        opcion.lower()

        while opcion == '1' or opcion == '2' or opcion == 's':
            if opcion == '1':
                if largo_lista_negativa == i:
                    i = 0
                else:
                    i -= 1
                imprimir_ficha_heroe(lista_heroes[i])
                opcion = input("""[1] Ir a la izquierda [2] Ir a la derecha [3] Salir \n\n--> """)
            elif opcion == '2':
                if largo_lista == i:
                    i = 0
                else:
                    i += 1
                imprimir_ficha_heroe(lista_heroes[i])
                opcion = input("""[1] Ir a la izquierda [2] Ir a la derecha [3] Salir \n\n--> """)
            elif opcion == '3':
                break
    else:
        print("Error")

def imprimir_menu() -> int:
    """
    Esta funcion imprime un menu de opciones, pide un entero y lo retorna.
    """

    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Imprimir la lista de nombres y el código del mismo
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir 
    """)

def stark_menu_principal():
    """
    Esta función imprime el menú de opciones y le pide al usuario que ingrese una.
    Retorna: La respuesta del usuario.
    """

    imprimir_menu()
    respuesta = input("\n\n--> ")

    return respuesta

def stark_marvel_app(lista_heroes:list):
    """ 
    La función se encargará de la ejecución principal de nuestro programa.
    """
    activar_opciones = False
    bandera_normalizar = True

    while True:
        opcion = stark_menu_principal()

        match opcion:
            case '1':
                if activar_opciones:
                    stark_imprimir_nombres_con_iniciales(lista_heroes)
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case '2':
                if activar_opciones:
                    imprimir_nombres_codigos_heroes(lista_heroes)
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case '3':
                if bandera_normalizar is True:
                    activar_opciones = stark_normalizar_datos(lista_heroes)
                    bandera_normalizar = False
                else:
                    print("Los datos ya fueron normalizados anteriormente.")
            case '4':
                if activar_opciones:
                    stark_imprimir_indice_nombre(lista_heroes)
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case '5':
                if activar_opciones:
                    stark_navegar_fichas(lista_heroes)
                else:
                    print("Debe normalizar los datos antes de usar esta opcion.")
            case 's':
                break
            case _:
                print("\nERROR, ingrese una opcion valida")
                opcion = stark_menu_principal()
