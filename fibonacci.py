# author: Umesh Patil
# March 2020

# Produce Fibonacci numbers till the given limit
# Output:	0,1,1,2,3,5,8,13,21,34,....f<limit


def finboncci(limit):
	if limit > -1:
		output=""
		p=0
		q=1
		while p <= limit:
			output=output + ' ' + str(p)
			t = q
			q = p + q
			p = t
		print(output)
	else:
		print("Less than 0 argument, cannot produce regular Fibonacci Sequence.")


finboncci(-3)
print(' ')

finboncci(0)
print(' ')

finboncci(1)
print(' ')

finboncci(2)
print(' ')

finboncci(3)
print(' ')

finboncci(4)
print(' ')

finboncci(5)
print(' ')

finboncci(10)
print(' ')

finboncci(50)
print(' ')

finboncci(200)
print(' ')