#importamos librerias necesarias para el funcionamiento del codigp
import csv
import random


from ListaYdicc import *


# Asignacion de sueldo
def asignarSueldos():
    for trabajador in dicc_trabajadores:
        sueldo = random.randint(300000, 2500000)   # Random.radint para generar los sueldos entre 300.000 y 2.000.000
        dicc_trabajadores[trabajador] = sueldo   # Para encontrar la clave trabajor y usarla en los sueldos
    print('\nsueldos asignados')

    for trabajador in dicc_trabajadores:
        print(f'{trabajador} -${dicc_trabajadores[trabajador]}')   #vamos a imprimir cada trabajador con su respectivo sueldo

#Clasificamos
def clasificarSueldos():
    
    # 3 listas para que los datos no se acumulen y de error
    listaSueldoMenor = []   
    listaSueldoMedio = []
    listaSueldoMayor = []

    totalSueldos = sum(dicc_trabajadores[x] for x in dicc_trabajadores)   # Suma de los sueldos
    
    for trabajador in dicc_trabajadores:

        if dicc_trabajadores[trabajador] < 800000:   # Sueldos menores a 800.000
            listaSueldoMenor.append(trabajador)

        elif dicc_trabajadores[trabajador] >= 800000 and dicc_trabajadores[trabajador] < 2000000:   # Sueldos entre 800.000 y 2.000.000
            listaSueldoMedio.append(trabajador)

        elif dicc_trabajadores[trabajador] >= 2000000:   # Sueldos mayores a 2.000.000
            listaSueldoMayor.append(trabajador)
    print('\nsueldos clasificados')

    total = len(listaSueldoMenor) # Trabajadores con menos sueldo a 800.000

    print(f'\nSueldos menores a $800.000 -> TOTAL: {total}')
    
    for x in listaSueldoMenor:
        print(f'{x} -${dicc_trabajadores[x]}')   # Imprimimos el nombre junto al sueldo

    total = len(listaSueldoMedio)

    print(f'\nSueldos entre $800.000 y $2.000.000 -> TOTAL: {total}')

    for x in listaSueldoMedio:
        total = len(listaSueldoMedio)
        print(f'{x} -${dicc_trabajadores[x]}')

    total = len(listaSueldoMayor)

    print(f'\nSueldos mayores a $2.000.000 -> TOTAL: {total}')

    for x in listaSueldoMayor:
        total = len(listaSueldoMayor)
        print(f'{x} -${dicc_trabajadores[x]}')

    print(f'\nTotal suma sueldos: ${totalSueldos}')    #se imprime el sueldo total de la empresa

# Estadisticas
def estadisticas():
    sueldoMenor = min(dicc_trabajadores, key=dicc_trabajadores.get)
    sueldoMayor = max(dicc_trabajadores, key=dicc_trabajadores.get)
    promedioSueldos = sum(dicc_trabajadores.values()) / len(dicc_trabajadores)

    # Cálculo correcto de la media geométrica
    numeroElementos = len(dicc_trabajadores)
    productoSueldo = 1

    # Con esto nos ayudamos a poder resolver de mejor manera y entendible la media geometrica
    for sueldo in dicc_trabajadores.values():
        productoSueldo *= sueldo
    mediaGeometrica = productoSueldo ** (1 / numeroElementos)

    print(f'mostrar estadisticas')
    print(f'sueldo bajo: {sueldoMenor} -> ${dicc_trabajadores[sueldoMenor]}')
    print(f'sueldo mayor: {sueldoMayor} -> ${dicc_trabajadores[sueldoMayor]}')
    print(f'promedio de los sueldos: ${promedioSueldos}')
    print(f'media geometrica: ${mediaGeometrica}')

# Generamos el csv para usarlo como reporte al final
def reporte():
    with open('reporte_sueldos.csv', 'w') as file:   # Programa abierto en modo escritura
        write = csv.writer(file)
        write.writerow(['Nombre emmpleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo liquido'])   # Parametros

        for trabajador in dicc_trabajadores:

            descuentoSalud = dicc_trabajadores[trabajador] * 0.07   # Calculo del descuento de salud

            descuentoAfp = dicc_trabajadores[trabajador] * 0.12   # Calculo descuento afp

            descuentoSalud = round(descuentoSalud, 2)   # con round redondeamos el descuento de salud

            descuentoAfp = round(descuentoAfp, 2) # lo mismo con el de afp

            sueldoLiquido = dicc_trabajadores[trabajador] - descuentoSalud - descuentoAfp  # Calculamos el sueldo liquido. restando el descuento de salud y afp mas el sueldo bruto

            write.writerow([trabajador, dicc_trabajadores[trabajador], descuentoSalud, descuentoAfp, sueldoLiquido])   # con writerow agregamos los datos al cvs para crear la carpeta

    print('\nreporte generado con exito')
