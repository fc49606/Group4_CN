import numpy as np
import csv
from datetime import datetime

f = open("ratings_alterado.csv","w+")#utf8  cp1252
with open("ratings.csv", "r",encoding="utf8") as file_obj:
    '''file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)'''
    for linha in file_obj:
        teste = linha.split(",")  
        f.write(str(teste[1])+","+str(teste[2])+"\n")
        


  