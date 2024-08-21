# Get the name of the input file
input_file_name = input()

# Open the input file
f = open(input_file_name)

# Print contents of input file
for line in f:
    print(line)     

# Close the input file
f.close()