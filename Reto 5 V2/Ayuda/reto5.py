import csv

def solucion():
  data = ["Fecha","Mean-Min-Max","Concepto"]
  with open("MSFT.csv","r") as csv_file:
    with open("analisis_archivo.csv","w") as salida_file:
      archivo_salida = csv.writer(salida_file,delimiter="\t")
      archivo = csv.reader(csv_file,delimiter=",")
      archivo_salida.writerow(data)
      contador_filas = 0
      promedio = 0
      concepto = ""
      fecha = ""
      date_lowest = ""
      lowest_value = 1000000
      date_highest = ""
      highest_value = -1000000
      for row in archivo:
          contador_filas += 1
          if (contador_filas > 1):
            if (float(row[3]) < lowest_value):
              lowest_value = float(row[3])
              date_lowest = row[0]
            if  (float(row[2]) > highest_value):
              highest_value = float(row[2])
              date_highest = row[0]
            fecha = row[0]
            promedio = (float(row[2]) + float( row[3]))/2

            if (promedio < 207):
              concepto = "MUY BAJO"
            elif (promedio >= 207 and promedio <221):
              concepto = "BAJO"
            elif (promedio >= 221 and promedio <235):
              concepto = "MEDIO"
            elif (promedio >= 235 and promedio < 249):
              concepto = "ALTO"
            elif (promedio >=249):
              concepto = "MUY ALTO"

            cadena_salida = [fecha, str(promedio), concepto]
            archivo_salida.writerow(cadena_salida)

    return date_lowest,lowest_value,date_highest,highest_value
          #print(fecha,promedio,concepto)
        
solucion()