import numpy as np
import csv
from datetime import datetime

f = open("movies_metadata_corrigido_1.csv","w+")#utf8  cp1252
with open("movies_metadata.csv", "r+",encoding="utf8") as file_obj:
    '''file_data = csv.DictReader(file_obj, skipinitialspace = True)
    file_list = list(file_data)'''
    for linha in file_obj:
        teste = linha.split(";")
        aux = teste[3].split("/")
        f.write(str(teste[0])+";"+str(teste[1])+";"+str(teste[2])+";"+str(aux[2])+";"+str(teste[4])+";"+str(teste[5])+";"+str(teste[6]))
        


  