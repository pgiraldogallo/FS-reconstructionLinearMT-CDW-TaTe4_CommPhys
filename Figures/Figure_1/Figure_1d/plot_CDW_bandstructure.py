#!/usr/bin/env python3
"""
Plot the CDW-phase electronic band dispersion from the raw DFT band data.

Input file expected in the same directory:
    Pncc-bands-nosoc.dat

The energies in the input file are already referenced to the Fermi level,
so the Fermi level is EF = 0 eV and the plotted quantity is E - EF.

The raw file is organized as 960 bands, with 140 k-points per band.
Between consecutive bands there is one separator/blank line in the original
VASP-style band-path output. This script ignores blank/separator lines and
reshapes the data into an array with shape (960, 140).
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({"font.size": 30})

DATA_FILE = Path("Pncc-bands-nosoc.dat")
OUTPUT_FILE = Path("Bandstructure_identified_CDW.png")

N_KPOINTS = 140
N_BANDS = 960
FERMI_LEVEL_EV = 0.0

# Python uses zero-based band indices j. The corresponding one-based band
# numbers are j + 1.
HIGHLIGHTED_BANDS = {
    824: {"color": "orange", "linewidth": 1.5, "label": "j=824, band 825"},
    825: {"color": "yellow", "linewidth": 1.5, "label": "j=825, band 826"},
    826: {"color": "red", "linewidth": 4.5, "label": "j=826, band 827"},
    827: {"color": "lightblue", "linewidth": 2.25, "label": "j=827, band 828"},
    828: {"color": "pink", "linewidth": 4.5, "label": "j=828, band 829"},
    829: {"color": "purple", "linewidth": 2.25, "label": "j=829, band 830"},
}

# These two bands were skipped in the original plotting script.
SKIPPED_BANDS = {830, 831}

K_LABELS = ["γ", "x", "m", "γ", "z", "r", "a", "z"]


def load_band_data(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Return k_distances and band energies with shape (N_BANDS, N_KPOINTS)."""
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                rows.append((float(parts[0]), float(parts[1])))
            except ValueError:
                continue

    expected = N_BANDS * N_KPOINTS
    if len(rows) != expected:
        raise ValueError(
            f"Expected {expected} numeric rows ({N_BANDS} bands x {N_KPOINTS} k-points), "
            f"but found {len(rows)} in {path}."
        )

    data = np.array(rows, dtype=float).reshape(N_BANDS, N_KPOINTS, 2)
    k_distances = data[0, :, 0]
    energies = data[:, :, 1]
    return k_distances, energies


def main() -> None:
    k_distances, energies = load_band_data(DATA_FILE)

    tick_indices = [
        0,
        N_KPOINTS // 7 - 1,
        2 * N_KPOINTS // 7 - 1,
        3 * N_KPOINTS // 7 - 1,
        4 * N_KPOINTS // 7 - 1,
        5 * N_KPOINTS // 7 - 1,
        6 * N_KPOINTS // 7 - 1,
        N_KPOINTS - 1,
    ]
    tick_positions = [k_distances[i] for i in tick_indices]

    fig, ax = plt.subplots(figsize=(8, 7))

    for j in range(N_BANDS):
        if j in SKIPPED_BANDS:
            continue
        if j in HIGHLIGHTED_BANDS:
            style = HIGHLIGHTED_BANDS[j]
            ax.plot(
                k_distances,
                energies[j],
                color=style["color"],
                linewidth=style["linewidth"],
                label=style["label"],
            )
        else:
            ax.plot(k_distances, energies[j], color="black", linewidth=0.3)

    ax.axhline(y=FERMI_LEVEL_EV, linestyle="--", color="black", linewidth=1.0)
    for xpos in tick_positions:
        ax.axvline(x=xpos, linestyle="-", color="black", linewidth=1.0)

    ax.set_xticks(tick_positions)
    ax.set_xticklabels(K_LABELS)
    ax.set_xlabel(r"$k$-points")
    ax.set_ylabel(r"$E-E_f$ [eV]")
    ax.set_ylim(-1, 1)
    ax.set_xlim(k_distances[0], k_distances[-1])

    fig.savefig(OUTPUT_FILE, dpi=800, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
