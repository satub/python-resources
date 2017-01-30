## Python 3.x version of input_if_else.py code

#Python 3.x:
input_string = input("Enter a positive integer:\n")
n = int(input_string)

if n <= 0:
    print ("That's not very positive!")
elif n % 2 == 1:
    print ("Quite Odd.")
elif n % 2 == 0 and n > 100:
    print ("Livin' large, eh?")
else:
    print ("We are even.")
