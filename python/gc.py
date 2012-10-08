#!/usr/bin/env python

# Exercise GC
# ===========
#
# *Return the id of the sequence with the greatest gc content and the percent*
#
# The data is in Fasta format, so with BioPython it is easy.

from Bio import SeqIO
seqs = SeqIO.parse (open ('data/rosalind_gc.txt'), 'fasta')

# For each sequence we manually calculate the GC content by doing a simple
# count of G and C across the sequence and dividing by the length. We keep
# track of the maximum as we go.

max_id = ''
max_gc = 0.0
for s in seqs:
	seq_len = len (s)
	seq_str = s.seq.tostring()
	gc = float (seq_str.count('G') + seq_str.count('C')) / seq_len
	if max_gc < gc:
		max_gc = gc
		max_id = s.id

# Finally, we print the result with a little bit of formatting. There are
# several ways you could format the numerical result, just watch out for the
# double percent.

print max_id
print "%2.4g%%" % (max_gc * 100)