import pandas as pd
import argparse 
import matplotlib.pyplot as plt
import numpy as np

def expression_graph():
  '''
  Funcion para graficar niveles de expresion 
  de los primeros 10 genes en las primeras 10 muestras.
  '''
  
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

  
  
def LOC_stat_graph():
  '''
  Funcion para graficar si cada donador de muestas
  tuvo alguna lesion cerebal a lo largo de su vida
  '''
  
  #Se abre el archivo del que se obtienen los datos con pandas
  donnor_data = pd.read_csv(args.FILE)

  #Se inicializan nuestras variables 
  data = []
  had_tbi = 0
  no_tbi = 0

  #Con un ciclo, se recorre el archivo
  for donnor in donnor_data.index:
      #Se revisa a que estado corresponde el dato en el campo que se recorre
      if (donnor_data["ever_tbi_w_loc"][donnor] == "Y"):
          #Se suma 1 al contador correspondiente al estado
          had_tbi += 1
      if (donnor_data["ever_tbi_w_loc"][donnor] == "N"):
          no_tbi += 1

  #Se guardan ambas variables en una lista
  data.append(had_tbi)
  data.append(no_tbi)

  #Se crea una lista con las dos clasificaciones en el orden correspondiente
  status = ["Tuvo lesion", "No tuvo lesion"]

  #Se inicializa la figura
  fig = plt.figure(figsize=(10,7))
  plt.pie(data, labels = status)

  plt.show()


  
def diagnostics_graph()::
  '''
  Funcion para graficar el diagnostico
  clinico de cada donador de muestras
  '''
  #Se abre el archivo usando pandas
  donnor_data = pd.read_csv(args.FILE)

  #Se inicializan nuestras variables y listas
  data = []
  NoDementia = 0
  VascularDementia = 0
  AlzheimerType = 0
  MultipleEtiologies = 0
  OtherMedical = 0
  Unkown = 0

  #Con un ciclom se recorre el archivo, obteniendo el diagnostico de cada donador de muestra
  for donnor in donnor_data.index:
      if (donnor_data["dsm_iv_clinical_diagnosis"][donnor] == "No Dementia"):
          #Se incrementa en 1 la variable correspondiente a cada clasificacion de diagnostico cuando esta se encuentra
          NoDementia += 1
      if (donnor_data["dsm_iv_clinical_diagnosis"][donnor] == "Vascular"):
          VascularDementia += 1
      if (donnor_data["dsm_iv_clinical_diagnosis"][donnor] == "Alzheimer's Disease Type"):
          AlzheimerType += 1
      if (donnor_data["dsm_iv_clinical_diagnosis"][donnor] == "Multiple Etiologies"):
          MultipleEtiologies += 1
      if (donnor_data["dsm_iv_clinical_diagnosis"][donnor] == "Other Medical"):
          OtherMedical += 1
      if (donnor_data["dsm_iv_clinical_diagnosis"][donnor] == "Other or Unknown Cause"):
          Unkown += 1

  #Se guardan los valores totales en una lista
  data.append(NoDementia)
  data.append(VascularDementia)
  data.append(AlzheimerType)
  data.append(MultipleEtiologies)
  data.append(OtherMedical)
  data.append(Unkown)

  #Se genera la lista de las clasificaciones de diagnosticos en el orden correspondiente
  diagnostics = ["No Dementia", "Vascular dementia", "Alzheimer's Disease Type", "Multiple Etiologies", "Other Medical", "Other or unkown"]

  #Se inicializa una gráfica de pie
  fig = plt.figure(figsize=(10,7))
  plt.pie(data, labels = diagnostics)

  plt.show()
