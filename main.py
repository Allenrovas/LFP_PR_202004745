from tkinter import *
from tkinter.filedialog import askopenfilename
from Productos import Productos
from os import system, startfile
import matplotlib.pyplot as plt
import numpy as np
SeleccionarUsuario=0
Arregloproductos = []
ListaCantidadVendida = []
VerificacionDatos=False
VerificacionInstrucciones1=False
VerificacionInstrucciones2=False

def ordenamientoBurbuja(Lista):
  tamaño=len(Lista)
  i=0
  while i < tamaño - 1:
      j=0
      while j < tamaño - 1:
        if Lista[j].cantidad < Lista[j+1].cantidad:
          temp = Lista[j+1]
          Lista[j+1] = Lista[j]
          Lista[j] = temp
        j+=1
      i+=1

def ordenamientoBurbuja1(Lista):
  tamaño=len(Lista)
  i=0
  while i < tamaño - 1:
      j=0
      while j < tamaño - 1:
        if Lista[j].total < Lista[j+1].total:
          temp = Lista[j+1]
          Lista[j+1] = Lista[j]
          Lista[j] = temp
        j+=1
      i+=1

def CargarData():
    global Arregloproductos
    global Anio
    global Mes
    global VerificacionDatos
    global ListaCantidadVendida
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
        VerificacionDatos = True
        for i in range(j):
            CuartaSeparacion = TerceraSeparacion[i].split(',')
            NombreTemporal = CuartaSeparacion[0]
            PrecioTemporal = float(CuartaSeparacion[1])
            CantidadTemporal = int(CuartaSeparacion[2])
            TotalTemporal = PrecioTemporal*CantidadTemporal             
            NuevoProducto = Productos(NombreTemporal,PrecioTemporal,CantidadTemporal,TotalTemporal)
            Arregloproductos.append(NuevoProducto)
            ListaCantidadVendida.append(NuevoProducto)
        print("Se ha cargado el archivo de datos")
        print("")
    root.destroy()

def CargarInstrucciones():
    global DiccionarioDatos
    global VerificacionInstrucciones1
    global VerificacionInstrucciones2
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
        ArchivoInstrucciones = ArchivoInstrucciones.replace(' ','')
        ArchivoInstrucciones = ArchivoInstrucciones.lower() 
        DiccionarioDatos = dict((l.split(':') for l in ArchivoInstrucciones.split(',')))
        print("Se ha cargado el archivo de instrucciones")
        print("")
        try:
            DiccionarioDatos['nombre']
            VerificacionInstrucciones1=True
            DiccionarioDatos['nombre'] = DiccionarioDatos['nombre'].replace(" ",'')
        except:
            print("No ha ingresado nombre")
            print("")
            VerificacionInstrucciones1=False
        try:
            DiccionarioDatos['grafica']
            VerificacionInstrucciones2=True
        except:
            print("No ha ingresado tipo de gráfica")
            print("")
            VerificacionInstrucciones2=False
    root.destroy()

def Analizar():
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
        
        if hasattr(DiccionarioDatos, 'titulo'):
            ax.set_title(str(DiccionarioDatos['titulo']))
        else:
            SegundoTitulo= "Reporte de Ventas "+Mes+" - "+Anio
            ax.set_title(SegundoTitulo)

        if hasattr(DiccionarioDatos, 'tituloy'):
            ax.set_ylabel(str(DiccionarioDatos['tituloy']))
        
        if hasattr(DiccionarioDatos, 'titulox'):
            ax.set_xlabel(str(DiccionarioDatos['titulox']))
        
        print("Se ha generado la grafica de lineas")
        print("")


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

        if hasattr(DiccionarioDatos, 'titulo'):
            ax.set_title(str(DiccionarioDatos['titulo']))
        else:
            SegundoTitulo= "Reporte de Ventas "+Mes+" - "+Anio
            ax.set_title(SegundoTitulo)

        if hasattr(DiccionarioDatos, 'tituloy'):
            ax.set_ylabel(str(DiccionarioDatos['tituloy']))
        
        if hasattr(DiccionarioDatos, 'titulox'):
            ax.set_xlabel(str(DiccionarioDatos['titulox']))

        plt.savefig(str(DiccionarioDatos['nombre'])+'.png')
        system(str(DiccionarioDatos['nombre'])+'.png')

        print("Se ha generado la grafica de barras")
        print("")
        
    elif DiccionarioDatos['grafica']=='pie' or DiccionarioDatos['grafica']=='pastel':
        i=0
        for i in range(j):
            DatosX.append(Arregloproductos[i].nombre)
            DatosY.append(int(Arregloproductos[i].total))
            i+=1

        fig, ax = plt.subplots()

        ax.pie(DatosY, labels = DatosX, autopct="%0.1f %%")
        
        if hasattr(DiccionarioDatos, 'titulo'):
            ax.set_title(str(DiccionarioDatos['titulo']))
        else:
            SegundoTitulo= "Reporte de Ventas "+Mes+" - "+Anio
            ax.set_title(SegundoTitulo)

        if hasattr(DiccionarioDatos, 'tituloy'):
            ax.set_ylabel(str(DiccionarioDatos['tituloy']))
        
        if hasattr(DiccionarioDatos, 'titulox'):
            ax.set_xlabel(str(DiccionarioDatos['titulox']))

        plt.savefig(str(DiccionarioDatos['nombre'])+'.png')
        system(str(DiccionarioDatos['nombre'])+'.png')

        print("Se ha generado la grafica de pie")
        print("")

    else:
        print("Usted no ingreso un nombre válido para el gráfico")

