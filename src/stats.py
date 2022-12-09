import pandas as pd
from scipy.stats import ttest_ind
import argparse 
import tsv
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
#ind_expr_df = pd.read_csv(args.FILE1, header = None)
base_df = pd.read_csv(args.FILE2)
genes_df = pd.read_csv(args.FILE3)

##Inicializar las listas
control = []
prueba = []
t_tests = []
genes_list = []

genes_list = genes_df["GeneID"].values.tolist()
gene_ids_list  = expr_df["gene_id \ rnaseq_profile_id"].values.tolist()

num_genes = len(genes_list)
num_gene_IDs = len(gene_ids_list)

indexes = [(j) for i in range(len(genes_list)) for j in range(len(gene_ids_list)) if genes_list[i] == gene_ids_list[j]]

frames = [expr_df.iloc[[f]] for f in indexes]
result = pd.concat(frames)

header = ['ID', 'T-value', 'P-value']
data = []


for gen in result.index:
    for persona in base_df.index:
        
        ## En el caso de que sea sujeto prueba se almacena el valor de la expresión del gen en la lista prueba
        if (base_df["TBI_status"][persona] == "Y"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            prueba.append(result[pozo][gen])
    
                
        ## En en el caso de que sea sujeto control se almacena el valor de la expresion del gen en la lista control
        if (base_df["TBI_status"][persona] == "N"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            control.append(result[pozo][gen])
    data.append(ttest_ind(prueba, control))
stats = pd.Series(data, index = indexes, name = 'Stats')

table = tabulate(stats, headers=header, tablefmt='orgtbl')
print(tabulate(table))
