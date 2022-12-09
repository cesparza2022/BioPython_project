import pandas as pd
import matplotlib.pyplot as plt
import argparse


arg_parser = argparse.ArgumentParser(description="generar una grafica de pie con cantidades de controles y muestras experimentales")
#Se inicializa el paso de argumentos del programa
arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="archivo con datos de los donadores",
                    required=True)

args = arg_parser.parse_args()

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

