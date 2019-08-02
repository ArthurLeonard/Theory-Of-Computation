import re # module for processing regular expressions https://docs.python.org/3/library/re.html
import sys
import csv
if __name__ == '__main__':
  # Exit if command line args entered incorrectly
  if len(sys.argv) != 2:
    print("usage: extract_links.py [input_file]")
    sys.exit(0)

# Filename is 2nd command line arg
filename = sys.argv[1]

# TODO Read HTML file
f = open("stackoverflow.html", "r")
txt = f.read()
#print(txt)

# TODO Set up regex
expression = r"https?:[\/]{2}.+\.[cn][eo][mt].*?"

# TODO Find links using regex, save in list called 'matches'
matches = re.findall(expression, txt)
#print(a)
f.close()
# Check matches, print results
# TODO Read in links from answers.txt (hint...this is a CSV file), 
f = open("answers.txt", "r")
answer_data = f.read()
print('read answers', answer_data)
# save in list called 'answer_data'


# Compare answers with matches found using regex, print out any mismatches
# UNCOMMENT BELOW WHEN READY TO CHECK IF YOUR REGEX IS FINDING ALL THE LINKS
result = "All links matched!"
if len( matches ) != len( answer_data ):
  result = "Your regex found %i matches. There should be %i matches" %(len( matches ), len( answer_data ) )
else:
  for i in range( len(answer_data) ):
    if( matches[i] != answer_data[i] ):
      result = "Mismatched link. Got %s but expected %s" % ( matches[i], answer_data[i] )
      break
print( result )