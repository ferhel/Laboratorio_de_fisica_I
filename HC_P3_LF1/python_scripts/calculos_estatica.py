import pandas as pd
import os
import numpy as np
from scipy import stats

dir_archivo= os.path.dirname(os.path.abspath(__file__))
ruta_csvestat= os.path.join(dir_archivo, 'masa_resorte_estatico.csv')
#invocar csv'
df_estatico = pd.read_csv(ruta_csvestat, sep=',', decimal='.')  

#Convertir g a kg para añadir masa_kg y g
df_estatico['masa_kg'] = df_estatico['masa_g'] / 1000

#Convertir de cm a metros para añadir posicion_m

df_estatico['posicion_m'] = df_estatico['posicion_cm'] / 100

#------------------------

#Calcular k 
#------------------------
incertidumbre_g = 0.01
g = 9.78

# datos a np

masa = np.array([df_estatico['masa_kg']])
posicion = np.array([df_estatico['posicion_m']])

#calculo regresion lineal 

