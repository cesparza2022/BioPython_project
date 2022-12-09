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

#### 1. Se descargó una carpeta con 4 archivos relacionados a los experimentos.  
El primer archivo *columns_samples2.csv* describe el origen de las muestras recolectadas, incluyendo columnas cómo: donor_id, structure_name, hemisphere, TBI_status, etc. 
![image](https://user-images.githubusercontent.com/100377746/206722981-03db4b38-51ec-49f1-9424-4a502f594678.png)
###### *fig.1 archivo columns_samples2.csv*

El segundo archivo *fpkm_table_normalized.csv* que contiene los valores normalizados de la expresión de los genes por muestra. 
![image](https://user-images.githubusercontent.com/100377746/206724870-11e8ff0e-44cf-40a3-9f49-28f968283ed7.png)
###### *fig.2 archivo fpkm_table_normalized.csv*

El tercer archivo *tbi_data_files.csv* incluye infromación relacionad con las muestras, incluyendo aspectos cómo: la integridad del rna, lecturasa totales de rna, porcentaje de rna alineado a lecturas de ncrna
![image](https://user-images.githubusercontent.com/100377746/206733039-3e2dc242-118e-40a5-90b1-289d2cbe791e.png)
###### *fig.3 archivo tbi_data_files.csv*  

El cuarto archivo *row-genes.csv* que contiene la informacion sobre los genes que fueron muestreados en este experimento. Incluyendo columnas cómo: chromosome, gene_etrez_id, gene_name, etc.
![image](https://user-images.githubusercontent.com/100377746/206734079-165f426b-1708-455f-80c1-ac45ee53de55.png)
###### *fig.4 archivo row_genes.csv*

#### 4. Análisis de muestras
![image](https://user-images.githubusercontent.com/100377746/206742359-c152c1a5-25f3-4b91-b486-8113a89b3a0b.png)
###### *fig.5 evaluación de los pacientes* 

![image](https://user-images.githubusercontent.com/100377746/206759565-a20024da-b281-47f3-b02d-71d1c808bed4.png)
###### *fig.6 estructura de la que salió la muestra*

![image](https://user-images.githubusercontent.com/100377746/206748717-f6e01096-40be-4aaf-956e-317996e29e2d.png)
###### *fig.7 grupo control contra grupo prueba*

#### 3. Se obtuvieron los genes con mayor relevancia 
Para esto se corrio el programa *filtro_1.py* que toma los arhcivos *fpkm_table_normalized.csv* y *columns_samples2.csv* y devuelve una lista de genes que pasaron el filtro y una lista con su factro de divergencia. 

El programa corre por gen en el archivo *fpkm_table_normalized.csv*, y evalua la expresión por muestra control o muestra prueba. De esta forma, por cada gen llena las listas *control* y *prueba*, a las que se les saca el promedio y se restan para encontrar la diferencia en expresión entre estos grupos. 



#### 4. Evaluación de la estadística 
Se calcularon el t-value y p-value de los genes que superaron el filtro 1 para ver su significacnia en la la lesión cerebral. 

#### 5. Evaluación de resultados 
![image](https://user-images.githubusercontent.com/100377746/206754234-7a7e73a8-c78b-4c84-a88a-234a287ee2e3.png)
##### *fig. 8 5 genes con mayor expresión*
Se puede ver que los niveles de expresión diferencial de estos genes son bastante similares, lo que inidca que existe una posible relación entre estos. También vale la pena mencionar, que dos de estos genes son factores de necrosis de tumor.


### **Conclusión**
Con este proyecto se puediron encontrar los genes que presentan una mayor expresión en casos de lesión cerebral. Para futuras investigaciones, valdría la pena buscar vías de señalización que relacionen estos genes y comparar con lo que se sabe sobre lesiones cerebrales. Dentro de los genes más expresados en el grupo prueba que en el grupo control, se encontraron dos factores de necrosis de tumor, por lo que suena lógico buscar algun vínculo entre la necrosis de tumores y las lesiones cerebrales


