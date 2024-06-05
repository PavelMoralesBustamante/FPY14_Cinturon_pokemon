import os
import msvcrt
import csv

#Cargar el CSV en una lista
pokemones = ""
with open('pokemon_primera_generacion.csv',newline='',encoding='utf-8') as a:
    datos = csv.reader(a, delimiter=',') #Capturamos la información del archivo
    pokemones = list(datos) #Guardamos la información en formato lista
#Lista para el cinturon
cinturon = []
#Comenzamos el sistema
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""\033[31m
    Sistema de gestión cinturón Pokémon
    ═══════════════════════════════════\033[0m
    1) Mostrar pokemones
    2) Buscar pokemon
    3) Agregar Pokemon al cinturón
    4) Mostrar Cinturón
    5) Quitar pokemon del cinturón
    6) Generar reporte del cinturón en un CSV
    0) Salir
    \033[31m═══════════════════════════════════\033[0m""")
    opcion = input("Seleccione : ")
    #Validamos la opción
    if opcion=="0":
        break
    elif opcion=="1":
        print("\033[33mListado 150 pokemones\033[0m")
        for p in pokemones:
            print(f"{p[0]} {p[1]} Tipo:{p[2]} Altura:{p[3]} Peso:{p[4]}kg")
    elif opcion=="2":
        print("\033[33mBuscar pokemon\033[0m")
        nombre = input("Ingrese nombre para buscar : ").title()
        centinela = False #Esta variable permite identificar si fue encontrado o no
        for p in pokemones:
            if nombre==p[1]: #Comparamos el nombre con la posición del nombre en la sublista
                print(f"\033[32mEncontrado: {p[0]} {p[1]} Tipo:{p[2]} Altura:{p[3]} Peso:{p[4]}kg")
                centinela = True #Cambia a verdadero si lo encontramos
                break
        if not centinela:
            print("\033[31mNombre no encontrado\033[0m")
    elif opcion=="3":
        print("\033[33mAgregar pokemon al cinturón\033[0m")
        #Validar que el cinturón tenga menos de 6 pokemones
        if len(cinturon)<6:
            nombre = input("Ingrese nombre de pokemon para agregar: ").title()
            centinela = False
            for p in pokemones:
                if nombre==p[1]:
                    #validar que el pokemon (p) no está registrado en el cinturón
                    if p not in cinturon:
                        cinturon.append(p)
                        print("\033[32mPokemon registrado\033[0m")
                    else:
                        print("\033[31mPokemon ya registrado en el cinturón\033[0m")
                    centinela = True
                    break
            if not centinela:
                print("\033[31mNombre no encontrado\033[0m")
        else:
            print("\033[31mNo hay espacio disponible en el cinturón\033[0m")
    elif opcion=="4":
        print("\033[33mMostrar cinturón\033[0m")
        if len(cinturon)>0: #Validamos si hay pkemones en el cinturón
            for i in range(len(cinturon)): #Recorremos la lista del cinturón por el índice i
                print(f"{i+1}.- {cinturon[i][1]} Tipo: {cinturon[i][2]}")
        else:
            print("\033[31mNo hay pokemones en el cinturón\033[0m")
    elif opcion=="5":
        print("\033[33mQuitar pokemon del cinturón\033[0m")
        if len(cinturon)>0:
            nombre = input("Ingrese nombre para quitar: ").title()
            centinela = False
            for p in cinturon:
                if nombre==p[1]:
                    cinturon.remove(p)
                    print("\033[32mPokemon liberado\033[0m")
                    centinela=True
                    break
            if not centinela:
                print("\033[31mNombre no encontrado\033[0m")
        else:
            print("\033[31mNo hay pokemones en el cinturón\033[0m")
    elif opcion=="6":
        print("\033[33mGenerar Reporte cinturón en CSV\033[0m")
        #Validar que hay pokemones en el cinturón
        if len(cinturon)>0:
            with open('reporte_cinturon.csv','w',newline='',encoding='utf-8') as a:
                escritura = csv.writer(a, delimiter=',')
                escritura.writerows(cinturon)
            print("\033[32mReporte Generado 📃\033[0m")
        else:
            print("\033[31mNo hay pokemones en el cinturón\033[0m")
    else:
        print("\033[31mOpción no valida\033[0m")