def Reportes():
    global ListaCantidadVendida
    global Arregloproductos
    CuerpoHtml= """<!DOCTYPE html>
    <html lang=es>
    <head>
    <meta charset = "utf-8 ">
    <title>REPORTES</title>
    <style type = "text/css">
    body{
        margin: 0;
        font-family: Trebuchet MS, sans-serif;
        background-color: #fefbe9;
        background:linear-gradient(45deg,aqua,#02C7FF, #02A5FF , #0251FF , #022BFF, #6302FF,  #9402FF, #CA02FF ,#FF02F7);
    }
    .topnav {
        overflow: hidden;
        background-color: #DC143C;
        text-align: center;
    }
    table {
        border-collapse: collapse;
        width: 50%;
    }
    td, th {
        font-family: bahnschrift;
        border: 1px solid #000;
        text-align: center;
        padding: 8px;
    }
    h2{
        color: #000000;
    }</style>
    </head>
    <body>
    <div align="center" class="topnav"> 
        <h1 style = "color: black; ">REPORTE PRACTICA </h1>	</div><br><br>
        <div>
            <table align="center">
            <tr>
            <th colspan="2" style="background-color: Black; color: white;">Datos del Estudiante</th>
            </tr>
            <tr><th>Nombre</th> <th>Allen Giankarlo Roman Vasquez</th></tr>
            <tr><th>Carnet</th> <th>202004745</th></tr>
            </table>
            </div>
    <br></br>
    <div>
        <table align="center">
        <tr>
        <th colspan="3" style="background-color: Black; color: white;">Estadisticas de Productos</th>
        </tr>
        <tr>
        <th colspan="1"style="background-color: black; color: white;"</th>
        <th colspan="1"style="background-color: black; color: white;">Nombre</th>
        <th colspan="1"style="background-color: black; color: white;">Unidades vendidas</th>
        </tr>
        <tr><th colspan="1"style="background-color: black; color: white;">Producto mas vendido</th> <th>"""
    CuerpoHtml+= str(ListaCantidadVendida[0].nombre)+"""</th>"""
    CuerpoHtml+= """<th>"""+str(ListaCantidadVendida[0].cantidad)
    CuerpoHtml+= """</th></tr><tr><th colspan="1"style="background-color: black; color: white;">Producto menos vendido</th> <th>"""
    CuerpoHtml+= str(ListaCantidadVendida[-1].nombre)
    CuerpoHtml+= """<th>"""+str(ListaCantidadVendida[-1].cantidad)+"""</th>"""
    CuerpoHtml+= """</th></tr>
        </table>
        </div>
    <br></br>
    <table align="center">
    <tr>
    <th colspan="5" style="background-color: black; color: white;">Productos</th>
    </tr>
    <tr>
        <th colspan="1"style="background-color: black; color: white;">Nombre</th>
        <th colspan="1"style="background-color: black; color: white;">Precio</th>
        <th colspan="1"style="background-color: black; color: white;">Unidades vendidas</th>
        <th colspan="1"style="background-color: black; color: white;">Total Vendido</th>
    </tr>
    </tr>"""
    j= len(Arregloproductos)
    for i in range(j):
        CuerpoHtml+= """<tr class = "table-primary">"""
        CuerpoHtml+= """<th>"""+str(Arregloproductos[i].nombre)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(Arregloproductos[i].precio)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(Arregloproductos[i].cantidad)+"""</th>"""
        CuerpoHtml+= """<th>"""+str(Arregloproductos[i].total)+"""</th>"""
        CuerpoHtml+= """</tr>"""
    CuerpoHtml+="""</table>
    </div>
    </body>
    </html>"""
    ruta = str(DiccionarioDatos['nombre'])+'.html'
    archivo = open(ruta,'w')
    archivo.write(CuerpoHtml)
    startfile(str(DiccionarioDatos['nombre'])+'.html')
    print("Se ha generado el html con los reportes.")

def MenuInicial():
    global SeleccionarUsuario
    global DiccionarioDatos
    global VerificacionDatos
    global VerificacionInstrucciones1
    global VerificacionInstrucciones2
    global Arregloproductos
    global ListaCantidadVendida
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
        if VerificacionInstrucciones1==True and VerificacionDatos==True and VerificacionInstrucciones2==True:   
            Analizar()
        else:
            print("Usted no ha ingresado correctamente uno o más archivo")
        MenuInicial()
    elif SeleccionarUsuario == 4:
        if VerificacionDatos==True and VerificacionInstrucciones1==True:
            ordenamientoBurbuja1(Arregloproductos)
            ordenamientoBurbuja(ListaCantidadVendida)
            Reportes()
        else:
            print("Usted no ha ingresado un archivo")
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