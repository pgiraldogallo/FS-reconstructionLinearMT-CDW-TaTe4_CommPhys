import numpy as np
import matplotlib.pyplot as plt

# Load only the two highlighted Fermi-crossing bands.
data = np.loadtxt('fermi_crossing_bands_blue_green.txt')
k = data[:, 0]
blue = data[:, 1]
green = data[:, 2]

ticks = []
labels = []
with open('k_path_ticks.txt') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        label, idx, xpos = line.split()
        labels.append('Γ' if label == 'Gamma' else label)
        ticks.append(float(xpos))

plt.plot(k, blue, color='blue', label='blue band, j=68 / band 69')
plt.plot(k, green, color='green', label='green band, j=70 / band 71')
plt.axhline(0, linestyle='--', color='black', linewidth=0.8)
for x in ticks:
    plt.axvline(x, color='black', linewidth=0.8)
plt.xticks(ticks, labels)
plt.xlabel(r'$k$-points')
plt.ylabel(r'$E-E_F$ [eV]')
plt.ylim(-1, 1)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig('nonCDW_fermi_crossing_bands.png', dpi=300)
plt.show()
