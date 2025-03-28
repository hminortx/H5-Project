from Bio import SeqIO

# Path to the file containing the list of IDs (the new file with your IDs)
ids_file_path = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\MSA Results\GenBank Extraction\Updated extraction_14MAR2025\2163_updated_ids.txt"  # Replace with the actual path to your combined IDs file

# Path to your original FASTA file
fasta_file_path = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\All_Genomes_Species.fna"  # Replace with the path to your original FASTA file

# Path to save the new FASTA file with only the sequences matching the IDs
output_fasta_path = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\MSA Results\GenBank Extraction\extracted_fasta_sequences.fna"  # Path to save the output FASTA file

# Read the IDs from the combined file
def read_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read and clean the lines to get a list of IDs
        file_ids = [line.strip() for line in file.readlines()]
    return set(file_ids)

# Read the list of IDs
ids_to_extract = read_ids_from_file(ids_file_path)

# Extract sequences that match the IDs from the FASTA file
extracted_sequences = []

# Parse the FASTA file and check each record's ID
for record in SeqIO.parse(fasta_file_path, 'fasta'):
    # If the record ID is in the list of IDs to extract, add it to the extracted list
    if record.id in ids_to_extract:
        extracted_sequences.append(record)

# Write the extracted sequences to a new FASTA file
SeqIO.write(extracted_sequences, output_fasta_path, 'fasta')

# Print the number of sequences that were extracted
print(f"Total sequences extracted: {len(extracted_sequences)}")
