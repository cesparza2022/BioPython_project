import pandas as pd
from matplotlib import pyplot as plt
import argparse

arg_parser = argparse.ArgumentParser("Número de genes por cromosoma secuenciados")

arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="archivo con expresión génica",
                    required=True)

args = arg_parser.parse_args()


## Hacer dataframes con los archivos de origen
crom_gen_df = pd.read_csv(args.FILE)


##Hacer el loop para recuperar que recorra el numero de rows por columna 
n = 1
gen_crom = []
cromosomas = ["1","2","3","4","5","6","7","8","9"        ,"10","11","12","13","14","15","16","17","18","19"
,"20","21","22","X","Y","MT"]

for gen in crom_gen_df.index:
  if (crom_gen_df["chromosome"][gen] != cromosomas[n]):
    gen_crom.append(gen)
    n = n +1


  
