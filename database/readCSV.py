## =================================================================== ##
#  this is file readCSV.py, created at 13-Aug-2016                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##


import csv
import os,shutil,glob
import datetime,unicodedata

directory =  '../content/projetos/'
directory_en =  '../content/projects/'
encoding = 'latin-1'

# removing all directories PT-BR
rm_dir = directory + "20*"
for path in glob.glob(rm_dir):
 shutil.rmtree(path)

# removing all directories EN
rm_dir_en = directory_en + "20*"
for path in glob.glob(rm_dir_en):
 shutil.rmtree(path)

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
 
   # Saved files PT_BR
   save_dir = directory + begin_year
   if not os.path.exists(save_dir):
    os.mkdir(save_dir)

   # Saved files EN
   save_dir_en = directory_en + begin_year
   if not os.path.exists(save_dir_en):
    os.mkdir(save_dir_en)
 
   file_pt = open(save_dir + '/' + agency + '-' 
                  + coordinator + '-' + str(count) + ".html",'w')
   file_pt.write("---\n")
   file_pt.write("Title: " + title + "\n")
   file_pt.write("Coordinator: " + coordinator + "\n")
   file_pt.write("Agency: " + agency + "\n")
   file_pt.write("Year: " + begin_year + "\n")
   file_pt.write("Modality: " + bid + "\n")
   nd = datetime.datetime.strptime(begin_date,'%m/%d/%y').strftime('%Y-%m-%d')
   file_pt.write("Created: !!timestamp '" + nd + " " 
                 + "10:00:00" + "'\n")
   file_pt.write("---\n")
   file_pt.close()

   file_en = open(save_dir_en + '/' + agency + '-' 
                  + coordinator + '-' + str(count) + ".html",'w')
   file_en.write("---\n")
   file_en.write("Title: " + title + "\n")
   file_en.write("Coordinator: " + coordinator + "\n")
   file_en.write("Agency: " + agency + "\n")
   file_en.write("Year: " + begin_year + "\n")
   file_en.write("Modality: " + bid + "\n")
   file_en.write("Created: !!timestamp '" + nd + " " 
                 + "10:00:00" + "'\n")
   file_en.write("---\n")
   file_en.close()

   count = count + 1
 
