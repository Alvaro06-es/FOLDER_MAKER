import os
import time
from datetime import datetime
import calendar 
from babel.dates import format_date 
from deep_translator import GoogleTranslator

# this function create a folder between a year range, for each year create a month folders then for each month create a days and for each days can create a days files.

#función que crea carpetas a partir de un rango de años, por cada mes crea una carpeta , dentro de cada mes el archivo de cada día y luego un archivo con cada día.



def traducir(texto,idioma_out): # Function, depends on the user chocie, you can translate the text for this language:
    if idioma_out == "":
        idioma_out = "en"
        
    try:
        resultado = GoogleTranslator("auto",idioma_out).translate(texto)
        return resultado  #Return only the word in any language, depending on the user
    except Exception as b:
        print(f"An error has occurred on the translation {texto} to --> {idioma_out} ")
        time.sleep(10)
        exit()



def formato_fecha(fecha,formato):
    try:
        resultado = format_date(fecha,format="short", locale=formato)
        formato = resultado.replace("/","-")
        return formato
    except ValueError:
        resultado = format_date(fecha,format="short",locale="en")
        formato = resultado.replace("/","-")
        return formato
    
idioma = input("Choose a language for execute the script (default language: en):")
inicio = int(input(traducir("Start year folder for range:",idioma)))
final = int(input(traducir("End year folder for range :",idioma)))



modo_1 = input(traducir("Do you want to include all the days for each month? (¿Y/N?) (default: Y): ",idioma))
modo_2 = input(traducir("Do you want to exclude weekends? (¿Y/N?) (default: Y ): ",idioma))
Texto = input(traducir("¿Last one, what text do you want to write for each file on the day?, on this beautiful day (date) .... (your text): ",idioma))


print(traducir("................................Wait the result please..............................",idioma))


años = []

archivo = os.path.join(os.path.abspath(__file__))
ruta = os.path.join(archivo,"../DEFAULT") # we move on the home path
os.chdir(ruta)
print(f"{traducir("we are in",idioma)} {os.getcwd()}") #our path route
time.sleep(10)
        
def generador(inicio_interior,final_interior): 
    for año in range(inicio_interior,final_interior+1):
        años.append(año) #in range of year, create a folder with year.
    años_generados = list(set(años)) # we don't want a repeats.
    for carpeta_año in años_generados: # for each folder of year.
        
        
        #................................YEAR ZONE----------------------------------------------#
        carpeta_año = str(carpeta_año)
        os.mkdir(carpeta_año)# make year folder        
        os.chdir(carpeta_año) # change path on Year for next part of months
        for mes in range(1,13):
            guarro = f"01/{mes:02d}/{carpeta_año}"  #the mining of format 02d is that the first zero will inclue if the len of 2 charactes is not found, and the d for decimal number .
            para_mes = time.strptime(guarro,"%d/%m/%Y") # función para conseguir un formato de fecha deseado
            hecho_nombre = time.strftime("%B",para_mes)  #obtenemos el nombre de cada mes
            nombre_traducido = traducir(f" Month of {hecho_nombre}",idioma)
            nombre_fino_1 = nombre_traducido.strip()
            print(nombre_fino_1)
            nombre_fino_2 = nombre_fino_1.replace(f"{traducir('Month of ',idioma)}","")
            os.mkdir(nombre_fino_2)
            print(f"{traducir('folder',idioma)} {nombre_traducido} {traducir('of',idioma)} {carpeta_año} {traducir('created in',idioma)} {os.getcwd()} ")
            os.chdir(nombre_fino_2)
            fecha_fina = datetime(int(carpeta_año),int(mes),1)
            dia_max = calendar.monthrange(fecha_fina.year, fecha_fina.month)[1]
            for dia in range(1,dia_max):
                if modo_1.upper() != "N": # if the option is diferent than Not, then make a folder for each month.
                    str_fecha = f"{dia}-{mes}-{carpeta_año}"
                    condicion = datetime(int(carpeta_año),int(mes),int(dia))
                    carpeta_dia = formato_fecha(condicion,idioma) 
                    if modo_2.upper() != "N": # if the second option is diferent than N, then exclue all weekends, else include the weekends folders. 
                        if condicion.weekday() not in range(5,7): # if a folder name day not between in day 6 of saturday or day 7 of sunday, then exclude it. 
                            os.mkdir(carpeta_dia)
                            os.chdir(carpeta_dia)
                            with open(f"{traducir("Day",idioma)} {carpeta_dia}.txt","w",encoding="utf-8") as documento:
                                documento.write(f"{traducir("on the day",idioma)} {carpeta_dia}: {Texto}")
                            os.chdir("..") #return to month
                    else: # if user doesn't want weekend then, include all of the folders.
                        os.mkdir(carpeta_dia)
                        os.chdir(carpeta_dia)
                        with open(f"{traducir("Day",idioma)} {carpeta_dia}.txt","w",encoding="utf-8") as documento:
                            documento.write(f"{traducir("on the day",idioma)} {carpeta_dia}, {Texto}")
                        os.chdir("..") #return to current month.
            os.chdir("..") #return to  current year.
        os.chdir(ruta) #return to home folder.
        
    print(traducir("Thanks for using my program, Álvaro García",idioma))
print(f"{generador(inicio,final)}")