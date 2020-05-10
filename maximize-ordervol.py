# author: Umesh Patil
# May 2020
#
# Problem:		Assume a company takes orders over phone calls and wants to
# 				maximize the total order volume in a given work day. Also it
#				knows which call comes at what time, what is the duration of
#				that call and order volume. (Maybe using Big Data it predicts.)
#				We want to find a sequence of calls which an operator can pick
#				to maximize the volume. At one point, an operator can only take
#				one call.
#
# Source:		HackerRank
#				TBD - Find URL
#
# Solution:		Basically it is a dynamic programming exercise. To refresh my
# 				understanding of Knapsack problems are addressed, I found very
#				useful article:
#				https://medium.com/@fabianterh/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf
#
#				So modelled my solution along the lines. Each incoming call is
#				a row of the grid we want to build. For column, I took One Hour
#				window. So basically we go on building for k calls up to 'h'
#				hour, what is the optimal solution. And then build next cells.

# Assumptions:	Start time for each call is given in minutes measured from the start of
#				the work day.
#
# Implementation: Matrix is made up of a MatrixCell. Each MatrixCell contains a
#				CallSequence. CallSequence is made up of a Call. Core methods are
#				'fitCallSubSeq' in CallSequence and 'computecell' in Matrix.
#
class CallSequence:

	def __init__(self):
		self.calls = list()
		self.vol = 0 	# accumulated order volume from these calls

	def append(self, call):
		self.calls.append(call)
		self.vol = self.vol + call.volume()

	def recompute(self):
		l = len(self.calls)
		if l > 0:
			v = 0
			for i in range(l):
				v += self.calls[i].volume
		else:
			self.vol = 0

	def remove(self, call):
		self.calls.remove(call)
		self.recompute()

	def clone(self):
		ccs = CallSequence()
		# shallow copy 
		ccs.calls = self.calls[:]
		ccs.vol = self.vol
		return ccs

	def len(self):
		return len(self.calls)

	def get(self, index):
		return self.calls[index]

	def tailcall(self, which):
		return self.get(self.len() - which)

	def last(self):
		return self.tailcall(1)

	def end(self):
		l = self.len()
		if l > 0:
			return self.calls[ l -1].end()
		else:
			return 0

	def start(self):
		l = self.len()
		if l > 0:
			return self.calls[0].start()
		else:
			return 0

	def volume(self):
		return self.vol

	# attempts to fit the incoming call
	def fitCallSubSeq(self, call):
		fcs = CallSequence()
		# If self is empty, we fit the incoming always.
		if self.len() == 0:
			fcs.append(call)
			return fcs
		# else rest of the processing
		i = 0
		l = self.len()
		done = False
		while not done and i < l:
			c = self.get(i)
			if c.end() < call.start():
				fcs.append(c)
			else:
				# Ok c is ending after call starts, meaning these 2 calls
				# are overlapping. The decision of ripping the current
				# call sequence should be based on what total volumes are
				# saying. What we do here is we know the volume of the
				# current call sequence which we are evaluating to change.
				# 'fcs' is build so far, we take its volume, add to that
				# the incoming call's volume and compare. Only if we have
				# more volume, we create fcs differently.
				if fcs.volume() + call.volume() > self.volume():
					fcs.append(call)
				else:
					# we say fcs needs to be same as self
					fcs = self.clone()
				# no matter are done here
				done = True
			i += 1
		if not done:
			# we came out of the while loop because i = l
			# which implies all of self's calls end before in the incoming
			# starts. That means we need to simply add incoming to the end.
			fcs.append(call)
		return fcs

	def tostring(self):
		result = str(self.vol) + '['
		l = self.len()
		for i in range(l):
			result = result + str(self.get(i).globalindex()) + ','
		result = result + ']'
		return result

class Call:

	def __init__(self, gi, st, dur, vol):
		# Call refers to a call which is 'gi' in the given input list
		self.gi = gi
		self.st = st
		self.dur = dur
		self.vol = vol

	def end(self):
		return self.st + self.dur

	def start(self):
		return self.st

	def volume(self):
		return self.vol

	def duration(self):
		return self.dur

	def globalindex(self):
		return self.gi

	def tostring(self):
		return '(' + str(self.gi) + ',' + str(self.st) + ',' + str(self.dur) + ',' + str(self.vol) + ')'

class MatrixCell:

	def __init__(self, mr, mc):
		# row id in the matrix
		# it implies that we have considered first 'mr' calls of the given call list
		self.matrix_row = mr
		# c is the workday duration, say how many hours are considered
		# so far
		self.matrix_col = mc
		# Call sequence associated with the cell
		self.callseq = CallSequence()

	def volume(self):
		return self.callseq.volume()

	def end(self):
		return self.callseq.end

	def start(self):
		return self.callseq.start

	def sequence(self):
		return self.callseq

	def setsequence(self, seq):
		self.callseq = seq
		
	def clone(self):
		m = MatrixCell(self.matrix_row, self.matrix_col)
		m.setsequence(self.sequence().clone())
		return m

