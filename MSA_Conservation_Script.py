import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

# ---------- Step 1: Load and Parse MSA FASTA ----------
def parse_fasta(filepath):
    sequences = defaultdict(str)
    current_header = None
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_header = line
F            else:
                sequences[current_header] += line
    return sequences

# Load your MSA file (Update filename if needed)
msa_file = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\MSA Results\MSA - Third Round\MSA_Round_3.fasta"
# Update this with your actual filename
msa_sequences = parse_fasta(msa_file)
sequences = list(msa_sequences.values())

# Alignment size
num_sequences = len(sequences)
alignment_length = len(sequences[0]) if sequences else 0

print(f"Loaded {num_sequences} sequences with alignment length {alignment_length}")

# Convert sequences to numpy array for analysis
alignment_array = np.array([list(seq) for seq in sequences])

# ---------- Step 2: Compute Conservation Scores ----------
def analyze_alignment(alignment_array):
    conservation = []
    
    for col in alignment_array.T:  # Iterate over columns (positions)
        counter = Counter(col)
        total = sum(counter.values())

        # Most common residue frequency (conservation score)
        most_common_freq = counter.most_common(1)[0][1] / total if total > 0 else 0
        conservation.append(most_common_freq)

    return conservation

conservation = analyze_alignment(alignment_array)

# ---------- Step 3: Plot Full Conservation ----------
plt.figure(figsize=(12, 5))
plt.plot(conservation, label="Conservation", linewidth=1.5)
plt.axhline(y=0.5, color='r', linestyle='--', label="50% Conservation (Variable Threshold)")
plt.axhline(y=1.0, color='g', linestyle='--', label="Fully Conserved")

plt.xlabel("Alignment Position")
plt.ylabel("Conservation Score")
plt.title("Sequence Conservation Across MSA")
plt.legend()
plt.grid()

# Save full plot
plt.savefig("MSA_Conservation_Plot.png", dpi=300)
plt.show()

print("Full conservation plot saved as 'MSA_Conservation_Plot.png'.")

# ---------- Step 4: Zoomed-In Plots at Positions 2500, 19000, 25000 ----------
regions = [(2300, 2500), (18000, 20000), (24800, 25200), (26000, 28000)]

for start, end in regions:
    plt.figure(figsize=(10, 4))
    plt.plot(range(start, end), conservation[start:end], label="Conservation", linewidth=1.5)
    plt.axhline(y=0.5, color='r', linestyle='--', label="50% Conservation (Variable Threshold)")
    plt.axhline(y=1.0, color='g', linestyle='--', label="Fully Conserved")

    plt.xlabel("Alignment Position")
    plt.ylabel("Conservation Score")
    plt.title(f"Zoomed-In Conservation: Positions {start} - {end}")
    plt.legend()
    plt.grid()

    # Save each zoomed-in plot
    zoomed_plot_name = f"MSA_Conservation_Zoom_{start}-{end}.png"
    plt.savefig(zoomed_plot_name, dpi=300)
    plt.show()

    print(f"Zoomed-in plot saved as '{zoomed_plot_name}'.")

print("All plots generated and saved.")
