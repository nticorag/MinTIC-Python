from parqueadero import *
from tkinter import *
from tkinter import messagebox

usuarios = {"usuario":["Nicolas"],
            "password":["1234"]}

p=[]
def crearParqueadero():
    try:
        global p
        p = Parqueadero(int(Pisos.get()),int(Espacios.get()),int(Carros.get()),int(Motos.get()))
        x = p.estadoParqueadero()
        #crear.delete()
        resultados2.configure(text=x)
        
        messagebox.showinfo("Parqueadero","Parqueadero creado con éxito!")

        
    except:
        messagebox.showinfo("Alerta","Ingrese la informacion solicitada")

def parquear():
    try:
        x = p.parqueaVehiculo(int(enPisos.get()),int(enEspacios.get()),int(tseleccionado.get()),enPlaca.get())
        y = p.estadoParqueadero()
        resultados2.configure(text=y)
        messagebox.showinfo("Parqueadero","Todo bien")
    except:
        messagebox.showinfo("Alerta","Verifique informacion")

def pago():
    y = p.matriz[int(enPisos.get())][int(enEspacios.get())].pago()
    resultados2.configure(text=y)


def estado():
    x= p.estadoParqueadero()
    resultados2.configure(text=x)

def descargar():
    p.descargarInfo()
    messagebox.showinfo("Parqueadero","Informacion descargada")

def infoVehiculo():
    y = p.matriz[int(enPisos.get())][int(enEspacios.get())].info()
    resultados2.configure(text=y)

