#dna tool kit file

nucleotides = ["A", "C", "G", "T"]


#check the sequence to make sure it is a DNA string
def validateseq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
        return tmpseq
#uses a dictionary to print the amount of individual nucleotides which is useful in mapping purposes later
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0,  "C": 0,  "G": 0,  "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

#replicating transcription and translation::

def transcription(seq):
    return seq.replace("T", "U")

def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]












