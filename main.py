#DNA tookit test file

from DNAtoolkit import *
import random

import utilities import colored 

randDNAstr = ''.join([random.choice(nucleotides)
                      for nuc in range(50)])

DNAstr = validateseq(randDNAstr)

print(f'\nsequence: {colored(DNAstr)}\n')
print(f'\nsequence: {DNAstr}\n')
print(f'[1] + sequence length: {len(DNAstr)}\n')
print(f'[2] + sequence length: {countNucFrequency(DNAstr)}\n')
print(f'[3] + DNA/RNA Transcription: {transcription(DNAstr)}\n')
print(f"[4] + DNA string + Reverse Transcription:\n5' {DNAstr} 3'")
print(f"    {''.join(['|' for c in range(len(DNAstr))])}")
print(f"3' {reverse_complement(DNAstr)[::-1]} 5' [Complement]\n")
print(f"5' {reverse_complement(DNAstr)} 3' [Rev. compliment]\n")





# last lines creates a copy of DNA replication transcription and reverse transcription during replication. 






