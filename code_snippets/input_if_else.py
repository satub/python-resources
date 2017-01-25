# This file shows comparison between ruby and python code that reads
# a numerical input from STDIN end evaluates it.
# Assumption: input is a number, the code snippet does no exception handling.

#Python 2.x:
input_string = raw_input("Enter a positive integer:\n")
n = int(input_string)

if n <= 0:
    print "That's not very positive!"
elif n % 2 == 1:
    print "Quite Odd."
elif n % 2 == 0 and n > 100:
    print "Livin' large, eh?"
else:
    print "We are even."

#Ruby:
# puts "Enter a positive integer:"
# n = gets.strip.to_i
#
# if n <= 0
#     puts "That's not very positive!"
# elsif n % 2 == 1
#     puts "Quite Odd."
# elsif n % 2 == 0 && n > 100
#     puts "Livin' large, eh?"
# else
#     puts "We are even."
# end
