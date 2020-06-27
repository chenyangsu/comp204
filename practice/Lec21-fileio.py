f = open("patients.txt")
all_lines = f.readlines()

for line in all_lines:
	print("The line is", line.rstrip())
	#print("The line is", line)
f.close()
