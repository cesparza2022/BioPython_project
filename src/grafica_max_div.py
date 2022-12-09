import pandas as pd
from matplotlib import pyplot as plt
import argparse


#Hacemos el pase de argumentos en el que toma una lista de genes y una lista de el valor de divergencia de estos genes
arg_parser = argparse.ArgumentParser("Número de genes por cromosoma secuenciados")

arg_parser.add_argument("-l1", "--LIST1",
                    help="Lista de genes",
                    required=True)

arg_parser.add_argument("-l2", "--LIST2",
                    help="Lista con divergencia de genes",
                    required=True)



args = arg_parser.parse_args()


gen_list = args.LIST1
div_gen_list = args.LIST2

new_div_gen_list = [int(x) for x in div_gen_list] 

def max_div(gen,div_gen,num):
  div_gen2 = div_gen
  new_max_gen = []
  new_max_div = []
  for i in range(0,num):
    ind_gen_max = div_gen.index(max(div_gen))
    
    gen_max_num = gen[ind_gen_max]
    div_max_num = div_gen[ind_gen_max]
    
    new_max_gen.append(gen_max_num)
    new_max_div.append(div_max_num)
    
    div_gen2.remove((max(div_gen)))
     
    
  return new_max_gen, new_max_div
tuple_list = list(max_div(gen_list,div_gen_list,5))

new_genes = []
expr = []
for i in range(0,10):
  if i % 2 == 0: 
    new_genes.append(tuple_list[i])
   else:
    expr.append(tuple_list[i])

nums = [1, 2, 3, 4, 5]

  

plt.bar(nums, expr, abvr_genes = abvr_genes,
        width = 0.8, color = ['red', 'green',"blue","yellow","pink"])
  
plt.xlabel('abreviación del gen')
plt.ylabel("nivel de expresión")
plt.title('5 genes con mayor expresión')
plt.show()
 
  

  
