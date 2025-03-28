import os
import re
from collections import Counter

# Paths
input_fasta = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\All_Genomes_Species.fna"
output_file = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\accession_species_mapping_ANIMAL.txt"

# Regex pattern to extract species from the first parentheses
accession_pattern = re.compile(r">(\S+)")  # Extract accession number
species_pattern = re.compile(r">[^/]+/([^/]+)")  # Extract the first word after the first /


def build_accession_species_mapping(input_fasta):
    """
    Creates a mapping of accession numbers to species names from the input FASTA file.
    """
    accession_to_species = {}

    with open(input_fasta, 'r') as file:
        for line in file:
            if line.startswith(">"):  # Only process headers
                full_header = line.strip()
                
                # Extract accession number (first word after ">")
                accession_match = accession_pattern.match(full_header)
                accession = accession_match.group(1) if accession_match else None
                
                # Extract species info from the first parentheses
                species_match = species_pattern.search(full_header)
                species_info = species_match.group(1) if species_match else "UNKNOWN"

                if accession:
                    accession_to_species[accession] = species_info  # Store mapping
    
    print(f"Loaded {len(accession_to_species)} accessions from FASTA.")  # Debugging
    return accession_to_species

# Step 1: Build a mapping of accession numbers to species names
accession_to_species = build_accession_species_mapping(input_fasta)

# Step 2: Write the mapping to a text file
with open(output_file, "w") as file:
    for accession, species in accession_to_species.items():
        file.write(f"{accession}\t{species}\n")

print(f"Accession-to-species mapping saved to: {output_file}")

