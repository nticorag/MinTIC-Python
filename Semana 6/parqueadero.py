import datetime
import csv
 
class Vehiculo:
    def __init__(self,placa):
        self.placa = placa
        self.ingreso = datetime.datetime.now()
    def info(self):
        #t='{%d %m %y %H %M }'.format(self.ingreso)
        t=self.ingreso.strftime("%d-%m-%y %H:%M")
        return f"El vehiculo con placa {t}, fecha de ingreso: {t}"
 
 
class Moto(Vehiculo):
    precio = 0
    def __init__(self,placa):
        super().__init__(placa)
 
    def info(self):
        return f"Moto - {super().info()}"
 
    def pago(self):
        hoy = datetime.datetime.now()
        t = hoy - self.ingreso
        m = round(t.total_seconds()/60,2)
        p = round(m * Moto.precio,2)
        return f"La MOTO de placa {self.placa} lleva {m} minutos \n TOTAL PAGAR: {p} $COP"
 
class Carro(Vehiculo):
    precio = 0
    def __init__(self,placa):
        super().__init__(placa)
 
    def info(self):
        return f"Carro - {super().info()}"
 
    def pago(self):
        hoy = datetime.datetime.now()
        t = hoy - self.ingreso
        m = round(t.total_seconds()/60,2)
        p = round(m * Carro.precio,2)
        return f"El CARRO de placa {self.placa} lleva {m} minutos \n TOTAL PAGAR: {p} $COP"

class Parqueadero:
  def __init__(self,pisos,espacios,vcarros,vmoto):
    self.p = pisos
    self.e = espacios
    self.vc = vcarros #precio x minuto carro
    self.vm = vmoto #precio x minuto moto
    Carro.precio= vcarros
    Moto.precio=vmoto
    self.matriz = [[0] * espacios for i in range(pisos)]

  def imprimeVacios(self):
    x =""
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[0])):
        if (self.matriz[i][j]==0):
          x = x + f"Piso {i}, Espacio {j} -> Está vacío, \n"
    return x

  def parqueaVehiculo(self,p,e,t,pl):
    try:
      if (self.matriz[p][e]==0):
        if (t==1):
          self.matriz[p][e] = Carro(pl)
        elif (t ==2):
          self.matriz[p][e] = Moto(pl)
        else:
          return "Opción desconocida"
      else:
        return "LUGAR NO DISPONIBLE"
    except IndexError:
      return "Piso y espacio ingresado no existe"

  def estadoParqueadero(self):
    x=""
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz[0])):
        if (self.matriz[i][j]==0):
          x= x+ f"Piso {i}, Espacio {j} -> Está vacío \n"
        else:
          x=x+ f"Piso {i}, Espacio {j} -> {self.matriz[i][j].info()}, \n"
    return x

  def descargarInfo(self):
    with open('Descargue.csv','a',newline='') as file:
      writer= csv.writer(file)
      for i in range(len(self.matriz)): #TODO ESTE CICLO DEBE ESTAR DENTRO DEL WITH
        for j in range(len(self.matriz[0])):
         if (self.matriz[i][j]==0):
           writer.writerow([f"Piso {i}, Espacio {j} -> Está vacío \n"])
         else:
           writer.writerow([f"Piso {i}, Espacio {j} -> {self.matriz[i][j].info()}, \n"])
    # writerow es para guardar FILAS TODO EL CONTENIDO
    # writerows es para guardar COLUMNAS, SEPRADO POR COLUMNAS
      # for i in self.matriz:
      #   writer.writerow([i])

""" x = Parqueadero(4,3,5000,2000)
print(x.imprimeVacios())
x.parqueaVehiculo(1,1,1,"FRT2342")
x.parqueaVehiculo(0,0,2,"gty432")
print(x.parqueaVehiculo(0,0,2,"gty432"))
print(x.estadoParqueadero())

x.descargarInfo()
 """