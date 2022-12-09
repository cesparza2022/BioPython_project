# BioPython_project
## Análisis de expresión diferencial de materia gris y blanca en individuos lesiones cerebrales traumáticas
### **Integrantes**
César F. Esparza Alvarado  
Héctor Ulises Gaspar Eslava  
Natalia Gutierrez Ponce  

### **Introducción**  
Las lesiones cerebrales traumáticas son lesiones repentinas que causan daño en el cerebro, debido a impactos en la cabeza. Los efectos pueden ser de moderados a severos, dependiendo de los efectos de la lesión en las funciones cerebrales. Estas lesiones son la tercer causa de muerte y discapacidad en el mundo, y la primera en adolescentes. Igualmente, estas lesiones tienen efectos progresivos tales como secuelas neurológicas y casos de suicidio. 
Se ha encontrado que, posterior a una lesión severa, hay niveles elevados de expresión de APP3 (Proteína precursora amiloidea). En el caso de lesiones moderadas, se han encontrado niveles altos de deposición de especies de tau fosforilada en varias regiones cerebrales. Sin embargo, se sabe poco de los cambios a largo plazo y las implicaciones de las lesiones en los pronósticos médicos de los pacientes.   

### **Objetivos**
Analizar marcadores moleculares neuropatológicos en el transcriptoma de una cohorte de pacientes bien caracterizados. 
Comprender las bases moleculares de la neurodegeneración relacionada a lesiones cerebrales traumáticas. 

### **Metodología**  

1. Descargar los datos de expresión de la base de datos Aging, Dementia and TBI study (http://aging.brain-map.org/) 

2. Realizar un análisis de los datos recolectados, evaluando mediante gráficas que consideren la proscedencia de las muestras. 
   
2. Al manejar una base de datos con más de 50,000 genes y 377 muestras, lo primordial fue reducir estos valores, poniendo filltros para evaluar la divergencia entre estos genes y tomar solamente los que muestren información relevante. 
 
3. Realizar el análisis estadístico calculando el t_value y p_value de los genes que superaron el filtro, para de esta forma obtener la significancia de los datos con los que trabajamos.

4. Valorar los resultados con gráficas que describan esta expresión.

5. Evaluar la relación entre el origen de la muestra y los resultados con gráficas

### **Resultados**

Se descargó una carpeta con 4 archivos relacionados a los experimentos.  
El primer archivo *columns_samples2.csv* describe el origen de las muestras recolectadas, incluyendo columnas cómo: donor_id, structure_name, hemisphere, TBI_status, etc. 
![image](https://user-images.githubusercontent.com/100377746/206722981-03db4b38-51ec-49f1-9424-4a502f594678.png)
##### *fig.1 archivo columns_samples2.csv*

El segundo archivo *fpkm_table_normalized.csv* que contiene los valores normalizados de la expresión de los genes por muestra. 
![image](https://user-images.githubusercontent.com/100377746/206724870-11e8ff0e-44cf-40a3-9f49-28f968283ed7.png)
##### *fig.2 archivo fpkm_table_normalized.csv*

El tercer archivo *tbi_data_files.csv* incluye infromación relacionad con las muestras, incluyendo aspectos cómo: la integridad del rna, lecturasa totales de rna, porcentaje de rna alineado a lecturas de ncrna
![image](https://user-images.githubusercontent.com/100377746/206733039-3e2dc242-118e-40a5-90b1-289d2cbe791e.png)
###### *fig.3 archivo tbi_data_files.csv*  

El cuarto archivo *row-genes.csv* que contiene la informacion sobre los genes que fueron muestreados en este experimento. Incluyendo columnas cómo: chromosome, gene_etrez_id, gene_name, etc.
![image](https://user-images.githubusercontent.com/100377746/206734079-165f426b-1708-455f-80c1-ac45ee53de55.png)
###### *fig.4 archivo roe_genes.csv*


