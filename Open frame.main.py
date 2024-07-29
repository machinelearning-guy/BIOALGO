import re

def load_fasta(file_path):
    # Loads a FASTA file and returns the sequence as a string.
    with open(file_path, 'r') as file:
        lines = file.readlines()
    sequence = ''.join([line.strip() for line in lines if not line.startswith('>')])
    return sequence.upper()

def load_code(file_path):
    # Loads a codon table from a file into a dictionary.
    codon_table = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                codon, aa = parts
                codon_table[codon.upper()] = aa
    return codon_table

def translate_sequence(sequence, codon_table, start_pos=0, format_type='single'):
    # Translates a nucleotide sequence starting from a given position.
    translated = []
    for i in range(start_pos, len(sequence) - 2, 3):
        codon = sequence[i:i + 3].replace('T', 'U')
        amino_acid = codon_table.get(codon, 'X')  # 'X' for unknown codons
        translated.append(amino_acid)
    if format_type == 'single':
        return ''.join(translated)
    elif format_type == 'three-letter':
        return ','.join(translated)

def reverse_complement(sequence):
    # Returns the reverse complement of a nucleotide sequence.
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    return ''.join(complement[nuc] for nuc in reversed(sequence))

def generate_translations(sequence, codon_table, format_type):
    # Generates translations for all 6 frames.
    forward_frames = [translate_sequence(sequence, codon_table, start_pos=i, format_type=format_type) for i in range(3)]
    reverse_sequence = reverse_complement(sequence)
    reverse_frames = [translate_sequence(reverse_sequence, codon_table, start_pos=i, format_type=format_type) for i in range(3)]
    return forward_frames + reverse_frames

def main(codon_table_path, sequence_path, format_type='single'):
    # Load the codon table and sequence using utility module functions
    codon_table = load_code(codon_table_path)
    sequence = load_fasta(sequence_path)

    # Generate reverse complement of the sequence
    reverse_complement_sequence = reverse_complement(sequence)

    # Print original sequence and its reverse complement
    print(f"Original Sequence ({len(sequence)} bp):\n{sequence}\n")
    print(f"Reverse Complement ({len(reverse_complement_sequence)} bp):\n{reverse_complement_sequence}\n")

    # Generate and print translations for all 6 frames
    translations = generate_translations(sequence, codon_table, format_type)
    for frame_number, frame in enumerate(translations, start=1):
        frame_type = "Forward" if frame_number <= 3 else "Reverse"
        print(f"{frame_type} Frame {frame_number}:\n{frame}\n")

if __name__ == "__main__":
    codon_table_path = #inster file directory for codon data
    sequence_path = #insert file directory for sequence
    format_type = 'three-letter'  # change to 'three-letter' to use three-letter amino acid codes
    main(codon_table_path, sequence_path, format_type)
