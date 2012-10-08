#!/usr/bin/env python

# Exercise DNA
# ============
#
# *Find positions of substring in larger string*

# The raw data is the string and substring in a file. Don't forget to strip
# the lines, to get rid of line-endings and whitespace.

in_hndl = open ('data/rosalind_subs.txt', 'r')
s = [s.strip() for s in in_hndl.readlines()]
big_s = s[0]
sub_s = s[1]

# Finding the locations of all substrings using Python turns out to be a
# strangely tricky proposition. The string "find" method simply find the
# first instance of a substring. Using regexes is the next obvious way. This
# seems like overkill and actually fails to find overlapping matches. So, we
# resign overselves to stepping over the string and looking for a match.

# A further trick is that the example given shows that they are expecting a
# 1-based answer, not a 0-based one. That is, the string position count from
# 1 upwards, such that if the larger string begins with the substring, the
# position reported is 1.

hits = []
for i in range (len(big_s) + 1 - len(sub_s)):
	big_s_slice = big_s[i:]
	if big_s_slice.startswith (sub_s):
		hits.append (i+1)

# To format the results correctly, we have to explciitly convert the integer
# results to a string.

results = ' '.join (["%s" % s for s in hits])

# Unfortunately, Rosalind kicked back my answer on this one several times.
# Despite checking it for errors and with other independent solutions, I
# seemed to have the right solution and even did an alternative solution
# to check. Eventually, the answer was marked as correct, so I'm inclined to
# think the datasets got mixed up.

print results

