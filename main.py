#DNA tookit test file

from DNAtoolkit import *
import random

randDNAstr = ''.join([random.choice(nucleotides)
                      for nuc in range(50)])

DNAstr = validateseq(randDNAstr)
print(countNucFrequency(randDNAstr))



