import pandas as pd
from scipy import stats
import argparse 
from tabulate import tabulate
import tsv
from statistics import mean

arg_parser = argparse.ArgumentParser(description="obtener el valor estadístico de t_test")

arg_parser.add_argument("-f1", "--FILE1",
                    metavar="path/to/file1",
                    help="archivo con expresión génica",
                    required=True)

arg_parser.add_argument("-f2", "--FILE2",
                    metavar="path/to/file2",
                    help="Archivo datos del control",
                    required=True)

        
args = arg_parser.parse_args()


## Hacer dataframes con los archivos de origen
base_df = pd.read_csv(args.FILE2)
expr_df = pd.read_csv(args.FILE1)

##Inicializar las listas
control = []
prueba = []
div_val = []
genes = []

for gen in expr_df.index:
    for persona in base_df.index:
    
        ## En el caso de que sea sujeto prueba se almacena el valor de la expresión del gen en la lista prueba
        if (base_df["TBI_status"][persona] == "Y"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            prueba.append(expr_df[pozo][gen])
   
            
        ## En en el caso de que sea sujeto control se almacena el valor de la expresion del gen en la lista control
        if (base_df["TBI_status"][persona] == "N"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            control.append(expr_df[pozo][gen])
   
    mean_control = (mean(control))
    mean_prueba = (mean(prueba))
    
    if (mean_control > mean_prueba and mean_control - mean_prueba > 3 ):
        genes.append(expr_df["gene_id \ rnaseq_profile_id"][gen])
        div_val.append(mean_control - mean_prueba)
    
    if (mean_prueba > mean_control and mean_prueba - mean_control > 3 ):
        genes.append(expr_df["gene_id \ rnaseq_profile_id"][gen])
        div_val.append(mean_prueba - mean_control)
    control = []
    prueba = []

        
 with open("data/results.tsv", 'w', encoding='utf8', newline='') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        tsv_writer.writerow(["gen", "divergencia"])
        for gen in genes:
            tsv_writer.writerow([gen, div_val])

