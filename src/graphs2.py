import pandas as pd
from matplotlib import pyplot as plt
import argparse

def max_div(gen,div_gen,num):
  # se hace una copia de la lista de divergencia
  div_gen2 = div_gen
  # se inicializan las listas 
  new_max_gen = []
  new_max_div = []
  
  #empieza el ciclo por la cantidad de genes que queramos 
  for i in range(0,num):
    #se busca el indice del numero de expresion maxima es la lista de diveregencia
    ind_gen_max = div_gen.index(max(div_gen))
    
    #se encuentra el gen al que pertence este valor expresion 
    gen_max_num = gen[ind_gen_max]
    #se obtiene el valor de divergencia 
    div_max_num = div_gen[ind_gen_max]
    
    #se agragan a sus respectivas listas 
    new_max_gen.append(gen_max_num)
    new_max_div.append(div_max_num)
    
    #se quita el valor de la lista original 
    div_gen2.remove((max(div_gen)))
     
   #devueleve una dupla 
  return new_max_gen, new_max_div

def max_div_to_list(gen_list,div_gen_list,num):
  #corremos la función para obtener la dupla de los genes y la expresion 
  tuple_list = list(max_div(gen_list,div_gen_list,5))

  #inicializamos las listas
  new_genes = []
  expr = []
  
  #Empezamos el loop 
  for i in range(0,10):
    #Si es par va a corresponder a un gen 
    if i % 2 == 0: 
      #se almacena en la lista de genes 
      new_genes.append(tuple_list[i])
    else:
      # si no es par se almacena en expr
      expr.append(tuple_list[i])
  #para graficar se hace el vector nums por los valores de x
  nums = [1, 2, 3, 4, 5]
  
  #se hace la grafica de barras con los vectores de los genes 
  plt.bar(nums, expr, new_genes = new_genes,
        width = 0.8, color = ['red', 'green',"blue","yellow","pink"])
  
  #se nombran los ejes
  plt.xlabel('abreviación del gen')
  plt.ylabel("nivel de expresión")
  #se nombra la grafica
  plt.title('5 genes con mayor expresión')
  plt.show()

  
def cromosoma_gen(archivo):
  #leer el archivo csv 
  crom_gen = pd.read_csv(archivo)
  #empezar el contador y la lista
  n = 1
  gen_crom = []
  cromosomas = ["1","2","3","4","5","6","7","8","9" 
              ,"10","11","12","13","14","15","16"
              ,"17","18","19","20","21","22","X",
              "Y","MT"]
  #empezar el loop por cromosoma
  for gen in crom_gen_df.index:
    #si cambiamos de cromosoma se corta el contador y se guarda la cantidad de genes 
    if (crom_gen_df["chromosome"][gen] != cromosomas[n]):
      gen_crom.append(gen)
      n = n +1
      
  #Graficar tomando
  plt.bar(cromosomas, gen_crom = gen_crom)
  plt.xlabel('cromosoma')
  plt.ylabel("numero de genes")
  plt.title('genes por cromosoma')
  plt.show()
   
def estruct_muestra(archivo):
  #se lee el archivo 
  dataset_df = pd.read_csv(archivo)
  #se transforma a una lista la columna del archivo 
  str_col = dataset_df["structure_name"].values.tolist()
 
  #se inicializa la lista
  num_estr = []
  
  #contamos la cantidad de muestras por estructura
  tmp_crt = str_col.count("temporal neocortex")
  w_mtr = str_col.count("white matter of forebrain")
  hipp = str_col.count("hippocampus (hippocampal formation)")
  par_neo = str_col.count("parietal neocortex")
   
  #arreglamos en forma de lista
  num_estr.append(tmp_crt,w_mtr,hipp,par_neo)
  
  #Graficar 
  plt.bar(cromosomas, gen_crom = abvr_genes)
  plt.xlabel('cromosoma')
  plt.ylabel("numero de genes")
  plt.title('genes por cromosoma')
  plt.show()
   
  
  
  
  
  
  
  
  
