# author: Umesh Patil
# March 2020

# Print star pyramid. For the input k, base will be 2k+1 and height k+1.

def starpyramid(k):
	if k > -1:
		for row in range(k+1):
			line=""
			# First segment of blank spaces.
			for j in range(k-row):
				line=line+' '
			# Second segment of actual stars.
			for j in range(k-row,k+row+1):
				line=line+'*'
			# Third segment is optional, we could decide to leave it blank actually.
			# Added here for the demonstration purposes.
			for j in range(k+row+1,2*k+1):
				line=line+' '
			print(line)
	else:
		print("Negative argument, cannot print the pyramid")


starpyramid(0)
print("-----------------------------------")
starpyramid(1)
print("-----------------------------------")
starpyramid(2)
print("-----------------------------------")
starpyramid(3)
print("-----------------------------------")
starpyramid(4)
print("-----------------------------------")
starpyramid(5)
print("-----------------------------------")
starpyramid(8)
print("-----------------------------------")