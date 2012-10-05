in_hndl = open ('../data/rosalind_revc.txt', 'r')
s = in_hndl.read()
bases = 'ACGT'
s = list (s[::-1])
for i in range (len (s)):
	c = s[i]
	p = bases.index(c)
	s[i] = bases[3-p]
print ''.join (s)
