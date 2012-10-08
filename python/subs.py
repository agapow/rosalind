# Rosalind: exercise SUBS
# Find positions of substring in larger string

# read in the data
in_hndl = open ('data/rosalind_subs.txt', 'r')
s = [s.strip() for s in_hndl.readlines()]
big_s = s[0]
sub_s = s[1]


# print results
# note that rosalind doesn't want the termination symbol, which python provides
print bseq.translate()[:-1]

