# Analyticke reseni Volterrovy rovnice (prevzata z DP)

# f(x) = f0*e^(-cx) + lam * int_{0}^{x} e^(-c*(x-y)) * f(y) dy
# kde c > 0, lam > 0
# plot the graph

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

# definice vsech symbolu
# real, positive -> realna cisla
f0, c, lam, x, y = sm.symbols('f0 c \lambda x y', real = True, positive = True)
s = sm.symbols('s', real = True, positive = True)

# Jadro integralni rovnice
# L{e^(-cx)} = 1/(s+c)
L_kernel = 1/(s+c)

# rovnice po transormaci
F = sm.symbols('F')
rovnice = sm.Eq(F, f0 * L_kernel + lam * L_kernel * F)

print ("Řešení Volterrovy integralni rovnice")
print (f"Transformovaná rovnice v tzv. s-doméně je:\n {rovnice}")

# vyjadreni F(s)
F_vysledek = sm.solve(rovnice, F)[0]
F_prehledneji = sm.simplify(F_vysledek)

# navrat k feseni f(x) - zpetna Laplaceova transformace
f_reseni = sm.inverse_laplace_transform(F_prehledneji, s, x)

print (f"Řešení této rovnice je f(x) = {sm.simplify(f_reseni)}")

# =================================================================
# Numerika a konfigurace

f0_num = 5 # pocatecni napeti materialu
x0 = 0 # start v case t = 0
x_max = 5 # cilovy stav, v case t = x_max
body = 1000 # hustota mrizky

# parametry (moznych scenaru)
c_num = 2 # tlumeni (vzdy kladne)
lam_stab = 1.9 # lambda < c - stabilni utlum
lam_nestab = 2.1 # vysoky zisk, lambda > c - exponenciala

# podklad pro graf
ox = np.linspace(x0, x_max, body)

reseni_vykonne = sm.lambdify((x, c, f0, lam), sm.simplify(f_reseni), 'numpy')

y_stab = reseni_vykonne(ox, c_num, f0_num, lam_stab)
y_nestab = reseni_vykonne(ox, c_num, f0_num, lam_nestab)

# ===========================================================
# 3) grafy
# a) oba v jednom

plt.figure(figsize=(10, 6))

plt.plot(ox, y_stab, color='darkgreen', linewidth=2.5, 
         label=fr'Stabilní režim ($\lambda$={lam_stab} < $c$={c_num}) - Útlum')
plt.plot(ox, y_nestab, color='crimson', linewidth=2.5, linestyle='--',
         label=fr'Nestabilní režim ($\lambda$={lam_nestab} > $c$={c_num}) - Nárůst')
plt.scatter([0], [f0_num], color='black', s=120, zorder=5, label=fr'$f(0) = f_0 = {f0_num}$')

plt.xlabel('Čas / Vzdálenost $x$ [s]', fontsize=11)
plt.ylabel('Napětí v materiálu $f(x)$ [N]', fontsize=11)

plt.suptitle('Globální analýza odezvy Volterrovy rovnice', fontsize=14, weight='bold', y=0.98)
plt.title(fr'Bifurkace chování systému z počátečního bodu $f_0 = {f0_num}$', fontsize=11, pad=10)

plt.grid(True, linestyle=':', alpha=0.5)
plt.axhline(0, color='gray', linewidth=1.0, linestyle='-', alpha=0.3)
plt.legend(loc='best', shadow=True, framealpha=0.9)
plt.tight_layout()

# b) oba separovane vedle sebe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# b1 - stabilni
ax1.plot(ox, y_stab, color='darkgreen', linewidth=2.5, 
         label=fr'Stabilní režim ($\lambda$={lam_stab})')
ax1.scatter([0], [f0_num], color='black', s=100, zorder=5, label=fr'$f(0) = {f0_num}$')
ax1.set_xlabel('Čas [s]', fontsize=11)
ax1.set_ylabel('Napětí v materiálu $f(x)$ [N]', fontsize=11)
ax1.set_title(fr'Detail stabilního řešení (Relaxace): $f(x) = {f0_num} \cdot e^{{{x_max}({lam_stab} - {c_num})}}$', 
             fontsize=12, weight='bold', pad=15)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.axhline(0, color='gray', linewidth=1.0, linestyle='-', alpha=0.3)
ax1.legend(loc='upper right', shadow=True)

# b2 - nestabilni
ax2.plot(ox, y_nestab, color='crimson', linewidth=2.5, linestyle='--',
         label=fr'Nestabilní režim ($\lambda$={lam_nestab})')
ax2.scatter([0], [f0_num], color='black', s=100, zorder=5, label=fr'$f(0) = {f0_num}$')
ax2.set_xlabel('Čas [s]', fontsize=11)
ax2.set_ylabel('Napětí v materiálu $f(x)$ [N]', fontsize=11)
ax2.set_title(fr'Detail nestabilního řešení (Aktivní nárůst): $f(x) = {f0_num} \cdot e^{{{x_max}({lam_nestab} - {c_num})}}$', 
             fontsize=12, weight='bold', pad=15)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.axhline(0, color='gray', linewidth=1.0, linestyle='-', alpha=0.3)

ax2.set_ylim(-0.5, f0_num * 4) 
ax2.legend(loc='upper right', shadow=True)

plt.suptitle('Detailní analýza stavových režimů (Separovaná měřítka)', fontsize=14, weight='bold', y=0.98)
plt.tight_layout()

plt.show()