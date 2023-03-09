
exito = 0

diccionario = {}

while exito == 0:
    print("1. Agregar un nuevo equipo")
    print("2. Buscar un equipo por su nombre y mostrar sus valores")
    print("3. Borarr un equipo a partir de su nombre")
    print("4.Listar todos los registros en forma de tabla")
    print("5. Salir")

    seleccion = int(input("Ingrese una opcion: "))

    if seleccion == 1:
        nombre = str(input("Introduce el nombre del equipo: "))
        pj = int(input("Introduzca los partidos jugados del equipo: "))
        v = int(input("Numero de partidos ganados: "))
        e = int(input("Numero de partidos empatados: "))
        d = int(input("Numero de partidos perdidos: "))
        gf = int(input("Numero de goles a favor: "))
        gc = int(input("Goles en contra: "))
        dg = gf - gc
        p = (v*3) + (e)

        try:
            diccionario[nombre] = (nombre,pj,v,e,d,gf,gc,dg,p)
            print("\nEquipo añadido correctamente\n")
        except:
            print("\nError al introducir el equipo\n")
    elif seleccion == 2:
        id = input("\nIntroduzca el nombre del equipo a borrar ")
        try:
            print(diccionario[id])
        except:
            print("\nNo se ha podido mostrar\n")
    elif seleccion == 3:
        id = input("\nIntroduce el nombre del equipo a borrar: ")
        try:
            del diccionario[id]
            print("\nEquipo borrado con exito\n")
        except:
            print("\nNo se ha podido borrar el equipo\n")
    elif seleccion == 4:
        print(diccionario)
    elif seleccion == 5:
        print("Saliendo....")
        exito = 1
    else:
        print("Ha escogido una opcion no contemplada")