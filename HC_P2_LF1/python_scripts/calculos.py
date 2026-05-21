import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datos_brutos as db
from utils import redondear


#------------------------------------
#Promedio de Dimensiones
#------------------------------------

#CORCHO
largo_corcho_promedio = np.mean(db.df_bruto_corcho['Largo_cm'])
diametro_corcho_promedio = np.mean(db.df_bruto_corcho['Diámetro_cm'])

largo_corcho_promedio_redondeado = redondear(largo_corcho_promedio, 3)
diametro_corcho_promedio_redondeado = redondear(diametro_corcho_promedio, 3)

#CILINDRO PLATEADO
largo_cilindro_plata_promedio = np.mean(db.df_bruto_cilindro_plata['Largo_cm'])
diametro_cilindro_plata_promedio = np.mean(db.df_bruto_cilindro_plata['Diámetro_cm'])   

largo_cilindro_plata_promedio_redondeado = redondear(largo_cilindro_plata_promedio, 3)
diametro_cilindro_plata_promedio_redondeado = redondear(diametro_cilindro_plata_promedio, 3)    

#CILINDRO DORADO
largo_cilindro_dorado_promedio = np.mean(db.df_bruto_cilindro_dorado['Largo_cm'])
diametro_cilindro_dorado_promedio = np.mean(db.df_bruto_cilindro_dorado['Diámetro_cm'])     

largo_cilindro_dorado_promedio_redondeado = redondear(largo_cilindro_dorado_promedio, 3)
diametro_cilindro_dorado_promedio_redondeado = redondear(diametro_cilindro_dorado_promedio, 3)  

#CILINDRO HUECO
largo_cilindro_hueco_promedio = np.mean(db.df_bruto_cilindro_hueco['Largo_cm'])
diametro_externo_cilindro_hueco_promedio = np.mean(db.df_bruto_cilindro_hueco['Diámetro_externo_cm'])
diametro_interno_cilindro_hueco_promedio = np.mean(db.df_bruto_cilindro_hueco['Diámetro_interno_cm'])

largo_cilindro_hueco_promedio_redondeado = redondear(largo_cilindro_hueco_promedio, 3)
diametro_externo_cilindro_hueco_promedio_redondeado = redondear(diametro_externo_cilindro_hueco_promedio, 3)
diametro_interno_cilindro_hueco_promedio_redondeado = redondear(diametro_interno_cilindro_hueco_promedio, 3)    

#MONEDA

espesor_moneda_promedio = np.mean(db.df_bruto_moneda['Espesor_cm'])
diametro_moneda_promedio = np.mean(db.df_bruto_moneda['Diámetro_cm'])   
diametro_moneda_promedio_redondeado = redondear(diametro_moneda_promedio, 3)
espesor_moneda_promedio_redondeado = redondear(espesor_moneda_promedio, 4)

#------------------------------------
#CÁLCULOS DE VOLUMEN (cm³)
# ------///------ {CORCHO} ------///------

radio_corcho = diametro_corcho_promedio/ 2
altura_corcho = largo_corcho_promedio
volumen_corcho_promedio = np.pi * (radio_corcho ** 2) * altura_corcho
volumen_corcho_promedio_redondeado = redondear(volumen_corcho_promedio, 3)

# ------///------ {CILINDRO PLATEADO} ------///------
radio_cilindro_plata = diametro_cilindro_plata_promedio / 2
altura_cilindro_plata = largo_cilindro_plata_promedio
volumen_cilindro_plata_promedio = np.pi * (radio_cilindro_plata ** 2) * altura_cilindro_plata
volumen_cilindro_plata_promedio_redondeado = redondear(volumen_cilindro_plata_promedio, 3)

# ------///------ {CILINDRO DORADO} ------///------
radio_cilindro_dorado = diametro_cilindro_dorado_promedio / 2
altura_cilindro_dorado = largo_cilindro_dorado_promedio
volumen_cilindro_dorado_promedio = np.pi * (radio_cilindro_dorado ** 2) * altura_cilindro_dorado
volumen_cilindro_dorado_promedio_redondeado = redondear(volumen_cilindro_dorado_promedio, 3)

