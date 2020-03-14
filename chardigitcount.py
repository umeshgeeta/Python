# author: Umesh Patil
# March 2020

# Problem - read a text file and return lower case, upper case, digit and
# all other characters in the text file.

# Method returns an array containing counts at index:
#
#	0: lower case character count
#	1: upper case character count
#	2: count of characters which are digits
#	3: count of all other characters
#
def countchars(filename):
	with open(filename) as tf:
		lowercasecount = 0
		uppercasecount = 0
		digits = 0
		otherchar = 0

		while True:
			line = tf.readline()
			if not line:
				break
			else:
				for c in line:
					if c.islower():
						lowercasecount += 1
					elif c.isupper():
						uppercasecount += 1
					elif c.isdigit():
						digits += 1
					else:
						otherchar += 1
	result = [lowercasecount, uppercasecount, digits, otherchar]
	return result



r = countchars("WhatIsNewInPython3.8.txt")
print(r)


#Umeshs-MacBook-Pro:Python umeshpatil$ python ./chardigitcount.py 
#[51801, 3184, 2450, 17755]
#Umeshs-MacBook-Pro:Python umeshpatil$ ls -lt
#total 224
#-rwxr--r--@ 1 umeshpatil  staff    870 Mar 13 22:06 chardigitcount.py
#-rw-r--r--@ 1 umeshpatil  staff  75190 Mar 13 15:59 WhatIsNewInPython3.8.txt
#-rwxr--r--@ 1 umeshpatil  staff    908 Mar 13 14:35 palindrome.py
#-rwxr--r--@ 1 umeshpatil  staff    936 Mar 12 23:03 prime.py
#-rwxr--r--@ 1 umeshpatil  staff    631 Mar 12 23:03 fibonacci.py
#-rwxr--r--@ 1 umeshpatil  staff    417 Mar 12 23:03 bubblesort.py
#-rwxr--r--@ 1 umeshpatil  staff   1021 Mar 12 23:03 startpyramid.py
#-rw-r--r--@ 1 umeshpatil  staff   1946 Nov 10 05:46 FillSquare.py
#-rw-r--r--@ 1 umeshpatil  staff   4998 Nov  9 19:34 FindPathsInGraph.py
#Umeshs-MacBook-Pro:Python umeshpatil$ pwd
#/Users/umeshpatil/git/Python
#Umeshs-MacBook-Pro:Python umeshpatil$ 
