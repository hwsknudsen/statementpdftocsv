import tabula
import os
import csv
import pandas as pd
import math
import numpy as np


path = 'C:\Satements'
os.chdir(path)
obj = os.scandir(path)


#myfile = 'C:\Satements\1.csv'


for file in obj:
    if file.path.endswith('pdf'):

        opname = file.name.split('.')[0] + ".csv"
        f = open(opname,'w')
        f.write("Date, Inv No., Inv. Amount, P.O. No., Payments, Amt. Due, Bal. Fwd"+'\n')

        
        data = tabula.read_pdf(file, pages='all', multiple_tables=False, guess=False, area=[[300,18,714,590]], columns=[100,162,244,356,416,490], pandas_options={'header': None})
        df = pd.DataFrame(data[0])

        list = df.values.tolist()

        amtdue = 0;

        for x in range(len(list)):
            
            if str(list[x][5])!='nan':
                amtdue = list[x][5] + amtdue
                #print(amtdue)
            
            if list[x][0].startswith('Cust'):
                #for y in range(len(list[x])):
                list[x][0] = str(list[x][0])+str(list[x][1])+str(list[x][2])+str(list[x][3])+str(list[x][4])+str(list[x][5])+str(list[x][6])
                
                list[x][0] = list[x][0].replace("nan","") 
                list[x][1] = list[x][2] = list[x][3] = list[x][4] = list[x][5] = list[x][6] = ""

            for y in range(len(list[x])):
                if str(list[x][y]) == "nan":
                    list[x][y] = ""

            opstr = str(list[x]).replace("[","").replace("]","").replace("'","")

            #print(opstr)
            
            f.write(opstr+'\n')

        f.write("Conversion Check Sum: " + str(amtdue))
        print(amtdue)


        f.close()
        
        
