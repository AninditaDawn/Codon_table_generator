# Project: Codon Table Generator
# Description: DNA and RNA sequence translation
# using the standard genetic code.

print("CODON TABLE GENERATOR")

print("Welcome to the Codon Table Generator!")

# Standard Genetic Code Dictionary
# creating the codon table
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

if not dna_sequence:
    print("Error: DNA sequence cannot be empty.")

elif not set(dna_sequence).issubset(valid_bases):
    print("Error: Invalid DNA sequence. Use only A, T, G, and C.")

else:
    print("Valid DNA sequence.")

    # Divide DNA sequence into codons
    codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]

    # Handle incomplete codons
    if len(dna_sequence) % 3 != 0:
        incomplete_bases = len(dna_sequence) % 3
        print("Incomplete bases:", dna_sequence[-incomplete_bases:])
        codons = codons[:-1]

    print("\nComplete codons:", codons)

    # Translate codons
    amino_acid_sequence = []

    for codon in codons:
        amino_acid_sequence.append(codon_table[codon])

    print("\nTranslated Amino Acid Sequence:")
    print(" - ".join(amino_acid_sequence))

    # Identify start and stop codons
    if start_codon in codons:
        print("Start codon ATG identified.")
    else:
        print("Start codon ATG not found.")

    found_stop_codons = [codon for codon in codons if codon in stop_codons]

    print("Stop codons identified:", found_stop_codons)

    # Identify and translate ORF
    if start_codon in codons:
        start_index = codons.index(start_codon)
        orf_amino_acids = []

        for codon in codons[start_index:]:
            orf_amino_acids.append(codon_table[codon])

            if codon in stop_codons:
                break

        print("\nORF Translation:")
        print(" - ".join(orf_amino_acids))
    else:
        print("No ORF found because the start codon is absent.")


# Accept RNA sequence from the user
print("\nRNA Sequence Input")
rna_sequence = input("Enter your RNA sequence, or press Enter to skip: ").upper()

# Validate and translate RNA sequence
if rna_sequence:
    if set(rna_sequence).issubset(set("AUGC")):
        print("Valid RNA sequence.")

        converted_dna = rna_sequence.replace("U", "T")
        print("Equivalent DNA sequence:", converted_dna)

        # Divide RNA sequence into codons
        rna_codons = [
            rna_sequence[i:i+3]
            for i in range(0, len(rna_sequence), 3)
        ]

        # Handle incomplete RNA codons
        if len(rna_sequence) % 3 != 0:
            incomplete_rna_bases = len(rna_sequence) % 3
            print("Incomplete RNA bases:", rna_sequence[-incomplete_rna_bases:])
            rna_codons = rna_codons[:-1]

        print("RNA Codons:", " - ".join(rna_codons))

        # Translate RNA codons
        rna_amino_acids = []

        for codon in rna_codons:
            dna_codon = codon.replace("U", "T")
            rna_amino_acids.append(codon_table[dna_codon])

        print("\nRNA Translated Amino Acid Sequence:")
        print(" - ".join(rna_amino_acids))

    else:
        print("Invalid RNA sequence. Use only A, U, G, and C.")

else:
    print("RNA input skipped.")

