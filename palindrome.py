# author: Umesh Patil
# March 2020

# The slice statement [::-1] means start at the end of the string and
# end at position 0, move with the step -1, negative one, which means 
# one step backwards. This makes finding palindrome a trivial exercise.

def isPalindrome(a):
	if a is None or a == "":
		print("No characters, not palindrome applicable.")
		return False
	else:
		b = a[::-1]
		if a == b:
			return True
		else:
			return False

a = None
palind = isPalindrome(a)
assert palind == False

a = 'x'
palind = isPalindrome(a)
if palind:
	print (a+" is a palindrome")

a = 'xyz'
palind = isPalindrome(a)
if not palind:
	print (a+" is not a palindrome")

a = 'xabccbax'
palind = isPalindrome(a)
if palind:
	print (a+" is a palindrome")

a = 'pqrxrqp'
palind = isPalindrome(a)
if palind:
	print (a+" is a palindrome")

a = 'pqrxrqfp'
palind = isPalindrome(a)
if not palind:
	print (a+" is not a palindrome")