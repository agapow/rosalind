#!/usr/bin/env python

# Exercise CONS
# =============
#
# *Produce a consensus string and profile matrix from a set of sequences*

# First read in and tidy up the data.

in_hndl = open ('data/rosalind_cons.txt', 'r')
seqs = [s.strip() for s in in_hndl.readlines()]

# Then create the matrix you are going to fill.

seq_len = len (seqs[0])
bases = "ACGT"
matrix = []
for b in bases:
	matrix.append ([0] * seq_len)

# Now, for every position in the sequences, calculate the base frequency and
# insert it into the matrix at the right position.

for i in range (seq_len):
	# calculate freq
	freqs = {}
	for s in seqs:
		r = s[i]
		freqs[r] = freqs.get (r, 0) + 1
	# now put in matrix
	for j, b in enumerate (bases):
		base_freq = freqs.get (b, 0)
		matrix[j][i] = base_freq

# Calculate the consensus by seeing which residue is most frequent. Actually,
# we could have done this in the last step, but have it here for clarity.

conc_list = []
for i in range (seq_len):
	max_base = ''
	max_freq = 0
	for j, b in enumerate (bases):
		base_freq = matrix [j][i]
		if max_freq < base_freq:
			max_freq = base_freq
			max_base = b
	conc_list.append (max_base)

# Finally, present this crap in the right form.
print ''.join (conc_list)
for j, b in enumerate (bases):
	print "%s: %s" % (b, ' '.join (["%s" %s for s in matrix[j]]))
