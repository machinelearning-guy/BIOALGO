#dna tool kit file

nucleotides = ["A", "C", "G", "T"]


#check the sequence to make sure it is a DNA string
def validateseq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
        return tmpseq