# ------///------ {CILINDRO HUECO} ------///------
radio_externo_cilindro_hueco = diametro_externo_cilindro_hueco_promedio / 2
radio_interno_cilindro_hueco = diametro_interno_cilindro_hueco_promedio / 2
altura_cilindro_hueco = largo_cilindro_hueco_promedio
volumen_cilindro_hueco_promedio = np.pi * (radio_externo_cilindro_hueco ** 2 - radio_interno_cilindro_hueco ** 2) * altura_cilindro_hueco
volumen_cilindro_hueco_promedio_redondeado = redondear(volumen_cilindro_hueco_promedio, 3)

# ------///------ {MONEDA} ------///------
radio_moneda = diametro_moneda_promedio / 2
altura_moneda = espesor_moneda_promedio
volumen_moneda_promedio = np.pi * (radio_moneda ** 2) * altura_moneda
volumen_moneda_promedio_redondeado = redondear(volumen_moneda_promedio, 3)

#------------------------------------
# ERRORES DE VOLUMENES
#------------------------------------

# ------///------ {CORCHO} ------///------
delta_v_corcho =( np.pi / 4 ) * ( ( 2 * diametro_corcho_promedio * largo_corcho_promedio * db.incertidumbre_vernier ) + (diametro_corcho_promedio ** 2) * db.incertidumbre_vernier)
delta_v_corcho_redondeado = redondear(delta_v_corcho, 3)
delta_v_corcho_redondeado_relativo = redondear((delta_v_corcho_redondeado / volumen_corcho_promedio_redondeado) * 100, 2)

# ------///------ {CILINDRO PLATEADO} ------///------
delta_v_cilindro_plata =( np.pi / 4 ) * ( ( 2 * diametro_cilindro_plata_promedio * largo_cilindro_plata_promedio * db.incertidumbre_vernier ) + (diametro_cilindro_plata_promedio ** 2) * db.incertidumbre_vernier) 
delta_v_cilindro_plata_redondeado = redondear(delta_v_cilindro_plata, 3)
delta_v_cilindro_plata_redondeado_relativo = redondear((delta_v_cilindro_plata_redondeado / volumen_cilindro_plata_promedio_redondeado) * 100, 2)

# ------///------ {CILINDRO DORADO} ------///------
delta_v_cilindro_dorado =( np.pi / 4 ) * ( ( 2 * diametro_cilindro_dorado_promedio * largo_cilindro_dorado_promedio * db.incertidumbre_vernier ) + (diametro_cilindro_dorado_promedio ** 2) * db.incertidumbre_vernier) 
delta_v_cilindro_dorado_redondeado = redondear(delta_v_cilindro_dorado, 3)
delta_v_cilindro_dorado_redondeado_relativo = redondear((delta_v_cilindro_dorado_redondeado / volumen_cilindro_dorado_promedio_redondeado) * 100, 2)

# ------///------ {CILINDRO HUECO} ------///------
delta_v_cilindro_hueco =( np.pi / 4 ) * ( diametro_externo_cilindro_hueco_promedio ** 2 - diametro_interno_cilindro_hueco_promedio ** 2) * db.incertidumbre_vernier + ( np.pi / 2 ) * ( diametro_externo_cilindro_hueco_promedio * largo_cilindro_hueco_promedio * db.incertidumbre_vernier + diametro_interno_cilindro_hueco_promedio * largo_cilindro_hueco_promedio * db.incertidumbre_vernier)
delta_v_cilindro_hueco_redondeado = redondear(delta_v_cilindro_hueco, 3)
delta_v_cilindro_hueco_redondeado_relativo = redondear((delta_v_cilindro_hueco_redondeado / volumen_cilindro_hueco_promedio_redondeado) * 100, 2)

# ------///------ {MONEDA} ------///------
delta_v_moneda = (np.pi/4) * ((2 * diametro_moneda_promedio * espesor_moneda_promedio * db.incertidumbre_vernier)  + (diametro_moneda_promedio**2) * db.incertidumbre_micrometro_cm)
delta_v_moneda_redondeado = redondear(delta_v_moneda, 3)
delta_v_moneda_redondeado_relativo = redondear((delta_v_moneda_redondeado / volumen_moneda_promedio_redondeado) * 100, 2)

#------------------------------------
# DENSIDADES (g/cm³)
#------------------------------------

# ------///------ {CORCHO} ------///------
densidad_corcho_promedio = db.masa_corcho_promedio / volumen_corcho_promedio
densidad_corcho_promedio_redondeada = redondear(densidad_corcho_promedio, 2)