def mainParqueadero():
    global window
    window = Toplevel(login_screen) #se debe indicar que hace parte ed ootra ventana (la principal, la de login)
    window.title("Parqueadero Mision TIC2022") #Título de la ventana
    window.geometry('800x400') #Medidas de la ventana

    #FRAMES
    inicio = Frame(window, bg="CadetBlue2", width=800,height=200) #Creamos un marco dentro de la ventana, se le aplica un color y se da el tamaño
    inicio.grid(row=0) #se le asigna un espacio en la ventana, vista como una matriz

    pagina = Frame(window, bg="gray14", width=800,height=200) #Creamos un marco dentro de la ventana, se le aplica un color y se da el tamaño
    pagina.grid(row=1) #se le asigna un espacio en la ventana, vista como una matriz

    #FRAMES DE PAGINA

    menu = Frame(pagina, bg="azure", width=390,height=190,pady=1) #Creamos un marco dentro de la ventana, se le aplica un color y se da el tamaño
    menu.grid(row=0,column=0) #se le asigna un espacio en la ventana, vista como una matriz

    info = Frame(pagina, bg="lavender", width=390,height=190,pady=1) #Creamos un marco dentro de la ventana, se le aplica un color y se da el tamaño
    info.grid(row=0,column=1) #se le asigna un espacio en la ventana, vista como una matriz

    #LABELS
    label1 = Label(inicio,text='Ingrese información del parqueadero: ') #Se crea el label,y se le indica en que frame se ubica
    label1.grid(row=0,columnspan=8,padx=20,pady=20) #Se le indica en que posición del frame se ubica
    #Solicitud Piso
    lblpisos = Label(inicio,text='Ingrese pisos: ') #Se crea el label,y se le indica en que frame se ubica
    lblpisos.grid(row=1,column=1,padx=10,pady=10) #Se le indica en que posición del frame se ubica
    global Pisos
    Pisos = Entry(inicio,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    Pisos.grid(row=2,column=1,padx=10,pady=10) #Se indica la posición de la caja Pisos en el frame
    #Solicitud Espacios
    lblEspacios = Label(inicio,text='Ingrese espacios: ') #Se crea el label,y se le indica en que frame se ubica
    lblEspacios.grid(row=1,column=2,padx=10,pady=10) #Se le indica en que posición del frame se ubica
    global Espacios
    Espacios = Entry(inicio,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    Espacios.grid(row=2,column=2,padx=10,pady=10) #Se indica la posición de la caja Pisos en el frame
    #Solicitud Motos
    lblMotos = Label(inicio,text='Ingrese valor motos: ') #Se crea el label,y se le indica en que frame se ubica
    lblMotos.grid(row=1,column=3,padx=10,pady=10) #Se le indica en que posición del frame se ubica
    global Motos
    Motos = Entry(inicio,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    Motos.grid(row=2,column=3,padx=10,pady=10) #Se indica la posición de la caja Pisos en el frame
    #Solicitud Carros
    lblCarro = Label(inicio,text='Ingrese valor carros: ') #Se crea el label,y se le indica en que frame se ubica
    lblCarro.grid(row=1,column=4,padx=10,pady=10) #Se le indica en que posición del frame se ubica
    global Carros
    Carros = Entry(inicio,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    Carros.grid(row=2,column=4,padx=10,pady=10) #Se indica la posición de la caja Pisos en el frame

    #BOTON QUE CREA EL PARQUEADERO, LLAMA A LOS MÉTODOS
    crear2=Button(inicio,text="Crear parqueadero",bg="chocolate1",command=crearParqueadero)
    crear2.grid(row=2,column=6,padx=10,pady=10)

    ## FRAME MENU. LADO IZQUIERDO
    global crear
    crear = Frame(menu, bg="peach puff", width=400,height=200) #Creamos un marco dentro de la ventana, se le aplica un color y se da el tamaño
    crear.grid(row=0) #se le asigna un espacio en la ventana, vista como una matriz

    botones = Frame(menu, bg="khaki1", width=400,height=200) #Creamos un marco dentro de la ventana, se le aplica un color y se da el tamaño
    botones.grid(row=1) #se le asigna un espacio en la ventana, vista como una matriz

    #LABELS
    linfo = Label(crear,text="Ingrese información del vehículo a parquear:")
    linfo.grid(row=0,columnspan=6,padx=5,pady=5)
    #Solicitud Piso
    lbl_en_pisos = Label(crear,text='PISO') #Se crea el label,y se le indica en que frame se ubica
    lbl_en_pisos.grid(row=1,column=1) #Se le indica en que posición del frame se ubica
    global enPisos
    enPisos = Entry(crear,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    enPisos.grid(row=2,column=1) #Se indica la posición de la caja Pisos en el frame
    #Solicitud Espacios
    lbl_en_Espacios = Label(crear,text='ESPACIO') #Se crea el label,y se le indica en que frame se ubica
    lbl_en_Espacios.grid(row=1,column=2,padx=5,pady=5) #Se le indica en que posición del frame se ubica
    global enEspacios
    enEspacios = Entry(crear,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    enEspacios.grid(row=2,column=2,padx=5,pady=5) #Se indica la posición de la caja Pisos en el frame
    #Solicitud Placa
    lbl_en_Placa = Label(crear,text='Ingrese placa: ') #Se crea el label,y se le indica en que frame se ubica
    lbl_en_Placa.grid(row=1,column=3,padx=5,pady=5) #Se le indica en que posición del frame se ubica
    global enPlaca
    enPlaca = Entry(crear,width=10) #Se crea la caja de texto y se indica en que frame se ubica
    enPlaca.grid(row=2,column=3,padx=5,pady=5) #Se indica la posición de la caja Pisos en el frame


    #RADIOBUTTONS
    frame_radios = Frame(crear)
    global tseleccionado
    tseleccionado = IntVar()
    rad1 = Radiobutton(frame_radios, text='Carro',  value=1, variable=tseleccionado)
    rad2 = Radiobutton(frame_radios, text='Moto', value=2, variable=tseleccionado)
    rad1.grid(column=1, row=6)
    rad2.grid(column=1, row=7)
    frame_radios.grid(column=4, row=2,padx=5, pady=5)

    #BOTON QUE CARGA INFO, LLAMA A LOS MÉTODOS###
    bparquear=Button(botones,text="CARGAR INFO",bg="chocolate1",command=parquear)
    bparquear.grid(row=0,column=0,padx=5,pady=5)


    #BOTON DE ESTADO, LLAMA A LOS MÉTODOS###
    bestado=Button(botones,text="CONSULTAR ESTADO",bg="chocolate1",command=estado)
    bestado.grid(row=0,column=1,padx=5,pady=5)

    #BOTON DE PAGO, LLAMA A LOS MÉTODOS###
    bpago=Button(botones,text="PAGO",bg="chocolate1",command=pago)
    bpago.grid(row=1,column=0,padx=5,pady=5)

    #BOTON DE DESCARGA, LLAMA A LOS MÉTODOS###
    bdescarga=Button(botones,text="DESCARGAR",bg="chocolate1",command=descargar)
    bdescarga.grid(row=1,column=1,padx=5,pady=5)

    #BOTON DE CONSULTA, LLAMA A LOS MÉTODOS###
    bconsulta=Button(botones,text="CONSULTAR",bg="chocolate1",command=infoVehiculo)
    bconsulta.grid(row=2,padx=5,pady=5)


    #FRAME LADO DERECHO - BOTONES
    global resultados2
    resultados2 = Label(info,text="INFO")
    resultados2.grid(row=1,column=0,columnspan=6,padx=5,pady=5)


    #Bluce principal encargado de gestionar todos los eventos
    #window.mainloop()


def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    login_screen.mainloop()
 
# Implementing event on register button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if username1 in usuarios["usuario"]:
        if password1 in usuarios["password"]:
            mainParqueadero()
        else:
            messagebox.showinfo("Alerta","Contraseña incorrecta")
    else:
        messagebox.showinfo("Alerta","Usuario no encontrado")
 
 
# Designing popup for login success


login()