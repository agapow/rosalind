# Ex. 4: HAMM
# calculate the Hamming distance between two strings

# read in the data
in_hndl = open ('data/rosalind_hamm.txt', 'r')
# need to remove newline chars off strings
s = [l.strip() for l in in_hndl.readlines()]
print s

# iterate over every position and compare chars
total = 0
max_len = len (s[0])

for i in range (max_len):
	if s[0][i] != s[1][i]:
		total += 1

# print result
print total 
