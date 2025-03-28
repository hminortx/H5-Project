import os

def process_fna_files(main_directory, output_directory, separator="NNNNNNNNNN"):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for genome_folder in os.listdir(main_directory):
        genome_path = os.path.join(main_directory, genome_folder)

        if os.path.isdir(genome_path):
            fna_files = [f for f in os.listdir(genome_path) if f.endswith('.fna')]

            for fna_file in fna_files:
                input_path = os.path.join(genome_path, fna_file)
                output_path = os.path.join(output_directory, f"{genome_folder}.fna")  # Naming output after folder

                with open(input_path, 'r') as infile:
                    lines = infile.readlines()

                sequences = []
                current_sequence = []

                for line in lines:
                    if line.startswith(">"):
                        if current_sequence:  # Store previous segment before starting a new one
                            sequences.append("".join(current_sequence))
                            current_sequence = []

			if not original_header:
    			original_header = line.strip()  # Save the first header
                    else:
                        current_sequence.append(line.strip())

                if current_sequence:  # Append the last segment
                    sequences.append("".join(current_sequence))

                # Join all segments with the separator
                concatenated_sequence = separator.join(sequences)

                # Use the original header (first header in the file)
                fasta_header = original

                with open(output_path, 'w') as outfile:
                    outfile.write(f"{fasta_header}\n{concatenated_sequence}\n")

                print(f"Processed: {input_path} -> {output_path}")

# Example usage
main_directory = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\ncbi_viral_AvianOnly_dataset\ncbi_dataset\data"
output_directory = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\ncbi_viral_AvianOnly_dataset\ncbi_dataset\Compiled_genomes_SPECIES"
separator = "NNNNNNNNNN"  # Customizable separator between segments

process_fna_files(main_directory, output_directory, separator)


import os

def merge_fasta_files(output_directory, final_output_file):
    with open(final_output_file, 'w') as outfile:
        for file_name in os.listdir(output_directory):
            if file_name.endswith('.fna'):
                file_path = os.path.join(output_directory, file_name)
                
                with open(file_path, 'r') as infile:
                    outfile.write(infile.read() + "\n")  # Add newline between files
                
                print(f"Merged: {file_path}")

# Example usage
output_directory = r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\ncbi_viral_AvianOnly_dataset\ncbi_dataset\Compiled_genomes_SPECIES"
final_output_file = os.path.join(output_directory, "All_Viral_Genomes_Species.fna")

merge_fasta_files(output_directory, final_output_file)



