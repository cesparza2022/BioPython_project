import pandas as pd
import argparse 
import matplotlib.pyplot as plt
import numpy as np

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

genes_list = genes_df["GeneID"].values.tolist()
gene_ids_list  = expr_df["gene_id \ rnaseq_profile_id"].values.tolist()
indexes = [(j) for i in range(0, 10) for j in range(len(gene_ids_list)) if genes_list[i] == gene_ids_list[j]]

genes_to_use = genes_list[:10]

frames = [expr_df.iloc[[f]] for f in indexes]
result = pd.concat(frames)
print(result)
#prueba = []
#control = []
expression_list = []
value = []


data_list = [(genes_to_use), (value)]
df = pd.DataFrame(data_list).T
df.columns = ['GeneID', ('Value')]
print(df)
for gen in result.index:
    for persona in range(0, 10):
        
        ## En el caso de que sea sujeto prueba se almacena el valor de la expresión del gen en la lista prueba
        if (base_df["TBI_status"][persona] == "Y"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            expression_list.append(float(result[pozo][gen]))
            #prueba.append(result[pozo][gen])
    
                
        ## En en el caso de que sea sujeto control se almacena el valor de la expresion del gen en la lista control
        if (base_df["TBI_status"][persona] == "N"):
            pozo = str(base_df["rnaseq_profile_id"][persona])
            expression_list.append(float(result[pozo][gen]))
            #control.append(result[pozo][gen])

n = 10
endlist = [[] for _ in range(n)]
for index, item in enumerate(expression_list):
    endlist[index % n].append(item)


x = np.arange(1, 11, 1)
plt.xlim(1, 11)
default_x_ticks = range(len(x))
plt.xticks(np.arange(0, 11, step = 1))

for list in endlist:
    y = list
    plt.plot(x, y, marker = '.')
plt.legend(genes_to_use)
plt.xlabel('Numero de muestra')
plt.ylabel('Nivel de expresion')
plt.title('Nivel de expresion de los primeros 10 genes en 10 muestras')
plt.show()
