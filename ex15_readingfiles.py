from sys import argv # imports the argv feature

script, filename = argv # argument name is filename

txt = open(filename) # when txt i called it will open the filename given by argv


print "Here's your file %r:" % filename # it print the name of the file
print txt.read() # it will print the inside of the file

print "Type the filename again:" #print type the filename again
file_again = raw_input("> ") # ask to input the inside of the filename

txt_again = open(file_again) # file_again is named txt_again and it will open it

print txt_again.read() # print the inside of the file name.
