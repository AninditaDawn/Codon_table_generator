# ============================================
# Project: Codon Table Generator
# Description: DNA and RNA sequence translation
# using the standard genetic code.
# ============================================

print("===================================")
print("       CODON TABLE GENERATOR")
print("===================================")

print("Welcome to the Codon Table Generator!")


# Standard Genetic Code Dictionary

codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",

    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}


print("\nStandard Genetic Code:")

for codon, amino_acid in codon_table.items():
    print(codon, ":", amino_acid)

print("\nTotal codons:", len(codon_table))

# Define start and stop codons

start_codon = "ATG"

stop_codons = ["TAA", "TAG", "TGA"]

print("\nStart Codon:", start_codon)
print("Stop Codons:", stop_codons)


# Accept DNA sequence from the user

print("\nDNA Sequence Input")

dna_sequence = input("Enter your DNA sequence: ")

print("\nYour entered DNA sequence is:", dna_sequence)

# Convert DNA sequence to uppercase
dna_sequence = dna_sequence.upper()
print("\nStandardized DNA Sequence:", dna_sequence)

# Validate DNA sequence
valid_bases = set("ATGC")

if dna_sequence == "":
    print("Error: DNA sequence cannot be empty.")

elif not set(dna_sequence).issubset(valid_bases):
    print("Error: Invalid DNA sequence. Use only A, T, G, and C.")

else:
    print("Valid DNA sequence.")


# Divide DNA sequence into codons
codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]

print("\nCodons:")
print(" - ".join(codons))


# Handle incomplete codons
if len(dna_sequence) % 3 != 0:
    incomplete_bases = len(dna_sequence) % 3

    print("\nWarning: Incomplete codon at the end of the sequence.")
    print("Incomplete bases:", dna_sequence[-incomplete_bases:])

    codons = codons[:-1]

print("\nComplete codons:", codons)


# Translate codons into amino acids
amino_acid_sequence = []

for codon in codons:
    amino_acid = codon_table[codon]
    amino_acid_sequence.append(amino_acid)

print("\nTranslated Amino Acid Sequence:")
print(" - ".join(amino_acid_sequence))


# Identify start and stop codons
if start_codon in codons:
    print('Start codon ATG identified in the sequence.')
else:
    print('Start codon ATG not found.')

found_stop_codons = [codon for codon in codons if codon in stop_codons]

if found_stop_codons:
    print('Stop codons identified:', ', '.join(found_stop_codons))
else:
    print('No stop codons found.')
