import tabula
import os
import csv
import pandas as pd
import math

path = 'C:\Satements'
os.chdir(path)
obj = os.scandir(path)


#myfile = 'C:\Satements\1.csv'


for file in obj:
    if file.path.endswith('pdf'):

        f = open('csvfile.csv','w')
        f.write("Date, Inv No., Inv. Amount, P.O. No., Payments, Amt. Due, Bal. Fwd"+'\n')

        
        data = tabula.read_pdf(file, pages='all', multiple_tables=False, guess=False, area=[[300,18,714,590]], columns=[100,162,244,356,416,490], pandas_options={'header': None})
        df = pd.DataFrame(data[0])

        list = df.values.tolist()

        for x in range(len(list)):
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

                #print(list[x])
            #if df.iloc[x][0].startswith('Cust'):
            #    #df.iloc[x][0].replace("test")
            #    print(df.iloc[x][0])



        f.close()
        
        #out = csv.writer(open("myfile1.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
        #out.writerows(list)
        #out.close()


                

        #df.to_csv(r'file')

    #print(data)



    #df.to_csv(r'C:\Satements\1.csv')
    
#tabula.convert_into_by_batch(path, output_format='csv', pages='all', pandas_options=None, multiple_tables=True)
