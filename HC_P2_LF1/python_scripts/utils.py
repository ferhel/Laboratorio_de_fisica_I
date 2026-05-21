# utils.py
from decimal import Decimal, ROUND_HALF_EVEN

def redondear(valor, decimales):
    cuantizador = Decimal(10) ** -decimales
    return float(Decimal(str(valor)).quantize(cuantizador, rounding=ROUND_HALF_EVEN))