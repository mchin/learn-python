# Write a program that prints out its own command line arguments in reverse order from last to first.

# To run the program in the command line:
# python3 nameoffile.py [add your various arguments here with spaces between]
# python3 nameoffile.py This is my cool program woo
# sys.argv is a list in Python, which contains the command-line arguments passed to the script.

# import sys module which is needed for using sys.argv
import sys

print('Here are the command line arguments in reverse order from last to first:')

# iterate to cycle through the arguments and print each as well
for cl_arg in reversed(sys.argv):
   print(cl_arg)
