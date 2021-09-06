# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 19:30:20 2021

@author: USUARIO
"""
#https://www.visualtk.com/

from parqueadero import *
from tkinter import *
from tkinter import messagebox

p = []
def crearParqueadero():
    try:
        global p
        p = Parqueadero(int(Pisos.get()),int(Espacios.get()),int(Motos.get()),int(Carros.get()))
        x = p.estadoParqueadero()
        resultado2.configure(text=x)
        messagebox.showinfo("Parqueadero","Parqueadero creado con éxito")
    except:
        messagebox.showinfo("Parqueadero","Ingrese la información solicitada")
        
def parquear():
    x = p.parqueaVehiculo(int(ePisos.get()), int(eEspacios.get()), int(seleccionado.get()), ePlaca.get())
    y = p.estadoParqueadero()
    resultado2.configure(text=y)
    messagebox.showinfo("Parqueadero",x)

window = Tk()
window.title("PARQUEADERO MisionTIC2022")
window.geometry('800x400')

#FRAMES 
inicio = Frame(window, bg="CadetBlue2", width=800, height=200)
inicio.grid(row=0)
pagina = Frame(window, bg="khaki1", width=800, height=200)
pagina.grid(row=1)
#FRAMES DE PAGINA
menu = Frame(pagina, bg="azure", width=390, height=190,pady=1)
menu.grid(row=0,column=0)
info = Frame(pagina, bg="lavender", width=390, height=190,pady=1)
info.grid(row=0,column=1)

#LABELS DE INICIO
label1 = Label(inicio,text="Ingrese información del parqueadero:")
label1.grid(row=0,columnspan=8,padx=20, pady=20)

#SOLICITUD PISOS
lblPisos = Label(inicio,text="Ingrese pisos:")
lblPisos.grid(row=1,column=1,padx=5, pady=5)
Pisos = Entry(inicio,width=10)
Pisos.grid(row=2,column=1,padx=5, pady=5)
#SOLICITUD ESPACIOS
lblEspacios = Label(inicio,text="Ingrese espacios:")
lblEspacios.grid(row=1,column=2,padx=5, pady=5)
Espacios = Entry(inicio,width=10)
Espacios.grid(row=2,column=2,padx=5, pady=5)
#SOLICITUD MOTOS
lblMotos= Label(inicio,text="Ingrese valor motos:")
lblMotos.grid(row=1,column=3,padx=5, pady=5)
Motos = Entry(inicio,width=10)
Motos.grid(row=2,column=3,padx=5, pady=5)
#SOLICITUD CARROS
lblCarros = Label(inicio,text="Ingrese valor carros:")
lblCarros.grid(row=1,column=4,padx=5, pady=5)
Carros = Entry(inicio,width=10)
Carros.grid(row=2,column=4,padx=5, pady=5)
#Bucle principal encargado de gestionar todos los eventos

#BOTON CREAR PARQUEADERO
crear2 = Button(inicio, text="Crear Parqueadero", bg="OliveDrab1", command=crearParqueadero)
crear2.grid(row=2,column=6,padx=5, pady=5)


#FRAMES LADO IZQUIERDO
crear = Frame(menu, bg="peach puff", width=400, height=200)
crear.grid(row=0)
botones = Frame(menu, bg="khaki1", width=400, height=200)
botones.grid(row=1)

#SOLICITUD PISOS
nota = Label(crear,text="Ingrese información del vehiculo a parquear")
nota.grid(row=0,columnspan=6,padx=5, pady=5)

uPisos = Label(crear,text="Piso")
uPisos.grid(row=1,column=1,padx=5, pady=5)
ePisos = Entry(crear,width=10)
ePisos.grid(row=2,column=1,padx=5, pady=5)
uEspacios = Label(crear,text="Espacio")
uEspacios.grid(row=1,column=2,padx=5, pady=5)
eEspacios = Entry(crear,width=10)
eEspacios.grid(row=2,column=2,padx=5, pady=5)
uPlaca = Label(crear,text="Placa")
uPlaca.grid(row=1,column=3,padx=5, pady=5)
ePlaca = Entry(crear,width=10)
ePlaca.grid(row=2,column=3,padx=5, pady=5)

frame_radios = Frame(crear)
seleccionado = IntVar()
rad1 = Radiobutton(frame_radios, text='Carro',  value=1, variable=seleccionado)
rad2 = Radiobutton(frame_radios, text='Moto', value=2, variable=seleccionado)
rad1.grid(column=1, row=6)
rad2.grid(column=1, row=7)
frame_radios.grid(column=4, row=2,padx=5, pady=5)


#BOTONES FRAME BOTONES
parquear = Button(botones, text="Parquear Vehiculo", bg="Orange2", command=parquear)
parquear.grid(row=0,column=0,padx=5, pady=5)

#FRAME LADO DERECHO
resultado2 = Label(info,text="Info")
resultado2.grid(row=1,column=0,padx=5, pady=5)

window.mainloop()