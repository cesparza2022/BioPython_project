import pandas as pd
import matplotlib.pyplot as plt
import argparse

#Se agrega el paso de argumentos
arg_parser = argparse.ArgumentParser(description="generar una grafica de pie con los diagnosticos de los donadores")

arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="archivo con datos de los donadores",
                    required=True)

args = arg_parser.parse_args()

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
