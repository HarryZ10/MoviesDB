import os
from os.path import join, dirname

# Open the file for reading
ppl_path = os.path.join(os.path.dirname(__file__), "castsindex.csv")
f = open(ppl_path, "r")

# Read the first line (column names)
line = f.readline()

# Read the rest of the lines
for line in f:

    # Split the line into a list of strings
    fields = line.split(',')

    # Remove the newline character from the last field
    fields[-1] = fields[-1].strip()

    # propogate dir_id to empty fields below it
    if fields[0] != '':
        dir_id = fields[0]
    else:
        fields[0] = dir_id
    
    # write the record to the database
    print(fields)

    # write to a new file
    with open('castsindex2.csv', 'a') as w:
        
        entry = ','.join(fields)
        w.write(entry + '\n')

# Close the file
w.close()

# Close the file
f.close()

    