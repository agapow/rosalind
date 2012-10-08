#!/usr/bin/env python

# Exercise SUBS
# =============
#
# *Find positions of substring in larger string, using a regex*

# Given that Rosalind won't accept my answer to this, it seems wise to
# solve it another way, using regexes. Note that REs won't find overlapping
# matches. 

in_hndl = open ('data/rosalind_subs.txt', 'r')
s = [s.strip() for s in in_hndl.readlines()]
big_s = s[0]
sub_s = s[1]

import re
hits = [m.start() + 1 for m in re.finditer (sub_s, big_s)]

results = ' '.join (["%s" % s for s in hits])

# This gives a quite different answer to the non-regex solution - due to the
# rejection of overlapping matches - which still isn't accepted by Rosalind!

print results

