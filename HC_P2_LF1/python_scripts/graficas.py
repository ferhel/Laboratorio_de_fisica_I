import numpy as np
import matplotlib.pyplot as plt
import python_scripts.calculos as cal
import python_scripts.datos_brutos as db
 
# ─── DATOS DESDE CALCULOS ────────────────────────────────────
solidos = ['Corcho', 'Cil.\nPlateado', 'Cil.\nDorado', 'Cil.\nHueco', 'Moneda']
x = np.arange(len(solidos))
 
masas = np.array([db.masa_corcho_promedio,
                  db.masa_cilindro_plata_promedio,
                  db.masa_cilindro_dorado_promedio,
                  db.masa_cilindro_hueco_promedio,
                  db.masa_moneda_promedio])
 
volumenes = np.array([cal.volumen_corcho_promedio_redondeado,
                      cal.volumen_cilindro_plata_promedio_redondeado,
                      cal.volumen_cilindro_dorado_promedio_redondeado,
                      cal.volumen_cilindro_hueco_promedio_redondeado,
                      cal.volumen_moneda_promedio_redondeado])
 
dV = np.array([cal.delta_v_corcho_redondeado,
               cal.delta_v_cilindro_plata_redondeado,
               cal.delta_v_cilindro_dorado_redondeado,
               cal.delta_v_cilindro_hueco_redondeado,
               cal.delta_v_moneda_redondeado])
 
dV_pct = np.array([cal.delta_v_corcho_redondeado_relativo,
                   cal.delta_v_cilindro_plata_redondeado_relativo,
                   cal.delta_v_cilindro_dorado_redondeado_relativo,
                   cal.delta_v_cilindro_hueco_redondeado_relativo,
                   cal.delta_v_moneda_redondeado_relativo])
 
densidades = np.array([cal.densidad_corcho_promedio_redondeada,
                       cal.densidad_cilindro_plata_promedio_redondeada,
                       cal.densidad_cilindro_dorado_promedio_redondeada,
                       cal.densidad_cilindro_hueco_promedio_redondeada,
                       cal.densidad_moneda_promedio_redondeada])
 
drho = np.array([cal.delta_d_corcho_redondeado,
                 cal.delta_d_cilindro_plata_redondeado,
                 cal.delta_d_cilindro_dorado_redondeado,
                 cal.delta_d_cilindro_hueco_redondeado,
                 cal.delta_d_moneda_redondeado])
 
drho_pct = np.array([cal.delta_d_corcho_redondeado_relativo,
                     cal.delta_d_cilindro_plata_redondeado_relativo,
                     cal.delta_d_cilindro_dorado_redondeado_relativo,
                     cal.delta_d_cilindro_hueco_redondeado_relativo,
                     cal.delta_d_moneda_redondeado_relativo])
 
# ─── ESTILO ──────────────────────────────────────────────────
plt.rcParams.update({
    'font.family':       'DejaVu Sans',
    'font.size':         11,
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'axes.grid':         True,
    'grid.alpha':        0.3,
    'grid.linestyle':    '--',
})
 
COLORS  = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2']
MARKERS = ['o', 's', '^', 'D', 'P']
MS = 90
 
fig, axes = plt.subplots(2, 2, figsize=(13, 10))
fig.suptitle('Densidad de Sólidos — Resultados Experimentales',
             fontsize=14, fontweight='bold', y=1.01)
 
# ── Gráfica 1: Volumen con barras de error ────────────────────
ax1 = axes[0, 0]
for i in range(len(solidos)):
    ax1.scatter(x[i], volumenes[i], s=MS, color=COLORS[i], marker=MARKERS[i], zorder=3)
    ax1.errorbar(x[i], volumenes[i], yerr=dV[i],
                 fmt='none', color=COLORS[i], capsize=5, capthick=1.5, linewidth=1.5)
ax1.set_xticks(x)
ax1.set_xticklabels(solidos, fontsize=10)
ax1.set_ylabel('Volumen (cm³)')
ax1.set_title('Volumen por sólido (± δV)')
 
# ── Gráfica 2: Densidad con barras de error ───────────────────
ax2 = axes[0, 1]
for i in range(len(solidos)):
    ax2.scatter(x[i], densidades[i], s=MS, color=COLORS[i], marker=MARKERS[i], zorder=3)
    ax2.errorbar(x[i], densidades[i], yerr=drho[i],
                 fmt='none', color=COLORS[i], capsize=5, capthick=1.5, linewidth=1.5)
ax2.set_xticks(x)
ax2.set_xticklabels(solidos, fontsize=10)
ax2.set_ylabel('Densidad (g/cm³)')
ax2.set_title('Densidad por sólido (± δρ)')
 
referencias = {'Corcho (~0.2)': 0.2, 'Agua (1.0)': 1.0,
               'Al (2.7)': 2.7,      'Fe (7.9)': 7.9,
               'Cu (8.9)': 8.9,      'Pb (11.3)': 11.3,
               'Au (19.3)': 19.3}
for label, val in referencias.items():
    if val <= max(densidades) + 2:
        ax2.axhline(val, linestyle=':', linewidth=0.9, color='gray', alpha=0.6)
        ax2.text(4.55, val, label, fontsize=7.5, va='center', color='gray')
 
# ── Gráfica 3: Error relativo de volumen ─────────────────────
ax3 = axes[1, 0]
for i in range(len(solidos)):
    ax3.scatter(x[i], dV_pct[i], s=MS, color=COLORS[i], marker=MARKERS[i], zorder=3)
ax3.set_xticks(x)
ax3.set_xticklabels(solidos, fontsize=10)
ax3.set_ylabel('δV / V × 100 (%)')
ax3.set_title('Error relativo de volumen')
ax3.axhline(2.0, linestyle='--', linewidth=1, color='tomato', alpha=0.7)
ax3.text(4.55, 2.05, '2%', fontsize=8, color='tomato')
 
# ── Gráfica 4: Masa vs Densidad ──────────────────────────────
ax4 = axes[1, 1]
for i in range(len(solidos)):
    ax4.scatter(masas[i], densidades[i], s=MS, color=COLORS[i],
                marker=MARKERS[i], zorder=3,
                label=solidos[i].replace('\n', ' '))
    ax4.errorbar(masas[i], densidades[i], yerr=drho[i],
                 fmt='none', color=COLORS[i], capsize=5, capthick=1.5, linewidth=1.5)
ax4.set_xlabel('Masa (g)')
ax4.set_ylabel('Densidad (g/cm³)')
ax4.set_title('Masa vs Densidad (± δρ)')
ax4.legend(fontsize=8.5, loc='upper left', framealpha=0.7)
 
plt.tight_layout()
plt.savefig('graficas_laboratorio.png', dpi=150, bbox_inches='tight')
print("Guardado: graficas_laboratorio.png")
 