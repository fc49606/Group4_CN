import numpy as np
import csv
from datetime import datetime

f = open("movies_metadata_alterado.csv","w+")#utf8  cp1252
with open("movies_metadata.csv", "r+",encoding="utf8") as file_obj:
    '''file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)'''
    for linha in file_obj:
        teste = linha.split(";")  
        date_time_obj = datetime.strptime(teste[3], '%d/%m/%Y')
        date_time_obj = date_time_obj.date()
        teste[3] = str(date_time_obj)
        print(teste)
        f.write(str(teste[0])+";"+str(teste[1])+";"+str(teste[2])+";"+str(teste[3])+";"+str(teste[4])+";"+str(teste[5])+";"+str(teste[6]))
        


  