# ------///------ {CILINDRO PLATEADO} ------///------
densidad_cilindro_plata_promedio = db.masa_cilindro_plata_promedio / volumen_cilindro_plata_promedio
densidad_cilindro_plata_promedio_redondeada = redondear(densidad_cilindro_plata_promedio, 2)

# ------///------ {CILINDRO DORADO} ------///------
densidad_cilindro_dorado_promedio = db.masa_cilindro_dorado_promedio / volumen_cilindro_dorado_promedio
densidad_cilindro_dorado_promedio_redondeada = redondear(densidad_cilindro_dorado_promedio, 2)

# ------///------ {CILINDRO HUECO} ------///------
densidad_cilindro_hueco_promedio = db.masa_cilindro_hueco_promedio / volumen_cilindro_hueco_promedio
densidad_cilindro_hueco_promedio_redondeada = redondear(densidad_cilindro_hueco_promedio, 2)

# ------///------ {MONEDA} ------///------
densidad_moneda_promedio = db.masa_moneda_promedio / volumen_moneda_promedio
densidad_moneda_promedio_redondeada = redondear(densidad_moneda_promedio, 2)    

#------------------------------------
# ERRORES DE DENSIDAD
#------------------------------------

# ------///------ {CORCHO} ------///------
delta__d_corcho = (db.masa_corcho_promedio * delta_v_corcho + volumen_corcho_promedio * db.incertidumbre_balanza) / (volumen_corcho_promedio**2)
delta_d_corcho_redondeado = redondear(delta__d_corcho, 2)
delta_d_corcho_redondeado_relativo = redondear((delta_d_corcho_redondeado / densidad_corcho_promedio_redondeada) * 100, 2)

# ------///------ {CILINDRO PLATEADO} ------///------
delta__d_cilindro_plata = (db.masa_cilindro_plata_promedio * delta_v_cilindro_plata + volumen_cilindro_plata_promedio * db.incertidumbre_balanza) / (volumen_cilindro_plata_promedio**2)
delta_d_cilindro_plata_redondeado = redondear(delta__d_cilindro_plata, 2)
delta_d_cilindro_plata_redondeado_relativo = redondear((delta_d_cilindro_plata_redondeado / densidad_cilindro_plata_promedio_redondeada) * 100, 2)

# ------///------ {CILINDRO DORADO} ------///------
delta__d_cilindro_dorado = (db.masa_cilindro_dorado_promedio * delta_v_cilindro_dorado + volumen_cilindro_dorado_promedio * db.incertidumbre_balanza) / (volumen_cilindro_dorado_promedio**2)
delta_d_cilindro_dorado_redondeado = redondear(delta__d_cilindro_dorado, 2)
delta_d_cilindro_dorado_redondeado_relativo = redondear((delta_d_cilindro_dorado_redondeado / densidad_cilindro_dorado_promedio_redondeada) * 100, 2)

# ------///------ {CILINDRO HUECO} ------///------
delta__d_cilindro_hueco = (db.masa_cilindro_hueco_promedio * delta_v_cilindro_hueco + volumen_cilindro_hueco_promedio * db.incertidumbre_balanza) / (volumen_cilindro_hueco_promedio**2)
delta_d_cilindro_hueco_redondeado = redondear(delta__d_cilindro_hueco, 2)
delta_d_cilindro_hueco_redondeado_relativo = redondear((delta_d_cilindro_hueco_redondeado / densidad_cilindro_hueco_promedio_redondeada) * 100, 2)

# ------///------ {MONEDA} ------///------
delta__d_moneda = (db.masa_moneda_promedio * delta_v_moneda + volumen_moneda_promedio * db.incertidumbre_balanza) / (volumen_moneda_promedio**2)
delta_d_moneda_redondeado = redondear(delta__d_moneda, 2)
delta_d_moneda_redondeado_relativo = redondear((delta_d_moneda_redondeado / densidad_moneda_promedio_redondeada) * 100, 2)


#------------------------------------
# RESULTADOS TOTALES
#------------------------------------

