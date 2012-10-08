
in_hndl = File.open ('data/rosalind_subs.txt')

s = in_hndl.gets.strip
pattern = Regexp.new(in_hndl.gets.strip)

puts [].tap { |offsets|
	offset = 0
	while s[offset..-1][pattern]
		offsets << offsets.last.to_i + Regexp.last_match.offset(0)[0] + 1
		offset = offsets.last
	end
}.join(' ')

