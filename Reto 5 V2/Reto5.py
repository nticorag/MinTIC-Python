import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    with open('MSFT.csv',newline='') as elcsv:
        reader = csv.DictReader(elcsv)
        with open('analisis_archivo.csv','a',newline='') as newcsv:
            encabezados = ['Fecha','Mean-Min-Max','Concepto']
            writer = csv.DictWriter(newcsv,delimiter='\t',fieldnames=encabezados)
            writer.writeheader()
            date_lowest=''
            lowest_value=1000000
            date_highest=''
            highest_value=0
            for row in reader:
                #print(row['Date'],row['Open'],row['High'],row['Low'],row['Close'],row['Adj Close'],row['Volume'])
                concepto=''
                high=float(row['High'])
                if (high>highest_value):
                    highest_value=high
                    date_highest=row['Date']
                low=float(row['Low'])
                if (low<lowest_value):
                    lowest_value=low
                    date_lowest=row['Date']
                prom=(high+low)/2
                if (prom < 207):
                    concepto='MUY BAJO'
                elif (prom>=207 and prom<221):
                    concepto='BAJO'
                elif (prom>=221 and prom<235):
                    concepto='MEDIO'
                elif (prom>=235 and prom<249):
                    concepto='ALTO'
                elif (prom>=249):
                    concepto='MUY ALTO'

                writer.writerow({'Fecha':row['Date'],'Mean-Min-Max':prom,'Concepto':concepto})
               
    
    return date_lowest, lowest_value, date_highest, highest_value

solucion()