
import pandas as pd
import importlib.util
import sys

# 1. Configuración de formatos (Tu regla de oro)
formatos = {
    'Masa (g)': "{:.2f}",
    'Diámetro (cm)': "{:.3f}",
    'Altura (cm)': "{:.3f}",
    'Espesor (cm)': "{:.3f}",
    'Radio (cm)': "{:.3f}"
}

def exportar_todos_los_dfs(ruta_script, archivo_salida="tablas_reporte.tex"):
    # Cargar el script de forma dinámica
    spec = importlib.util.spec_from_file_location("modulo_datos", ruta_script)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)

    with open(archivo_salida, 'w') as f:
        # 2. El Ciclo: Recorremos todos los objetos del script
        for nombre, obj in vars(modulo).items():
            if isinstance(obj, pd.DataFrame):
                print(f"Procesando: {nombre}...")
                
                # 1. Generamos el látex más básico (sin argumentos extra de estilo)
                # Solo dejamos los formatters para cumplir tu regla de decimales
                cuerpo_tabla = obj.to_latex(
                    index=False,
                    formatters=formatos,
                    column_format='c' * len(obj.columns)
                )

                # 2. Reemplazo Manual: Convertimos hlines feos en booktabs elegantes
                # Reemplazamos la primera y última línea para que tengan estilo paper
                cuerpo_tabla = cuerpo_tabla.replace('\\hline\\hline', '\\toprule') # Por si acaso
                cuerpo_tabla = cuerpo_tabla.replace('\\hline', '\\midrule')
                
                # 3. Construcción del entorno de la tabla
                f.write(f"\n% --- Tabla: {nombre} ---\n")
                f.write("\\begin{table}[h!]\n")
                f.write("    \\centering\n")
                f.write(f"    \\caption{{Datos de: {nombre.replace('_', ' ')}}}\n")
                f.write(f"    \\label{{tab:{nombre}}}\n")
                
                # Limpiamos el inicio y fin que Pandas pone por defecto (\begin{tabular}...)
                # para asegurar que las líneas booktabs queden bien puestas
                lineas = cuerpo_tabla.split('\n')
                for i, linea in enumerate(lineas):
                    if i == 1: # Justo después de \begin{tabular}
                        f.write("    \\toprule\n")
                    
                    f.write("    " + linea + "\n")
                    
                    if i == len(lineas) - 3: # Justo antes de \end{tabular}
                        f.write("    \\bottomrule\n")

                f.write("\\end{table}\n")

    print(f"\n¡Listo! Todas las tablas están en {archivo_salida}")


exportar_todos_los_dfs("python_scripts/datos_brutos.py")