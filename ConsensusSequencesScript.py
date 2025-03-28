from collections import defaultdict, Counter
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Load your MSA file (FASTA format)
msa_file = "MSA_Round_3_species_headers_human_merged.fasta"  # Replace with your filename if different

# Parse sequences and group by species (assumed to be in the header)
species_groups = defaultdict(list)

for record in SeqIO.parse(msa_file, "fasta"):
    species = record.id.strip()
    species_groups[species].append(record.seq)

# Function to generate consensus sequence from a list of aligned sequences
def generate_consensus(sequences):
    consensus = ""
    columns = list(zip(*sequences))
    for col in columns:
        counter = Counter(col)
        consensus += counter.most_common(1)[0][0]
    return consensus

# Generate consensus sequences per species
consensus_records = []

for species, seqs in species_groups.items():
    consensus_seq = generate_consensus(seqs)
    record = SeqRecord(Seq(consensus_seq), id=species, description="Consensus")
    consensus_records.append(record)

# Save to a new FASTA file
output_file = "Species_Consensus_Sequences.fasta"
SeqIO.write(consensus_records, output_file, "fasta")
print(f"Consensus sequences written to: {output_file}")
