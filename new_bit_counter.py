#Author is Flynn Acworth
file_content = open("zeros_and_ones.txt").read()
# I took the below method of counting from Vasilis' email. I assume that calculating the 1's this way is faster computationally
# and that is the reason for not simply running another .count on the file?

zeros = file_content.count("0")
ones= len(file_content)-zeros

one_count = 0
zero_count = 0
prev_bit = 0

results = [0,0] # the resulting streak of the zeros will be recorded in the results[0] index. ones will be results[1]


for bit in file_content:
	if bool(int(bit)): # if bit is a 1
		if bool(int(prev_bit)): # if previous bit is also a 1
			results[1] += 1# that means two 1s in a row. streak continues.
			results[0] = 1 # also means prev bit was not a zero, so reset zero count.
			continue
		else:
			results[1] = 1
	else:
		# if this bit was not a 1, it must be a 0. which means add one to the zero count
		results[0] += 1
	prev_bit = bit


print zeros
print ones
print "######################"
print "Longest zero chain: {}".format(results[0])
print "Longest one chain: {}".format(results[1])
