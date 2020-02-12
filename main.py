import tabula
import os
import csv
import pandas as pd
import math
import numpy as np
import PyPDF2


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
        unappliedcredit = 0;

        for x in range(len(list)):
            
            if str(list[x][5])!='nan':
                amtdue = list[x][5] + amtdue
                #print(amtdue)

            if str(list[x][1]).startswith('- Unapplied Cred') or str(list[x][2]).startswith('napplied Cred'):
                unappliedcredit = list[x][6]
                #print(list[x][6])
            else:
                if str(list[x][0]).startswith('Cust'):
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

        pdfFileObj = open(file.name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        lastpage = pdfReader.getNumPages()
        #print(lastpage)

        data2 = tabula.read_pdf(file, pages="{}".format(lastpage), multiple_tables=False, guess=False, area=[[700,18,762,590]], columns=[100,200,285,365,460], pandas_options={'header': None})
        df2 = pd.DataFrame(data2[0])
        list2 = df2.values.tolist()

        #print(list2[1][5])

        f.write(str(list2[0]).replace("[","").replace("]","").replace("'","")+'\n')
        f.write(str(list2[1]).replace("[","").replace("]","").replace("'","")+'\n')

        Checksum = str(float(format(amtdue, '.2f')) + float(str(unappliedcredit).replace("'","").replace(" ","")))

        f.write("Conversion Check Sum: " + Checksum)
        #print(format(amtdue, '.2f'))


        f.close()
        pdfFileObj.close()

        a=float(Checksum)
        b=float(format(float(list2[1][5]), '.2f'))

        if a!=b:
            print("error"+str(file.name))
            input("Press Enter to continue...")
        else:
            print("no error "+str(file.name))

