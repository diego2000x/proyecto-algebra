import os

nombre = "Control de inventario de una panaderia"

def limpiar_pantalla():
    os.system("cls")

def continuar():
    enter=input("Presione enter para continuar...")
    limpiar_pantalla()

limpiar_pantalla()

print(nombre)

harina = 3500 #en gramos
agua = 6000 # en ml
sal = 1000 # en gr
levadura = 500 # en gr
azucar = 1000 # en gr

pan = 0

# un pan se hace con 300g de harina, 180 ml de agua, 3g de levadura, 6g de sal, y 5 g de azucar.

elementos = [harina, agua, sal, levadura, azucar]

def stock_ingredientes():

    print("")
    print("Ingredientes en stock:")
    print("")

    print(f"Hay {harina}gr de harina.")
    print(f"Hay {agua}ml de agua.")
    print(f"Hay {sal}gr de sal.")
    print(f"Hay {levadura}gr de levadura.")
    print(f"Hay {azucar}gr de azucar.")
    print("")

    print(f"Con esos ingredientes podemos hacer {calculo_panes()} panes.")
    continuar()


def pan_producible():
    global harina, agua, sal, levadura, azucar
    harina_actual= harina
    agua_actual=agua
    sal_actual=sal
    levadura_actual=levadura
    azucar_actual=azucar
    pan=0

    while harina_actual > 300 and agua_actual > 180 and sal_actual > 6 and levadura_actual > 3 and azucar_actual > 5:
        harina_actual-=300
        agua_actual-=180
        sal_actual-=6
        levadura_actual-=3
        azucar_actual-=5
        pan+=1

    print("")
    print(f"Podrias fabricar {pan} panes con los ingredientes actuales.")
    continuar()

def calculo_panes():
    global harina, agua, sal, levadura, azucar
    harina_actual= harina
    agua_actual=agua
    sal_actual=sal
    levadura_actual=levadura
    azucar_actual=azucar
    pan=0

    while harina_actual > 300 and agua_actual > 180 and sal_actual > 6 and levadura_actual > 3 and azucar_actual > 5:
        harina_actual-=300
        agua_actual-=180
        sal_actual-=6
        levadura_actual-=3
        azucar_actual-=5
        pan+=1

    return pan

def registro_panes_hechos():
    global harina, agua, sal, levadura, azucar
    produccion= int(input("Cuantos panes hizo hoy? Digite solo el numero: "))
    if harina > (produccion*300):
        if agua > (produccion*180):
            if sal > (produccion*6):
                if levadura > (produccion*3):
                    if azucar > (produccion*5):
                        harina-=(produccion*300)
                        agua-=(produccion*180)
                        sal-=(produccion*6)
                        levadura-=(produccion*3)
                        azucar-=(produccion*5)
                        print("")
                        print("Stock de ingredientes actualizado.")
                        pan_producible()
                    else:
                        print("Cantidad invalida, supera la cantidad de azucar del stock.")
                        print("Stock no actualizado.")
                        print("")
                else:
                    print("Cantidad invalida, supera la cantidad de levadura del stock.")
                    print("Stock no actualizado.")
                    print("")
            else:
                print("Cantidad invalida, supera la cantidad de sal del stock.")
                print("Stock no actualizado.")
                print("")
        else:
            print("Cantidad invalida, supera la cantidad de agua del stock.")
            print("Stock no actualizado.")
            print("")
    else:
        print("Cantidad invalida, supera la cantidad de harina del stock.")
        print("Stock no actualizado.")
        print("")
    continuar()

def cuantos_ingredientes():
    print("Cuantos panes quieres hacer?")
    numero=int(input("Digite el numero: "))
    print(f"Para hacer {numero} panes, necesitas: ")
    print(f"{numero*300}gr de harina, {numero*180}ml de agua, {numero*6}gr de sal, {numero*3}gr de levadura y {numero*5}gr de azucar.")
    continuar()



def menu():
    print("")
    print("-------- Menu Principal --------")
    print("")
    
    print("1. Ver stock de ingredientes. ")
    print("2. Cuantos panes se pueden hacer?")
    print("3. Ingresar panes preparados hoy.")
    print("4. Calcular la cantidad de ingredientes para hacer un numero de panes.")
    print("0. Para salir.")
    opcion= int(input("Digite una opcion: "))
    if opcion == 1:
        stock_ingredientes()
    elif opcion == 2:
        pan_producible()
    elif opcion ==3:
        registro_panes_hechos()
    elif opcion ==4:
        cuantos_ingredientes()
    elif opcion == 0:
        quit()
    else:
        print("Opcion invalida.")

while True:
    menu()

