#!/usr/bin/env python

# Exercise GRPH
# =============
#
# *Return the adjacency table of sequences, based on suffixes linking to prefixes*
#
# Again, the data is in Fasta format, so with BioPython it is easy.

from Bio import SeqIO
seqs = [s for s in SeqIO.parse (open ('data/rosalind_grph.txt'), 'fasta')]

# The adjacency table is really just a set of pairs, with the end of the first
# part matching the start of the second part. The matching length we are
# looking for is 3.

graph = []
match_len = 3
for s in seqs:
	for t in seqs:
		if s != t:
			if s.seq.tostring()[-3:] == t.seq.tostring()[:3]:
				print s.id, t.id

