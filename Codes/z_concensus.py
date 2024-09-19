import os
from Bio import SeqIO
from collections import defaultdict

# Path to the directory containing the 1166 folders
base_path = "user/work/xl23854/mitos2_output_zhokhov"

# List of target genes to extract
target_genes = ['atp6', 'atp8', 'rrnL', 'rrnS', 'nad1', 'nad2', 'nad3', 'nad4', 'nad4l', 'nad5', 'nad6', 'cox1', 'cox2', 'cox3', 'cob']

# Dictionary to hold the sequences for each gene
gene_sequences = {gene: [] for gene in target_genes}

# Iterate over each folder
for i in range(1166):
    folder_path = os.path.join(base_path, str(i))
    print(folder_path)
    result_file = os.path.join(folder_path, 'result.fas')
    print(i)
    if os.path.isfile(result_file):
	#print(i)
        # Read the result.fas file
        with open(result_file, 'r') as file:
            for record in SeqIO.parse(file, 'fasta'):
                description = record.description
                sequence = str(record.seq)
                
                # Extract the gene name from the description
                gene_name = description.split('; ')[-1].split('(')[0]
                
                # Check if the gene name is in the list of target genes
                if gene_name in target_genes:
                    gene_sequences[gene_name].append(f">{description}\n{sequence}")

# Write the extracted sequences into separate files for each gene
output_dir = "user/work/xl23854/concensus_folder"
os.makedirs(output_dir, exist_ok=True)

for gene, sequences in gene_sequences.items():
    output_file = os.path.join(output_dir, f"{gene}_zhokhov.fasta")
    with open(output_file, 'w') as out_file:
        out_file.write("\n".join(sequences))

print("Gene extraction and file creation completed.")

