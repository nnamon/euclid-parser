from pytesser import *

filename = raw_input("Enter filename: ")
text = image_file_to_string(filename, graceful_errors=True)
print "Text parsed: \n%s" % text
