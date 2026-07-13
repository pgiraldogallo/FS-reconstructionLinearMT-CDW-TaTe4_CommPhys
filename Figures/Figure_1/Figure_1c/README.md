Non-CDW DFT band dispersion data
This folder contains simplified text files for the non-CDW electronic band dispersion.
Energy reference
The energies are already plotted as `E - E_F` in eV. Therefore, the Fermi level in these files is at:
```text
E - E_F = 0 eV
```
The absolute DFT Fermi energy is not contained in the plotting script or in this shifted band file. If needed, report the absolute Fermi energy separately from the DFT output.
Band indexing
The original plotting script uses zero-based Python indexing and highlights only two bands as crossing the Fermi level:
```python
j == 68  # blue band
j == 70  # green band
```
These correspond to one-based band labels:
```text
blue band  = band 69
green band = band 71
```
Files
`band_01.txt` ... `band_96.txt`: one file per band. Columns are `k_distance` and `energy_minus_EF_eV`.
`band_blue_j68_band69.txt`: highlighted blue Fermi-crossing band from the plotting script.
`band_green_j70_band71.txt`: highlighted green Fermi-crossing band from the plotting script.
`fermi_crossing_bands_blue_green.txt`: combined file containing only the two highlighted Fermi-crossing bands.
`all_bands_wide.txt`: one wide table with `k_distance` followed by all 96 bands.
`k_path_ticks.txt`: high-symmetry k-point positions used for plotting.
`plot_from_exported_data.py`: minimal plotting script using the simplified exported files.
k-path
The k-path labels used in the original figure are:
```text
Γ - X - M - Γ - Z - R - A - Z
```
See `k_path_ticks.txt` for the corresponding `k_distance` values.
