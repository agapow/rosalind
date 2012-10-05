in_hndl = open ('../data/rosalind_rna.txt', 'r')
s = in_hndl.read()
print s.replace('T', 'U')
