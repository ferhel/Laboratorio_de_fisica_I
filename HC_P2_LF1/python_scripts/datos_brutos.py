import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_EVEN
 
 
# -----------------------------------
# Función de redondeo metrológico
# -----------------------------------
 
def redondear(valor, decimales):
    """
    Redondeo científico correcto.
    Usa Decimal(str(x)) para evitar errores de representación binaria (float64),
    y ROUND_HALF_EVEN como estándar metrológico internacional (GUM/BIPM).
    """
    cuantizador = Decimal(10) ** -decimales
    return float(Decimal(str(valor)).quantize(cuantizador, rounding=ROUND_HALF_EVEN))
 
 
# -----------------------------------
# Apreciación de los instrumentos
# -----------------------------------
 
incertidumbre_balanza        = 0.01   # gramos
incertidumbre_vernier        = 0.005  # cm
incertidumbre_micrometro     = 0.01   # mm
incertidumbre_micrometro_cm  = 0.001  # cm
 
 
# -----------------------------------
# Datos en bruto
# -----------------------------------
 
# ------///------ {CORCHO} ------///------
 
# MASA (GRAMOS)
# La masa del corcho se midió por diferencia:
# se pesó la moneda sola, luego moneda + corcho.
# La diferencia da la masa del corcho.
 
masa_moneda        = np.array([9.51, 9.50, 9.50, 9.50])
masa_moneda_corcho = np.array([12.1, 12.77, 13.00, 13.00])
masa_corcho_       = masa_moneda_corcho - masa_moneda
masa_corcho_promedio = np.mean(masa_corcho_)
masa_corcho_promedio_redondeada = redondear(masa_corcho_promedio, 2)
 
# Incertidumbre: suma de las dos apreciaciones de la balanza (medición antes + después)
error_masa_corcho = 0.02
 
datos_bruto_corcho = {
    'Largo_cm':    [3.745, 3.745, 3.750, 3.750, 3.750, 3.800, 3.800, 3.800, 3.800, 3.750, 3.800, 3.740],
    'Diámetro_cm': [1.400, 1.435, 1.400, 1.435, 1.430, 1.435, 1.440, 1.430, 1.430, 1.435, 1.435, 1.435],
    'Masa_gr':     [masa_corcho_promedio_redondeada] * 12,
}
df_bruto_corcho = pd.DataFrame(datos_bruto_corcho)
 
 
# ------///------ {CILINDRO PLATEADO} ------///------
 
masa_cilindro_plata = np.array([17.75, 17.75, 17.85, 17.85, 18.00])
masa_cilindro_plata_promedio = np.mean(masa_cilindro_plata)
masa_cilindro_plata_promedio_redondeada = redondear(masa_cilindro_plata_promedio, 2)
 
diametro_cilindro_plata = np.array(1.100)
 
datos_bruto_cilindro_plata = {
    'Largo_cm':    [1.620, 1.620, 1.620, 1.620, 1.620, 1.620, 1.620, 1.620, 1.620, 1.620, 1.620, 1.615],
    'Diámetro_cm': [diametro_cilindro_plata] * 12,
    'Masa_gr':     [masa_cilindro_plata_promedio_redondeada] * 12,
}
df_bruto_cilindro_plata = pd.DataFrame(datos_bruto_cilindro_plata)
 
 
# ------///------ {CILINDRO DORADO} ------///------
 
masa_cilindro_dorado = np.array([43.85, 43.75, 43.80, 43.72, 43.80])
masa_cilindro_dorado_promedio = np.mean(masa_cilindro_dorado)
masa_cilindro_dorado_promedio_redondeada = redondear(masa_cilindro_dorado_promedio, 2)
 
diametro_cilindro_dorado = np.array(1.100)
 
datos_bruto_cilindro_dorado = {
    'Largo_cm':    [1.660, 1.660, 1.655, 1.660, 1.655, 1.660, 1.655, 1.660, 1.665, 1.665],
    'Diámetro_cm': [diametro_cilindro_dorado] * 10,
    'Masa_gr':     [masa_cilindro_dorado_promedio_redondeada] * 10,
}
df_bruto_cilindro_dorado = pd.DataFrame(datos_bruto_cilindro_dorado)
 
 
# ------///------ {CILINDRO HUECO} ------///------
 
masa_cilindro_hueco = np.array([3.40, 3.25, 3.25, 3.20, 3.20])
masa_cilindro_hueco_promedio = np.mean(masa_cilindro_hueco)
masa_cilindro_hueco_promedio_redondeada = redondear(masa_cilindro_hueco_promedio, 2)
 
diametro_externo_hueco = np.array(1.100)
 
datos_bruto_cilindro_hueco = {
    'Largo_cm':           [1.565, 1.570, 1.565, 1.570, 1.565, 1.565, 1.565, 1.565, 1.565, 1.565],
    'Diámetro_externo_cm':[diametro_externo_hueco] * 10,
    'Diámetro_interno_cm':[0.840, 0.885, 0.885, 0.885, 0.875, 0.870, 0.875, 0.875, 0.875, 0.875],
    'Masa_gr':            [masa_cilindro_hueco_promedio_redondeada] * 10,
}
df_bruto_cilindro_hueco = pd.DataFrame(datos_bruto_cilindro_hueco)
 
 
# ------///------ {MONEDA} ------///------
 
masa_moneda_promedio = np.mean(masa_moneda)
masa_moneda_promedio_redondeada = redondear(masa_moneda_promedio, 2)
 
datos_bruto_moneda = {
    'Espesor_cm':  [0.1370, 0.1350, 0.1380, 0.1350, 0.1350, 0.1350, 0.1330, 0.1380, 0.1350, 0.1370, 0.1330, 0.1370],
    'Diámetro_cm': [3.910, 3.910, 3.910, 3.910, 4.005, 4.005, 4.005, 3.910, 4.005, 3.910, 4.005, 4.005],
    'Masa_gr':     [masa_moneda_promedio_redondeada] * 12,
}
df_bruto_moneda = pd.DataFrame(datos_bruto_moneda)

