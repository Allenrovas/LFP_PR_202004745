from tkinter import *
from tkinter.filedialog import askopenfilename
from Productos import Productos
from os import system
import matplotlib.pyplot as plt
import numpy as np
Arregloproductos=[]
Anio = 0
Mes = ""
SeleccionarUsuario=0

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
        ArchivoOriginal = ArchivoOriginal.replace("\t","")
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
            TotalTemporal = PrecioTemporal*CantidadTemporal             
            NuevoProducto = Productos(NombreTemporal,PrecioTemporal,CantidadTemporal,TotalTemporal)
            Arregloproductos.append(NuevoProducto)

    root.destroy()
    

def CargarInstrucciones():
    global DiccionarioDatos
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.lfp")])
    if pathString:
        openFile = open(pathString, 'r')
        ArchivoInstrucciones = openFile.read()
        ArchivoInstrucciones = ArchivoInstrucciones.replace("\n","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("<","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace(">","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("¿","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("?","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("\t","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace("Â","")
        ArchivoInstrucciones = ArchivoInstrucciones.replace('"','')
        ArchivoInstrucciones = ArchivoInstrucciones.lower()
        DiccionarioDatos = {'nombre' : '','titulo' : '','titulox' : '','tituloy' : '','grafica' : ''} 
        DiccionarioDatos = dict((l.split(': ') for l in ArchivoInstrucciones.split(',')))
        print(DiccionarioDatos)
    root.destroy()

    if DiccionarioDatos['nombre']=='' or DiccionarioDatos['grafica']=='':
        DiccionarioDatos=""
        print("Faltan informacion obligatoria") 

def Analizar():
    global Arregloproductos
    DatosX=[]
    DatosY=[]
    j= len(Arregloproductos)

    if DiccionarioDatos['grafica']=='lineas':
        i=0
        for i in range(j):
            DatosX.append(Arregloproductos[i].nombre)
            DatosY.append(Arregloproductos[i].total)
            i+=1

        fig, ax = plt.subplots()

        ax.plot(DatosX,DatosY)
        
        if DiccionarioDatos['titulo'] != None:
            ax.set_title(str(DiccionarioDatos['titulo']))
        
        if DiccionarioDatos['tituloy'] != None:
            ax.set_ylabel(str(DiccionarioDatos['tituloy']))
        
        if DiccionarioDatos['titulox'] != None:
            ax.set_xlabel(str(DiccionarioDatos['titulox']))


        plt.savefig(str(DiccionarioDatos['nombre'])+'.png')
        system(str(DiccionarioDatos['nombre'])+'.png')
        
    elif DiccionarioDatos['grafica']=='barras':
        i=0
        for i in range(j):
            DatosX.append(Arregloproductos[i].nombre)
            DatosY.append(Arregloproductos[i].total)
            i+=1


        
        fig, ax = plt.subplots()

        ax.bar(DatosX, DatosY)

        if DiccionarioDatos['titulo'] != None:
            ax.set_title(str(DiccionarioDatos['titulo']))
        
        if DiccionarioDatos['tituloy'] != None:
            ax.set_ylabel(str(DiccionarioDatos['tituloy']))
        
        if DiccionarioDatos['titulox'] != None:
            ax.set_xlabel(str(DiccionarioDatos['titulox']))

        plt.savefig(str(DiccionarioDatos['nombre'])+'.png')
        system(str(DiccionarioDatos['nombre'])+'.png')
        
    elif DiccionarioDatos['grafica']=='pie' or DiccionarioDatos['grafica']=='pastel':
        i=0
        for i in range(j):
            DatosX.append(Arregloproductos[i].nombre)
            DatosY.append(int(Arregloproductos[i].total))
            i+=1

        fig, ax = plt.subplots()

        ax.pie(DatosY, labels = DatosX, autopct="%0.1f %%")
        
        if DiccionarioDatos['titulo'] != None:
            ax.set_title(str(DiccionarioDatos['titulo']))
        
        if DiccionarioDatos['tituloy'] != None:
            ax.set_ylabel(str(DiccionarioDatos['tituloy']))
        
        if DiccionarioDatos['titulox'] != None:
            ax.set_xlabel(str(DiccionarioDatos['titulox']))

        plt.savefig(str(DiccionarioDatos['nombre'])+'.png')
        system(str(DiccionarioDatos['nombre'])+'.png')
    else:
        print("Usted no ingreso un nombre válido para el gráfico")

def Reportes():
    print("Hola")

def MenuInicial():
    global SeleccionarUsuario
    SeleccionarUsuario=0
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
    if SeleccionarUsuario == 1:
        CargarData()
        MenuInicial()
    elif SeleccionarUsuario == 2:
        CargarInstrucciones()
        MenuInicial()
    elif SeleccionarUsuario == 3:
        Analizar()
        MenuInicial()
    elif SeleccionarUsuario == 4:
        Reportes()
        MenuInicial()
    elif SeleccionarUsuario == 5:
        print("Gracias por usar nuestro sistema, buen dia.")
        exit
    else:
        print("")
        print("Ingrese una entrada valida")
        print("")
        MenuInicial()
  

MenuInicial()

