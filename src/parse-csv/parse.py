
file_csv = open('movies2.csv', 'r')

# Read the first line (column names)
line = file_csv.readline()

# edit column awtype
# if awtype	is "H" and awattr has * then awtype append "H*"
# if awtype is "H" and awattr has ** then awtype append "H**"
# if awtype is "H" and awattr has *** then awtype append "H***"
# if awtype is "H" and awattr has **** then awtype append "H****"

# Read the rest of the lines
for line in file_csv:

    # Split the line into a list of strings
    fields = line.split(',')

    # replace all fields with quotes with \"
    # fields = [field.replace('"', '\\"') for field in fields]

    # Remove the newline character from the last field
    fields[-1] = fields[-1].strip()
    
    print(fields)

    if fields[7] == "H" and "*" in fields[8]:
        fields[7] += fields[8]
    
    # save changes to fields
    fields[5] = fields[5].lower()
    fields[6] = fields[6].lower()


with open('movies3.csv', 'w') as file_csv:
    file_csv.write(fields)

# Close the file
file_csv.close()