class Matrix:

	def __init__(self, input, cols):
		self.endtime = list()
		self.grid = list()
		self.input = input
		self.columns = cols

		call_count = input.len()
		for r in range(call_count+1):
			row = list()
			self.grid.append(row)

		# add empty call sequences in the first row and first call
		# when there is no call, there is nothing maximize regardless 
		# of how many wayday hours available and when there is work
		# day hour available it does not matter who many calls are feasible.
		for c in range(self.columns):
			self.grid[0].append(MatrixCell(0, c))
			self.endtime.append(c * 60)

		# and we will have to add the last hour too since range excludes the last value
		self.endtime.append(self.columns * 60)

		for r in range(call_count +1):
			self.grid[r].append(MatrixCell(r, 0))

	# In this method we evaluate whether including the incoming call can
	# maximize our order volume.
	#
	# Basic algorithm is we note the order volume without this call included
	# first. That value is nothing but volume in previous row of the same
	# column. Next we start the process of evaluating whether we can include
	# the incoming call in the mix or not. If the previous call sequence
	# (previous row, same column) ends before the start of the incoming
	# call and the incoming call completes before the end of this hour i.e.
	# col work day; we simply include it and add the volume. If the current
	# call cannot be finished by the end of the current work day / hour; we
	# simply do not include it. We want our call sequence to be complete by
	# the current hour. So if the incoming call ends by the hour in question, 
	# but the incoming call starts before the current sequence ends; we have 
	# to see if we can remove the previous call to accomodate the current call 
	# IF order volume of the current call is bigger than the call to be replaced. 
	# If the previous call also can not accomodate the incoming call and if it's 
	# order volume is justified removal of that call also; we keep moving up 
	# the chain in removing calls. That is you keep traversing in previous 
	# rows in the same column.
	def computecell(self, matrix_row, matrix_col):
		# let us determine first the incoming call based on arguments passed
		# it is always row index value minus one because we added empty row in the grid already
		incoming_call = self.input.get(matrix_row -1)
		previous_matrix_cell = self.grid[matrix_row -1][matrix_col]
		if incoming_call.end() > self.endtime[matrix_col]:
			# regardless, the incoming call is finishing after the current hour
			# we have to let go the current call and just keep the call
			# sequence as is - meaning without the current call.
			mtx_cell = previous_matrix_cell.clone()
			self.grid[matrix_row].append(mtx_cell)
		else:
			mc = MatrixCell(matrix_row, matrix_col)
			# End time of the incoming call is within the limit
			if incoming_call.start() >= previous_matrix_cell.end():
				# incoming call starts on or after the end of the previous
				# sequence and it's end time does not exceed the column limit;
				# we simply add it!
				seq = previous_matrix_cell.sequence().clone()
				seq.append(incoming_call)
				mc.setsequence(seq)
			else:
				# we need to evaluate the option of kicking out most recently 
				# added calls to make a room for this incoming one assuming
				# that results in higher order volume
				previous_vol = previous_matrix_cell.volume()
				fcs = previous_matrix_cell.sequence().fitCallSubSeq(incoming_call)
				if fcs.volume > previous_vol:
					# we take this new call sequence
					mc.setsequence(fcs)
				else:
					# we just carry the previous as is
					seq = previous_matrix_cell.sequence().clone()
					mc.setsequence(seq)
			self.grid[matrix_row].append(mc)

	def rowstring(self, row):
		result = ''
		how_many_in_row = len(self.grid[row])
		# print('how_many_in_row: ' + str(how_many_in_row) + str(self.grid[row]))
		for r in range(how_many_in_row):
			result += self.grid[row][r].sequence().tostring() + '\t\t'
		return result

	def printmatrix(self):
		print('-\t\t\t0\t\t1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8')
		# first row implies to call considered
		print('-\t\t\t' + self.rowstring(0))
		for i in range(1, self.input.len( ) +1):
			call_str = self.input.get( i -1).tostring() + '\t'
			row_str = self.rowstring(i)
			print(call_str +'\t ' +row_str)


# start:	list of numbers, time points where the call would start
#			it is minutes measured from the word day start point
# duration: list of call duration, assunmed in minutes
# volume:	how much order volume we expect from a call
# ith value in all 3 lists corresponds to the 'i'th call.
def phoneCalls(start, duration, volume):
	call_count = len(start)
	global inputCallSequence
	inputCallSequence = CallSequence()
	workday = 0
	for c in range(call_count):
		inputCallSequence.append(Call(c, start[c], duration[c], volume[c]))
		d = start[c] + duration[c]
		if d > workday:
			workday = d

	workdayhours = workday / 60
	if (workday % 60) > 0:
		workdayhours += 1
	print('Hours in the workday: ' + str(workdayhours))
	matrix = Matrix(inputCallSequence, workdayhours)

	# First row and first columns(0th row and 0th column) are already set, 
	# we start from second row and second column (the first call in the
	# first hour).

	for r in range(1, call_count+1):
		for c in range(1, workdayhours+1):
			matrix.computecell(r, c)
			# if you want to know grid immediately after each matrix cell computation
			# uncomment the below print statement
			# matrix.printmatrix()

	matrix.printmatrix()
	print('Maximum order volume attainable is: ' + str(matrix.grid[call_count][workdayhours].volume()))
		
if __name__ == '__main__':

	start 		= [2, 70, 122, 181]
	duration	= [40, 30, 60, 60]
	volume 		= [10, 40, 30, 31]

	phoneCalls(start, duration, volume)

	# Expected output is:
	# Hours in the workday: 5
	# -			0		1		2		3		4		5		6		7		8
	# -			0[]		0[]		0[]		0[]		0[]		0[]
	# (0,2,40,10)		 0[]		10[0,]		10[0,]		10[0,]		10[0,]		10[0,]
	# (1,70,30,40)		 0[]		10[0,]		50[0,1,]		50[0,1,]		50[0,1,]		50[0,1,]
	# (2,122,60,30)		 0[]		10[0,]		50[0,1,]		50[0,1,]		80[0,1,2,]		80[0,1,2,]
	# (3,181,60,31)		 0[]		10[0,]		50[0,1,]		50[0,1,]		80[0,1,2,]		81[0,1,3,]
	# Maximum order volume attainable is: 81