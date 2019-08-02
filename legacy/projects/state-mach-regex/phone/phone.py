import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
expression = r"\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}"

while line != "exit":
    # TODO Find matches
    match = re.findall(expression, line)
    
    # TODO If no match found, print that no number was found
    if len(match) == 0:
   		print("No valid phone number found")

    
    # TODO Else, break number up into area code, prefix, and suffic
    else:
   		print("Area code:", match[0][0:3])
   		print("Prefix:", match[0][3:6])
   		print("Suffix:", match[0][6:10])

    
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!
    
    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")