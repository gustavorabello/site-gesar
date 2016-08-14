## =================================================================== ##
#  this is file readCSV.py, created at 13-Aug-2016                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##


import csv
import os,shutil,glob
import datetime,unicodedata

directory =  '../content/projetos/'
count = 1

for filecsv in glob.glob('*.csv'):
 with open(filecsv) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
   process = row['Numero de processo']
   agency = row['Orgaos de Fomento']
   bid_type = row['Tipo']
   begin_year = row['Ano inicio']
   end_year = row['Ano fim']
   begin_date = row['Inicio']
   end_date = row['Fim']
   bid = row['Edital']
   title = row['Titulo do Projeto']
 
   initial_budget = row['Valor Pedido']
   budget = row['Valor Captado']
 
   coordinator = os.path.splitext(filecsv)[0]
 
   # Saved files 
   save_dir = directory + begin_year
   if not os.path.exists(save_dir):
    os.mkdir(save_dir)
 
   file = open(save_dir + '/' + agency + '-' + coordinator + '-' + str(count) + ".html",'w')
   file.write("---\n")
   file.write("Title: " + title + "\n")
   file.write("Coordinator: " + coordinator + "\n")
   file.write("Agency: " + agency + "\n")
   file.write("Year: " + begin_year + "\n")
   file.write("Modality: " + bid + "\n")
   nd = datetime.datetime.strptime(begin_date,'%m/%d/%y').strftime('%Y-%m-%d')
   file.write("Created: !!timestamp '" + nd + " " 
              + "10:00:00" + "'\n")
   file.write("---\n")
   file.close()
   count = count + 1
 
