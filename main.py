from tkinter import *
from tkinter.filedialog import askopenfilename
from Productos import Productos
Arregloproductos=[]
Anio = 0
Mes = ""

def CargarData():
    global Arregloproductos
    global Anio
    global Mes
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.data")])

    if pathString:
        openFile = open(pathString, 'r')
        ArchivoOriginal = openFile.read()
        ArchivoOriginal = ArchivoOriginal.replace(" ","")
        ArchivoOriginal = ArchivoOriginal.replace("\n","")
        ArchivoOriginal = ArchivoOriginal.replace("(","")
        ArchivoOriginal = ArchivoOriginal.replace(")","")
        ArchivoOriginal = ArchivoOriginal.replace('"','')
        ArchivoOriginal = ArchivoOriginal.replace('[','')
        ArchivoOriginal = ArchivoOriginal.replace(';','')
        PrimeraSeparacion = ArchivoOriginal.split('=')
        Fecha = PrimeraSeparacion[0]
        Ventas = PrimeraSeparacion[1]
        SegundaSeparacion = Fecha.split(':')
        Mes = SegundaSeparacion[0]
        Anio = SegundaSeparacion[1]
        TerceraSeparacion = Ventas.split(']')
        j=len(TerceraSeparacion)-1

        for i in range(j):
            CuartaSeparacion = TerceraSeparacion[i].split(',')
            NombreTemporal = CuartaSeparacion[0]
            PrecioTemporal = float(CuartaSeparacion[1])
            CantidadTemporal = int(CuartaSeparacion[2])              
            NuevoProducto = Productos(NombreTemporal,PrecioTemporal,CantidadTemporal)
            Arregloproductos.append(NuevoProducto)

    root.destroy()
    

def CargarInstrucciones():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.lfp")])
    if pathString:
        openFile = open(pathString, 'r')
        ArchivoInstrucciones = openFile.read()
        print(ArchivoInstrucciones)
        ArchivoInstrucciones = ArchivoInstrucciones.replace(" ","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("\n","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("<","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace(">","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("¿","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("?","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("\t","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("Â","")
        print(ArchivoInstrucciones)
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

