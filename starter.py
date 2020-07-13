"""
starter.py

All text enclosed in triple quotes (regardless of line breaks inside) will turn into a comment. 
Comments will be ignored when the code, which means we can use this to document what our code does. 
"""

# using a hashtag is another way to comment. you need another hashtag if you are going to use multiple lines. 


# Remember those packages we installed into the conda environment? This is how we import and use them. 
import numpy as np 			# here, the syntax is import <package name> with an optional mechanism to rename the package. (as np)



def main(): 



# this is something that will appear pretty much in every python script. The explanation is a little bit complicated. 
# Basically, each file of our code can either be directly executed in command line (by using python <file name>)
# or we can reference the contents of the file in a different file (to organize our code better)

# The following line checks to see if we are currently directly executing this file. 
if __name__ == "__main__": 

	# this stuff will only run if we are executing this script. 

	# We can print things to the command line, which will show up when we run the file. 
	print("Hello! My name is Alex")

	# we can directly define variables and assign them values: 
	a = 1
	b = 2.0 
	

	# we can print out variables: 
	print(a)
	print(b)

	# we can do mathematical operations: 
	d = a + b
	# note that we are putting d on the left hand. 
	# you can think of the equals sign as saying "d receives the value of a + b"

	print(d)

	# We can also define a variable to be some text. This is called a String, bc it's a string of characters. 
	c = "Hi! Nice to meet you."

	# It can be printed. 
	print(c)

	# This is nice, but it also makes sense to have things that are not just single numbers or strings. 
	# We can define data structures like Lists. This is done by using brackets. 

	empty_list = [] 
	full_list = ["apple", "pear", "COVID"]

	print(empty_list)
	print(full_list)


	# Now, we're going to run a function

	main()