datos_resultados = {
    'Objeto': ['Corcho', 'Cilindro Plateado', 'Cilindro Dorado', 'Cilindro Hueco', 'Moneda'],
    'Masa_promedio_gr': [db.masa_corcho_promedio_redondeada, db.masa_cilindro_plata_promedio_redondeada, db.masa_cilindro_dorado_promedio_redondeada, db.masa_cilindro_hueco_promedio_redondeada, db.masa_moneda_promedio_redondeada],
    'Error_masa_gr': [db.incertidumbre_balanza] * 5,
    'Volumen_promedio_cm3': [volumen_corcho_promedio_redondeado, volumen_cilindro_plata_promedio_redondeado, volumen_cilindro_dorado_promedio_redondeado, volumen_cilindro_hueco_promedio_redondeado, volumen_moneda_promedio_redondeado],
    'Error_volumen_cm3': [delta_v_corcho_redondeado, delta_v_cilindro_plata_redondeado, delta_v_cilindro_dorado_redondeado, delta_v_cilindro_hueco_redondeado, delta_v_moneda_redondeado], 
    'Error_volumen_%': [delta_v_corcho_redondeado_relativo, delta_v_cilindro_plata_redondeado_relativo, delta_v_cilindro_dorado_redondeado_relativo, delta_v_cilindro_hueco_redondeado_relativo, delta_v_moneda_redondeado_relativo],
    'Densidad_promedio_g/cm3': [densidad_corcho_promedio_redondeada, densidad_cilindro_plata_promedio_redondeada, densidad_cilindro_dorado_promedio_redondeada, densidad_cilindro_hueco_promedio_redondeada, densidad_moneda_promedio_redondeada],
    'Error_densidad_g/cm3': [delta_d_corcho_redondeado, delta_d_cilindro_plata_redondeado, delta_d_cilindro_dorado_redondeado, delta_d_cilindro_hueco_redondeado, delta_d_moneda_redondeado], 
    'Error_densidad_%': [delta_d_corcho_redondeado_relativo, delta_d_cilindro_plata_redondeado_relativo, delta_d_cilindro_dorado_redondeado_relativo, delta_d_cilindro_hueco_redondeado_relativo, delta_d_moneda_redondeado_relativo],
}
df_resultados = pd.DataFrame(datos_resultados)

#------------------------------------
# VOLUMENES
#------------------------------------
datos_resultados_volumenes = {
    'Objeto': ['Corcho', 'Cilindro Plateado', 'Cilindro Dorado', 'Cilindro Hueco', 'Moneda'],
    'Volumen_promedio_cm3': [volumen_corcho_promedio_redondeado, volumen_cilindro_plata_promedio_redondeado, volumen_cilindro_dorado_promedio_redondeado, volumen_cilindro_hueco_promedio_redondeado, volumen_moneda_promedio_redondeado],
    'Error_volumen_cm3': [delta_v_corcho_redondeado, delta_v_cilindro_plata_redondeado, delta_v_cilindro_dorado_redondeado, delta_v_cilindro_hueco_redondeado, delta_v_moneda_redondeado], 
    'Error_volumen_%': [delta_v_corcho_redondeado_relativo, delta_v_cilindro_plata_redondeado_relativo, delta_v_cilindro_dorado_redondeado_relativo, delta_v_cilindro_hueco_redondeado_relativo, delta_v_moneda_redondeado_relativo], 
}
df_resultados_volumenes = pd.DataFrame(datos_resultados_volumenes)

#------------------------------------
# DENSIDADES
#------------------------------------
datos_resultados_densidades = {
    'Objeto': ['Corcho', 'Cilindro Plateado', 'Cilindro Dorado', 'Cilindro Hueco', 'Moneda'],
    'Densidad_promedio_g/cm3': [densidad_corcho_promedio_redondeada, densidad_cilindro_plata_promedio_redondeada, densidad_cilindro_dorado_promedio_redondeada, densidad_cilindro_hueco_promedio_redondeada, densidad_moneda_promedio_redondeada],
    'Error_densidad_g/cm3': [delta_d_corcho_redondeado, delta_d_cilindro_plata_redondeado, delta_d_cilindro_dorado_redondeado, delta_d_cilindro_hueco_redondeado, delta_d_moneda_redondeado], 
    'Error_densidad_%': [delta_d_corcho_redondeado_relativo, delta_d_cilindro_plata_redondeado_relativo, delta_d_cilindro_dorado_redondeado_relativo, delta_d_cilindro_hueco_redondeado_relativo, delta_d_moneda_redondeado_relativo], 
}
df_resultados_densidades = pd.DataFrame(datos_resultados_densidades)


print(df_resultados)