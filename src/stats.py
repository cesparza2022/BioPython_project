'''
NAME
        stats.py
VERSION
        2.0
AUTHOR
        Hector Ulises Gaspar Eslava <hectorg@lcg.unam.mx>
DESCRIPTION
        Este programa contiene una funcion que realiza un análisis
        estadístico, T-test para evaluar si la diferencia
        de expresión de las diferentes muestras es significativa
        deacuerdo al grupo control.
CATEGORY
        Función 
USAAGE
       py src/stats.py -f1 path/to/file1 -f2 path/to/file2 -f3 path/to/file3 
GITHUB
        https://github.com/cesparza2022/BioPython_project/blob/main/src/stats.py
'''

import pandas as pd
from scipy.stats import ttest_ind
import argparse 
from tabulate import tabulate


arg_parser = argparse.ArgumentParser(description="obtener el valor estadístico de t_test")

arg_parser.add_argument("-f1", "--FILE1",
                    metavar="path/to/file1",
                    help="archivo con expresión génica",
                    required=True)

arg_parser.add_argument("-f2", "--FILE2",
                    metavar="path/to/file2",
                    help="Archivo datos del control",
                    required=True)

arg_parser.add_argument("-f3", "--FILE3",
                    metavar="path/to/file2",
                    help="Archivo genes seleccionados",
                    required=True)
        
args = arg_parser.parse_args()


## Hacer dataframes con los archivos de origen
expr_df = pd.read_csv(args.FILE1)
base_df = pd.read_csv(args.FILE2)
genes_df = pd.read_csv(args.FILE3)

##Inicializar las listas
control = []
prueba = []
t_tests = []
genes_list = []

#Se guardan los geneIDs seleccionados en el filtro anterior en una lista
genes_list = genes_df["GeneID"].values.tolist()
#Se guardan todos los geneIDs del experimento en otra lista
gene_ids_list  = expr_df["gene_id \ rnaseq_profile_id"].values.tolist()

#Se obtienen los indices de las columnas del archivo de datos de expresion donde se encuentran los genes del filtro anterior
indexes = [(j) for i in range(len(genes_list)) for j in range(len(gene_ids_list)) if genes_list[i] == gene_ids_list[j]]

#Se genera un nuevo dataframe unicamente con estas columnas
frames = [expr_df.iloc[[f]] for f in indexes]
result = pd.concat(frames)

#Se inicializa una lista como header y una lista vacia para usar
header = ['ID', 'T-value', 'P-value']
data = []

#Se recorre por gen el dataframe generado
for gen in result.index:
    #Se recorre el archivo con datos de control y prueba
    for persona in base_df.index:
        
        ## En el caso de que sea sujeto prueba se almacena el valor de la expresión del gen en la lista prueba
        if (base_df["TBI_status"][persona] == "Y"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            #Se guarda el valor de expresion en un vector correspondiente al grupo de prueba
            prueba.append(result[pozo][gen])
    
                
        ## En en el caso de que sea sujeto control se almacena el valor de la expresion del gen en la lista control
        if (base_df["TBI_status"][persona] == "N"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            #Se guarda el valor de expresion en un vector correspondiente al grupo de prueba
            control.append(result[pozo][gen])
    #En un vector se guardan los t_tests de cada uno
    data.append(ttest_ind(prueba, control))

#Se genera una tabla con los estadisticos
stats = pd.Series(data, index = indexes, name = 'Stats')

table = tabulate(stats, headers=header)

#Se guarda la tabla en un archivo
with open (t-tests.txt', 'w') as file
           file.write(table)

