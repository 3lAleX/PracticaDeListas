import time

def AnimacionInicio() :
    print("################################################################\n")
    print("Iniciando programa...\n" )
    time.sleep(.7)
    print("Descargando dependencias (12%)" )
    time.sleep(1.3)
    print("Descargando dependencias (48%)" )
    time.sleep(1.3)
    print("Descargando dependencias (90%)" )
    time.sleep(0.3)
    print("Descargando dependencias (97%)" )
    time.sleep(1.3)
    print("Descarga completada 17/17 elementos" )
    print("################################################################\n")

def Menu () -> int:
    msj =  ("===================================================================\n" +
            "PRÁCTICAS DE LISTAS\n" + 
            "Selecciona el ejercicio que deseas ejecutar:\n" +
            "[1] Agregar datos a una lista\n" +
            "[2] Buscar elemento en lista\n" +
            "[3] Práctica 2 - Lista de compras\n" +
            "[4] Práctica 3 - Una matriz\n" +
            "[5] Práctica 4 - Iguales o no\n" +
            "[0] Salir del programa\n" +
            "===================================================================\n" +
            "-> Ingresa el número de tu opción: ")
    respuesta = int(input(msj))
    return respuesta 

def AgregarDatos() -> tuple:
	print("Bienvenido!!!\nA continuación vas a ingresar datos en lista, para interrumpir el proceso ingresa un asterisco(*) y preciona enter.\n")
	Lista = []
	while True:
		x = input("Ingresa el elemento: ")
		if x == "":
			continue
		if x == "*":
			break
		Lista.append(x)
	return tuple(Lista)

def EstaEnLista() -> tuple:
    #Decidí no hacer uso de las funciones que python proporciona porque entré en razón que cada vez que se utiliza una función index,  'in', o count, se esta recorriendo la lista, entonces me dió cosa el pensar que para este programa estaba recorriendo tres veces la lista para la busqueda y pense en hacerlo de una forma que no requiera buscar tanto.
    """"""

    cuenta = 0 #Lista.count(elemento) #La cantidad de veces que el elemento se encuentra en la lista
    indices = []   #Contiene los indices del elemento en la Lista
    aux = 0 #Sirve para llevar una idea de en q index estamos
    Lista = AgregarDatos()
    busqueda = input("¿Que elemento deseas buscar?  ")

    for elemento in Lista:
        if elemento == busqueda:
            cuenta += 1
            indices.append(aux)
        aux += 1

    if cuenta > 0:
        return (True, busqueda, cuenta, indices)         
    else:
        return (False, busqueda)

def Practica2() -> None:
    List = []
    while True:
        msj =  ("-------------------------------------------------------------------\n" +
            "Menú de la Práctica 2 / Lista de compras\n" + 
            "Selecciona la acción que deseas ejecutar en la lista de compras:\n" +
            "[1] Agregar un elemento\n" +
            "[2] Cuantar las apariciones de un elemento\n" +
            "[3] Eliminar un elemento\n" +
            "[4] Modificar un elemento\n" +
            "[5] Mostrar la lista\n" +
            "[0] Finalizar\n" +
            "-------------------------------------------------------------------\n" +
            "-> Ingresa el número de tu opción: ")
        match int(input(msj)):
            case 1:
                List.append(input("Ingrese el elemento que desea añadir: "))
            case 2: 
                conteo = List.count(input("Ingrese el elemento que desea buscar: "))
                print(f"El elemento aparece {conteo} veces.")
            case 3:
                elementoEliminar = input("Ingresa el elemento que desea eliminar: ")
                conteo = List.count(elementoEliminar)
                if conteo > 1:
                    if input(f"El elemento {elementoEliminar} aparece {conteo} veces\n¿Desea eliminar todas las ocurrencias? s/n: ") == 's':
                        for i in range(conteo):
                             List.remove(elementoEliminar)
                    else: List.remove(elementoEliminar)
            case 4:
                elementoModificar = input("Ingresa el elemento que desea modificar: ")
                remplazo = input("Ingresa la modificación: ")
                conteo = List.count(elementoModificar)
                if conteo > 1:
                    if input(f"El elemento {elementoModificar} aparece {conteo} veces\n¿Desea modificar todas las ocurrencias? s/n: ") == 's':
                        for i in range(conteo-1):
                            index = List.index(elementoModificar)
                            List[index] = remplazo
                index = List.index(elementoModificar)
                List[index] = remplazo
            case 5:
                print("Lista de compras:\n")
                for conteo in range(len(List)):
                    if conteo == len(List)-1:
                        print(f"{List[conteo]} ")
                        break
                    print(f"{List[conteo]}, ", end=" ")
            case 0:
                break
            case _:
                None
      
def Practica3() -> None:
    #Matriz 4X5
    matriz = [
    ["1", "2", "3", "4", "5"],
    ["2", "4", "6", "8", "10"],
    ["3", "6", "9", "12", "15"],
    ["4", "8", "12", "16", "20"]
    ]

    aux = 0
    while True:
        if aux > 3:
            break
        for i in range(len(matriz[aux])):
            if i == len(matriz[aux])-1:
                print(matriz[aux][i], end=" | ")
            else:
                print(matriz[aux][i], end=", ")
        aux += 1
    print()
    #Aquí voy a suponer que se refiere a la columna y a la fila completa jeje, quizás se refiere a la coordenada pero no estoy seguro
    c = int(input("Ingresa el número de columna a buscar: "))-1
    f = int(input("Ingresa el número de fila a buscar: "))-1
    print(f"El contenido de la columna {c+1} es: ", end=" ")
    for i in range(4):
        if i == 3:
            print(matriz[i][c])
        else:
            print(matriz[i][c], end=", ")

    print(f"\nEl contenido de la fila {f+1} es: ", end=" ")
    for i in range(5):
        if i == 4:
            print(matriz[f][i])
        else:
            print(matriz[f][i], end=", ")
    print("\n")

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                print(f"El elemento en la posición {i+1}x{j+1} es: {matriz[i][j]}")


    return
def Practica4() -> None:
      return

AnimacionInicio()
while True:
    match Menu():
        case 1:
            Lista = AgregarDatos()
            print("La lista contiene:\n")
            for x in range(0, len(Lista)-1):
                print(f"{Lista[x]}", end= ", ")
            print(f"{Lista[len(Lista)-1]}.")        
        case 2:
            res = EstaEnLista()
            if res[0] == False:
                 print(f"La lista no contiene {res[1]}")
            else:
                print(f"El elemento ({res[1]}) se encuentra un total de {res[2]} veces en los indíces: ", end=" ")
                for x in res[3]:
                    print(x, end=", ")
        case 3:
            Practica2()
        case 4:
            Practica3()
        case 5: 
            Practica2()
        case 0:
            break
        case _:
            print("Opción desconocida")
    
