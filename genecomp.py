from test_main import *

element_to_count = ['A', 'T', 'G', 'C']

letter_count_patient1 = {letter: patient1.count(letter) for letter in element_to_count}
letter_count_patient2 = {letter: patient2.count(letter) for letter in element_to_count}

for letter in element_to_count:
    print(f"occurence of '{letter} in patient1: {letter_count_patient1}")
    print(f"occurence of '{letter} in patient2: {letter_count_patient2}")


segment1 = patient1[:2000]
segment2 = patient2[:2000]

def compare_seqeunces(seq1, seq2):
    differences = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            differences.append(f"{i+1}:{seq1[i]} -> {seq2[i]}")
    return differences

differences = compare_seqeunces(segment1, segment2)

print(f"segment 1: {segment1}")
print(f"segment 2: {segment2}")
if differences:
    print("differences (position:sequence1->sequence2):")
    for difference in differences:
        print(difference)
else:
    print("no difference has been found.")

def compare_sequences_summary(seq1, seq2):
    difference_count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            difference_count += 1
    return difference_count

differences_count = compare_sequences_summary(segment1, segment2)
print(f"Total differences: {differences_count}")

def count_codons(sequence):
    codon_count = {}
    
    for i in range(0, len(sequence) - len(sequence) % 3, 3):
        codon = sequence[i:i+3]
        if codon in codon_count:
            codon_count[codon] += 1
        else:
            codon_count[codon] = 1
    return codon_count


sequence = patient1 + patient2
codon_counts = count_codons(sequence)
print("Codon counts:", codon_counts)


def compare_sequences_with_codons(seq1, seq2):
    differences = []
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] != seq2[i]:

            codon_start_index = i - (i % 3)
            codon1 = seq1[codon_start_index:codon_start_index + 3]
            codon2 = seq2[codon_start_index:codon_start_index + 3]
            differences.append(f"Position {i+1} (Codon: {codon1} -> {codon2})")
    return differences


differences = compare_sequences_with_codons(segment1, segment2)

print("Differences (position and codon change):")
for difference in differences:
    print(difference)
