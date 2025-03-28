
from ete3 import Tree

# Step 1: Load the Newick file
tree = Tree(r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\Vsearch Results\Cluster Data (UC files)\vsearch_clusters_93percent.nwk")  # replace with your file path

# Step 2: Define your dictionary (mapping accession numbers to species names)
# Load the accession_species_mapping_ANIMAL.txt file into a dictionary
accession_to_species = {}
with open(r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\accession_species_mapping_ANIMAL.txt", 'r') as f:
    for line in f:
        # Assuming the file is tab-separated, adjust if the format is different
        accession, species = line.strip().split('\t')
        accession_to_species[accession] = species

# Step 3: Replace the accession numbers with species names
for node in tree.traverse():
    if node.is_leaf():  # Only process leaves (tips of the tree)
        accession = node.name
        if accession in accession_to_species:
            node.name = accession_to_species[accession]

# Step 4: Save the modified tree back to a Newick file
tree.write(outfile=r"C:\Users\hmino\OneDrive\Desktop\Capstone Class\Avian_Cattle_dataset\Vsearch Results\Cluster Data (UC files)\modified_tree_93percent.nwk") 
