def Menu():
    """Imprimimos las opciones por pantalla"""
    print("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Exponencial
6) Salir""")
def Calculadora():
    """Funcion que realizará la operación en función de la opción elegida"""
    Menu()
    opc = int(input("Selecione Opción "))
    while (opc<1 or opc>6):
        print("Elija una de las opciones del menú")
        Menu()
        opc = int(input("Selecione Opción "))
        while (opc >0 and opc <7):
            if (opc==6):
                print("Gracias por su atención")
                break
            else:
                x = float(input("Ingrese el Primer Operando "))
                y = float(input("Ingrese el Segundo Operando "))
                if (opc==1):
                    print("La Suma es: ", x+y)
                    Menu()
                    opc = int(input("Selecione Opción "))
                elif(opc==2):
                    print("La Resta es: ",x-y)
                    Menu()
                    opc = int(input("Selecione Opción "))
                elif(opc==3):
                    print("La Multiplicación es: ",x*y)
                    Menu()
                    opc = int(input("Selecione Opción "))
                elif(opc==4):
                    try:
                        print("La División es: ", x/y)
                        Menu()
                        opc = int(input("Selecione Opción "))
                    except ZeroDivisionError:
                        print("No se Permite la División Entre 0")
                        Menu()
                        opc = int(input("Selecione Opción "))
                elif(opc==5):
                    print(x," elevado a ",y," es ",x**y)
                    Menu()
                    opc = int(input("Selecione Opción "))
    else:
        while (opc >0 and opc <7):
            if (opc==6):
                print("Gracias por su atención")
                break
            else:
                x = float(input("Ingrese el Primer Operando "))
                y = float(input("Ingrese el Segundo Operando "))
                if (opc==1):
                    print("La Suma es: ", x+y)
                    Menu()
                    opc = int(input("Selecione Opción "))
                elif(opc==2):
                    print("La Resta es: ",x-y)
                    Menu()
                    opc = int(input("Selecione Opción "))
                elif(opc==3):
                    print("La Multiplicación es: ",x*y)
                    Menu()
                    opc = int(input("Selecione Opción "))
                elif(opc==4):
                    try:
                        print("La División es: ", x/y)
                        Menu()
                        opc = int(input("Selecione Opción "))
                    except ZeroDivisionError:
                        print("No se Permite la División Entre 0")
                        Menu()
                        opc = int(input("Selecione Opción "))
                elif(opc==5):
                    print(x," elevado a ",y," es ",x**y)
                    Menu()
                    opc = int(input("Selecione Opción "))
Calculadora()