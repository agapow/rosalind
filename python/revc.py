# read in the data
in_hndl = open ('../data/rosalind_revc.txt', 'r')
s = in_hndl.read()

# there are lots of ways this could be done (for example, using the BioPython
# tools, using a dict to map characters) but for simplicity I just express
# the bases as a string, in which the complementary character is at the 
# opposite position (e.g. 1st base matches the 1st from the back)
bases = 'ACGT'

# we have to reverse the string first
s = list (s[::-1])
for i in range (len (s)):
	c = s[i]
	p = bases.index(c)
	s[i] = bases[3-p]

# print results
print ''.join (s)
