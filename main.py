#DNA tookit test file

from DNAtoolkit import *
import random

randDNAstr = ''.join([random.choice(nucleotides)
                      for nuc in range(50)])

DNAstr = validateseq(randDNAstr)


print(f'\nsequence: {DNAstr}\n')
print(f'[1] + sequence length: {len(DNAstr)}\n')
print(f'[2] + sequence length: {countNucFrequency(DNAstr)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(DNAstr)}\n')





