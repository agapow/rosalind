in_hndl = open ('../data/rosalind_dna.txt', 'r')
s = in_hndl.read()
print ' '.join ([s.count(c) for c in 'ACGT']
