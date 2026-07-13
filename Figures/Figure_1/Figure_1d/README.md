TYPO: THIS IS Figure 1e

CDW-phase DFT band structure data
This folder contains the raw data and plotting script used to reproduce the CDW-phase electronic band dispersion.
Files
`Pncc-bands-nosoc.dat`: raw DFT band-structure data for the CDW phase without spin-orbit coupling.
`plot_CDW_bandstructure.py`: Python script that reads the `.dat` file and reproduces the highlighted band-structure plot.
Energy reference
The energies in `Pncc-bands-nosoc.dat` are already given relative to the Fermi level. Therefore,
```text
E_F = 0 eV
```
and the plotted vertical axis is
```text
E - E_F [eV]
```
The horizontal dashed line in the plot corresponds to `E - E_F = 0 eV`.
Data organization
The file contains 960 bands and 140 k-points per band. Each numeric row contains two columns:
```text
k_distance    energy_minus_EF_eV
```
The data are organized sequentially by band. Python uses zero-based indices, so the band index `j` in the script corresponds to the one-based band number `j + 1`.
Highlighted bands
The highlighted bands in the plot are:
color	Python index `j`	one-based band number
orange	824	825
yellow	825	826
red	826	827
light blue	827	828
pink	828	829
purple	829	830
In the original plotting script, bands with Python indices `j = 830` and `j = 831` were skipped.
k-path
The k-path labels used in the plot are:
```text
γ - x - m - γ - z - r - a - z
```
The vertical lines and tick positions are determined from the 140 k-points using the same indexing logic as the original plotting script.
Reproducing the plot
From this folder, run:
```bash
python plot_CDW_bandstructure.py
```
This creates:
```text
Bandstructure_identified_CDW.png
```
The script requires Python with `numpy` and `matplotlib` installed.
