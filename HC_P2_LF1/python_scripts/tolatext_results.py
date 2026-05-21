import pandas as pd
import importlib.util
import os

def generar_tablas_separadas(nombre_script="calculos.py", archivo_salida="tablas_finales.tex"):
    # 1. Cargar el script de cálculos
    dir_script = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(dir_script, nombre_script)
    if not os.path.exists(ruta): ruta = os.path.join(os.getcwd(), nombre_script)

    spec = importlib.util.spec_from_file_location("modulo_calculos", ruta)
    calc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(calc)

    # 2. Helpers de formato
    def f_pm(v, e, d): return f"${v:.{d}f} \\pm {e:.{d}f}$"

    df = calc.df_resultados.copy()

    # --- TABLA 1: MASA Y VOLUMEN ---
    tab1 = pd.DataFrame()
    tab1['Objeto'] = df['Objeto']
    tab1['Masa ($g$)'] = [f_pm(v, e, 2) for v, e in zip(df['Masa_promedio_gr'], df['Error_masa_gr'])]
    tab1['Volumen ($cm^3$)'] = [f_pm(v, e, 3) for v, e in zip(df['Volumen_promedio_cm3'], df['Error_volumen_cm3'])]
    tab1['$E_V$ (\%)'] = [f"{x:.2f}\%" for x in df['Error_volumen_%']]

    # --- TABLA 2: DENSIDAD ---
    tab2 = pd.DataFrame()
    tab2['Objeto'] = df['Objeto']
    tab2['Densidad ($g/cm^3$)'] = [f_pm(v, e, 2) for v, e in zip(df['Densidad_promedio_g/cm3'], df['Error_densidad_g/cm3'])]
    tab2['$E_{\\rho}$ (\%)'] = [f"{x:.2f}\%" for x in df['Error_densidad_%']]

    # 3. Función de escritura manual (Anti-errores de versión)
    def escribir_bloque(f, dataframe, caption, label):
        f.write(f"\n% --- {caption} ---\n")
        f.write("\\begin{table}[h!]\n\\centering\n")
        f.write(f"\\caption{{{caption}}}\n\\label{{{label}}}\n")
        
        raw_latex = dataframe.to_latex(index=False, escape=False)
        lineas = raw_latex.strip().split('\n')
        
        for i, linea in enumerate(lineas):
            if i == 0: f.write("    " + linea + "\n    \\toprule\n")
            elif i == 1: f.write("    " + linea + "\n    \\midrule\n")
            elif i == len(lineas) - 1: f.write("    \\bottomrule\n    " + linea + "\n")
            else: f.write("    " + linea.replace('\\hline', '') + "\n")
        f.write("\\end{table}\n")

    # 4. Generar el archivo final
    with open(archivo_salida, 'w') as f:
        escribir_bloque(f, tab1, "Resultados de Masa y Volumen Propagado", "tab:masa_vol")
        f.write("\n\\vspace{0.5cm} % Espacio entre tablas\n")
        escribir_bloque(f, tab2, "Resultados de Densidad y Error Relativo", "tab:densidad")

    print(f"¡Hecho! Revisa {archivo_salida}")

if __name__ == "__main__":
    generar_tablas_separadas()