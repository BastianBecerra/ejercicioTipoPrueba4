from funciones import *

#definimos variables para su uso posterios (buenas practicas)
key = 0
sueldo = 0


#inicio del menu
while True:
    print('\n--> SUELDOS DE EMPLEADOS <--')
    print("1- Asignar sueldos aleatorio")
    print("2- Clasificacion de sueldos")
    print("3- Estadisticas")
    print("4- Reporte")
    print("5- Exit")


    try: key = int(input('\ningrese una opcion: ')) #Almacena dentro de la variable key
    except Exception: print('ingrese una opcion valida')

    # Opciones

    if key == 1:   
        asignarSueldos()

    elif key == 2:
        clasificarSueldos()

    elif key == 3:
        estadisticas()

    elif key == 4:
        reporte()

    # Fin del examen
    elif key == 5:
        print('Fin \nDesarrollado por Bastian Becerra\nRUT 20.227.420-k')
        break