# author: Umesh Patil
# March 2020

# Basic bubble sort implementation

def bs(a):
	if a is not None:
		# We need stop at the second last element so that, last 2 can be compared.
		b=len(a)-1
		for x in range(b):
		    for y in range(b-x):
		        if a[y] > a[y+1]:
		            a[y],a[y+1] = a[y+1],a[y]
		return a
	else:
		print("Empty argument, nothing to sort")


a=[32,5,3,6,7,45,54,87,98,32]
b=bs(a)
print(b)