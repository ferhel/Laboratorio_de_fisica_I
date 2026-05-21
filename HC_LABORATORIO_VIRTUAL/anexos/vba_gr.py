"""
equivalente exacto de las macros VBA
Macros replicadas:
  - Posicionconstante → X_f y ΔX_f en MRU
  - aceleracion       → X_f y ΔX_f en MRUA
  - Vccte_Datos       → tabla posición vs tiempo en MRU
  - Vccte_Grafica     → gráfico X-t con línea de tendencia

  (olevba)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Tramo I — MRUA
X0_mrua   = 0       # posición inicial (m)
V0_mrua   = 0       # velocidad inicial (m/s)
t_mrua    = 6       # tiempo (s)
a         = 4       # aceleración (m/s²)

# Tramo II — MRU
# V0 se hereda del final del Tramo I
t_mru     = 50      # tiempo (s)

# Tramo III — MRUR
x_mrur    = 48      # distancia (m)
Vf_mrur   = 0       # velocidad final (el autobús para)

# Incertidumbres
Delta_t   = 0.01    # s
Delta_a   = 0.02    # m/s²
Delta_x   = 0.01    # m  (apreciación 1 cm)

print("=" * 50)
print("MACRO: aceleracion  →  Tramo I (MRUA)")
print("=" * 50)

Xf_mrua = X0_mrua + V0_mrua * t_mrua + 0.5 * a * t_mrua**2

# Propagación de incertidumbre:
# ΔX = ΔV₀·t + (V₀ + a·t)·Δt + 0.5·t²·Δa
Delta_V0_mrua = 0  # V0 es exacto (parte del reposo)
Delta_Xf_mrua = (Delta_V0_mrua * t_mrua
                 + (V0_mrua + a * t_mrua) * Delta_t
                 + 0.5 * t_mrua**2 * Delta_a)

V1 = V0_mrua + a * t_mrua          # velocidad al final del Tramo I
Delta_V1 = Delta_a * t_mrua + a * Delta_t  # ΔV₁

print(f"  Xf  = {Xf_mrua} m")
print(f"  ΔXf = {Delta_Xf_mrua:.4f} m")
print(f"  → X_I = ({Xf_mrua} ± {Delta_Xf_mrua:.2f}) m")
print(f"  V₁  = {V1} m/s  |  ΔV₁ = {Delta_V1:.4f} m/s")


# MACRO 1: Posicionconstante — Tramo II (MRU)

print()
print("=" * 50)
print("MACRO: Posicionconstante  →  Tramo II (MRU)")
print("=" * 50)

X0_mru = Xf_mrua    # empieza donde terminó el Tramo I
Xf_mru = X0_mru + V1 * t_mru

# ΔX = V·Δt + t·ΔV  (fórmula exacta de la macro G30)
Delta_Xf_mru = V1 * Delta_t + t_mru * Delta_V1

print(f"  Xf  = {Xf_mru} m")
print(f"  ΔXf = {Delta_Xf_mru:.4f} m")
print(f"  → X_II = ({Xf_mru} ± {Delta_Xf_mru:.2f}) m")


# Tramo III — MRUR  (velocidad promedio)

print()
print("=" * 50)
print("Tramo III (MRUR)  —  velocidad promedio")
print("=" * 50)

V_prom = (V1 + Vf_mrur) / 2
T3 = x_mrur / V_prom

# Δ(V_prom) = ΔV₁ / 2  (Vf = 0 exacto)
Delta_Vprom = Delta_V1 / 2
# ΔT₃ = Δx/V_prom + x·ΔV_prom/V_prom²
Delta_T3 = Delta_x / V_prom + x_mrur * Delta_Vprom / V_prom**2

print(f"  V_prom = {V_prom} m/s")
print(f"  T₃     = {T3} s")
print(f"  ΔT₃    = {Delta_T3:.4f} s")
print(f"  → T_III = ({T3} ± {Delta_T3:.2f}) s")


# Totales

print()
print("=" * 50)
print("TOTALES")
print("=" * 50)

X_total = Xf_mrua + (Xf_mru - Xf_mrua) + x_mrur
Delta_X_total = Delta_Xf_mrua + Delta_Xf_mru + Delta_x

t_total = t_mrua + t_mru + T3
Delta_t_total = Delta_t + Delta_t + Delta_T3   # Δt de cada tramo

print(f"  Distancia total = ({X_total} ± {Delta_X_total:.2f}) m")
print(f"  Tiempo total    = ({t_total} ± {Delta_t_total:.2f}) s")


# GRÁFICAS: Posición vs Tiempo


# — Datos por tramo —
a_mrur   = (Vf_mrur**2 - V1**2) / (2 * x_mrur)   # desaceleración (negativa)

t_sc_I   = np.linspace(0, t_mrua, 7)
x_sc_I   = X0_mrua + V0_mrua * t_sc_I + 0.5 * a * t_sc_I**2

t_sc_II  = np.linspace(t_mrua, t_mrua + t_mru, 11)
x_sc_II  = Xf_mrua + V1 * (t_sc_II - t_mrua)

t_sc_III = np.linspace(t_mrua + t_mru, t_total, 7)
dt_sc    = t_sc_III - (t_mrua + t_mru)
x_sc_III = Xf_mru + V1 * dt_sc + 0.5 * a_mrur * dt_sc**2

tramos = [
    (t_sc_I,   x_sc_I,   "royalblue", "Tramo I — MRUA",  2),
    (t_sc_II,  x_sc_II,  "seagreen",  "Tramo II — MRU",  1),
    (t_sc_III, x_sc_III, "tomato",    "Tramo III — MRUR", 2),
]

# ── Figura 1: scatter ────────
fig1, ax_all = plt.subplots(figsize=(8, 5))
for ts, xs, color, title, _ in tramos:
    ax_all.scatter(ts, xs, color=color, zorder=5, label=title)
ax_all.set_xlabel("Tiempo (s)")
ax_all.set_ylabel("Posición (m)")
ax_all.set_title("Posición vs Tiempo — Tres tramos")
ax_all.legend(fontsize=8)
ax_all.grid(True, alpha=0.3)

plt.suptitle("Figura 2.1 — Scatter", fontweight="bold")
plt.tight_layout()
plt.savefig("grafica_scatter.png", dpi=150)

# ── Figura 2: equivalente VBA — scatter + tendencia + R² ─
fig2, axes2 = plt.subplots(1, 3, figsize=(13, 4))

for ax, (ts, xs, color, title, deg) in zip(axes2, tramos):
    # scatter
    ax.scatter(ts, xs, color=color, zorder=5)

    # ajuste polinomial (= Trendlines.Add de Excel)
    coeffs = np.polyfit(ts, xs, deg)
    p      = np.poly1d(coeffs)
    t_fit  = np.linspace(ts[0], ts[-1], 200)

    ss_res = np.sum((xs - p(ts))**2)
    ss_tot = np.sum((xs - np.mean(xs))**2)
    r2     = 1 - ss_res / ss_tot if ss_tot != 0 else 1.0

    if deg == 1:
        label = f"X = {coeffs[0]:.2f}t + {coeffs[1]:.2f}\nR² = {r2:.4f}"
    else:
        label = f"X = {coeffs[0]:.3f}t² + {coeffs[1]:.2f}t + {coeffs[2]:.2f}\nR² = {r2:.4f}"

    ax.plot(t_fit, p(t_fit), color="black", lw=1.2, linestyle="--", label=label)
    ax.set_title(title)
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Posición (m)")
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)

plt.suptitle("Figura 2.2 — Equivalente macro VBA (tendencia + R²)", fontweight="bold")
plt.tight_layout()
plt.savefig("grafica_vba_equiv.png", dpi=150)

plt.show()
print("\nGuardadas:")
print("  grafica_scatter.png")
print("  grafica_vba_equiv.png     ← equivalente macro VBA")