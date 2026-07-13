CDW-phase DFT band dispersion data

This folder contains band dispersion data to generate the referred figure.
Energy reference
The energies are given as `E - E_F` in eV. Therefore, the Fermi level is at:
```text
E_F = 0 eV
```

Files
`band_001_j000.txt` ... `band_960_j959.txt`: one file per band.
`all_bands_wide.txt`: one wide table with `k_distance` followed by the energy of all 960 bands.
`highlighted_CDW_bands.txt`: only the bands highlighted in the original paper plotting script.
`k_path_ticks.txt`: high-symmetry k-point tick positions used in the plot.
`plot_highlighted_CDW_bands.py`: minimal example to reproduce the highlighted-band plot from the exported files.
Highlighted bands in the original script
The original script highlighted the following bands:
Color in plot	Zero-based script index `j`	One-based band number
orange	824	825
yellow	825	826
red	826	827
lightblue	827	828
pink	828	829
purple	829	830
The script also contained `continue` statements for `j = 830` and `j = 831`, so those two bands were skipped in the plotted figure.
k-path labels
The original plot used the following labels:
```text
gamma - x - m - gamma - z - r - a - z
```
The exact tick positions are listed in `k_path_ticks.txt`.
Notes on plotting logic
The original script used separate `if` statements instead of a full `if/elif/else` chain, meaning several highlighted bands may also be drawn again as thin black lines depending on the final `else` association. The exported files here preserve the numerical data only and remove that plotting-specific logic.
