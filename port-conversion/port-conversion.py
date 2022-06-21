# Header required by the FMC to import objects
header = ['', '', '', '', '']
output = []

# Get the files from the user
txtfile = input(r"Please enter the name of the text file you would like to convert:")
csvfile = input(r"Please enter the name of the csv file you like to receive:")

# Open txt file that will be used to add data to CSV
with open(txtfile, 'r') as f:
    ol = f.readlines()
    nl = []
    prefix = 'object'

    # Removes new line character from list objects
    for i in ol:
        nl.append(i.replace("\n", ""))

    # Combines objects to make easier to work with
    for item in nl:
        if item.startswith(prefix) or not output:
            output.append(item)
        else:
            output[-1] += item

    # Splits each object into it's own list
    testlist = []
    for x in output:
        y = x.split(" ")
        testlist.append(y)

print(testlist)