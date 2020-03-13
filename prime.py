# author: Umesh Patil
# March 2020

# Problem - to determine if the given +ve integer is a prime or not.
#
# All primes greater than 6 are of the form 6k - 1 or 6k + 1. 
# This is because all integers can be expressed as (6k + i) for some
# integer k and for i = -1, 0, 1, 2, 3, or 4. So the algorithm checks
# divisibility by 6k-i / 6k+i till square root of n.

# Ref. - https://en.wikipedia.org/wiki/Primality_test

def isPrime(n):
	if n < 1:
		print("Provide a positive integer number.")
	else:
		if n < 4:
			return "Yes"
		if n % 2 == 0 or n % 3 == 0:
			return "No"
		i = 5
		while i * i <= n:
			if n % i == 0 or n % (i+2) == 0:
				return "No"
			i += 6
		return "Yes"

def findPrimes(limit):
	if limit < 1:
		print("Provide a positive integer number.")
	else:
		output = ''
		for n in range(limit+1):
			if isPrime(n) == 'Yes':
				output = output + ' ' + str(n)
		print(output)


print("Primes under 200 are:")
findPrimes(200)