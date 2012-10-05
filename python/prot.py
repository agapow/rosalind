# read in the data
in_hndl = open ('data/rosalind_prot.txt', 'r')
s = in_hndl.read().strip()

# we have to bring in Biopython here, it would be foolish to do it otherwise

# make a sequence
from Bio.Alphabet import *
from Bio.Seq import Seq
bseq = Seq (s, RNAAlphabet())

# print results
# note that rosalind doesn't want the termination symbol, which python provides
print bseq.translate()[:-1]

