import os, pickle
from modelos import Producto

nombre = "Control de stock de una tienda."



def limpiar_pantalla():
    os.system("cls")

def continuar():
    print("")
    enter=input("Presione enter para continuar...")
    limpiar_pantalla()


limpiar_pantalla()

print(nombre)
print("")

productos={}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
datos = os.path.join(BASE_DIR, "productos.pkl")

def guardar_productos():
    with open(datos, "wb") as db:
        pickle.dump(productos, db)

def cargar_productos():
    global productos
    if os.path.exists(datos):
        with open(datos, "rb") as db:
            productos=pickle.load(db)

cargar_productos()

def nuevo_producto():
    limpiar_pantalla()
    nombre=input("Ingrese el nombre del producto: ")
    precio=int(input("Ingrese el precio del producto: "))
    stock=int(input("Ingrese el stock inicial: "))

    producto = Producto(nombre,precio,stock)
    productos[producto.nombre] = producto
    guardar_productos()
    print("Producto Guardado")
    continuar()

def ver_productos():
    limpiar_pantalla()
    print("-- Lista de productos --")
    print("")
    
    contador=1
    for producto in productos.values():
        print(f"{contador}. {producto.nombre}: ${producto.precio}, stock: {producto.stock}")
        contador+=1
    continuar()


def menu():
    print("-------- Menu Principal --------")
    print("")
    print("1. Ingresar nuevo producto.")
    print("2. Ver productos.")

    print("0. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion ==1:
        nuevo_producto()
    elif opcion==2:
        ver_productos()
    elif opcion ==0:
        quit()
    else:
        print("Opcion invalida. Intente nuevamente.")
        continuar()


while True:
    menu()

