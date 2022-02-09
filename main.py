from tkinter import *
from tkinter.filedialog import askopenfilename
from Productos import Productos

def CargarData():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.data")])
    if pathString:
        openFile = open(pathString, 'r')
        fileString = openFile.read()
        print(fileString)
    root.destroy()

def CargarInstrucciones():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.lfp")])
    if pathString:
        openFile = open(pathString, 'r')
        fileString = openFile.read()
        print(fileString)
    root.destroy()



SeleccionarUsuario=0
def MenuInicial(SeleccionarUsuario):
    print("         Menu Ventas")
    print("==============================================")
    print("Pulse el numero correspondiente a la solicitud")
    print("")
    print("1. Leer Archivo de Ventas.")
    print("2. Leer Archivo de Instrucciones")
    print("3. Analizar")
    print("4. Reportes")
    print("5. Salir")
    print("")
    SeleccionarUsuario = int(input())
    return SeleccionarUsuario

    
SeleccionarUsuario=MenuInicial(SeleccionarUsuario)
if SeleccionarUsuario == 1:
    CargarData()
    SeleccionarUsuario=MenuInicial(SeleccionarUsuario)
elif SeleccionarUsuario == 2:
    CargarInstrucciones()
    SeleccionarUsuario=MenuInicial(SeleccionarUsuario)
elif SeleccionarUsuario == 3:
    
    SeleccionarUsuario=MenuInicial(SeleccionarUsuario)
elif SeleccionarUsuario == 4:
    
    SeleccionarUsuario=MenuInicial(SeleccionarUsuario)
elif SeleccionarUsuario == 5:
    print("Gracias por usar nuestro sistema, buen dia.")
    exit
else:
    print("")
    print("Ingrese una entrada valida")
    print("")
    MenuInicial(SeleccionarUsuario)

