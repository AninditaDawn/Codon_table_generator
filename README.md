# Codon Table Generator

A Python-based project that accepts DNA and RNA sequences, identifies codons, and translates nucleotide sequences into their corresponding amino acids using the standard genetic code.

## Project Overview

The Codon Table Generator is designed to demonstrate the basic principles of genetic code interpretation and sequence translation. It uses a Python dictionary containing all 64 codons of the standard genetic code to convert nucleotide triplets into their corresponding amino acids.

The program also performs sequence validation, identifies start and stop codons, and handles incomplete codons at the end of a sequence.

## Features

- **Complete Codon Table:** Contains all 64 codons of the standard genetic code.
- **DNA Sequence Input:** Accepts DNA sequences containing A, T, G, and C.
- **RNA Sequence Input:** Accepts RNA sequences containing A, U, G, and C.
- **Sequence Validation:** Checks whether the entered sequence contains valid nucleotide bases.
- **Codon Identification:** Divides nucleotide sequences into groups of three bases.
- **Incomplete Codon Handling:** Identifies and excludes incomplete trailing codons from translation.
- **Amino Acid Translation:** Converts codons into their corresponding amino acids.
- **Start and Stop Codon Identification:** Identifies ATG as the start codon and TAA, TAG, and TGA as stop codons in DNA sequences.
- **Open Reading Frame (ORF) Translation:** Identifies the first ATG codon and translates the sequence from that point until the first in-frame stop codon.


## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run the Python script:

bash
python codon_generator.py


4. Enter a DNA sequence when prompted.
5. Enter an RNA sequence when prompted, or press Enter to skip RNA translation.

## Example

**Input DNA sequence:**

ATGGCTTTTTAA

**Codon identification:**

ATG - GCT - TTT - TAA

**Translated amino acid sequence:**


Methionine - Alanine - Phenylalanine - Stop

**Start codon:** ATG

**Stop codon identified:** TAA

**Input RNA sequence:**

AUGGCUUUUUAA

The RNA sequence is translated into the same amino acid sequence using the corresponding DNA codons for lookup.

## Project Structure

Codon_table_generator/
│
├── codon_generator.py
└── README.md

## Learning Objectives

- Understand the standard genetic code and codon–amino acid relationships.
- Apply Python dictionaries and conditional statements.
- Perform sequence validation and string manipulation.
- Understand codon identification and translation.
- Explore start codons, stop codons, and open reading frames.
- Use Git and GitHub for version control and project documentation.

## Author

**Anindita Dawn**
