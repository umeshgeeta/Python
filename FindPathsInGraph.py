# author: Umesh Patil
# November 9, 2019

# Finds number of paths and cycles in a random generated graph. Edge is redirections.
# When a value in the adjecancy graph cell [i][j] is > -1; it means there is an edge
# goinf from 'i' node to 'j' node. Nodes will be numbered from 0 to m-1 for m nodes graph.
#
# Assumptions:
# 1. We want to go from Node '0' to Node 'size -1'.

# imports random module 
import random 

# Creates a 2 dimensional array initialized to 0.
def matrix(size):
  # Creates a list containing size lists, each of size items, all set to 0
  w, h = size, size;
  matrix = [[-1 for x in range(w)] for y in range(h)] 
  return matrix
  
# Prints the matrix as m lines, each with m columns separated by a single space.
def printmatrix(m, size):
  for i in range(size):
    line = ''
    for j in range(size):
      line = line + str(m[i][j]) + ' '
    print(line)
    
def createrandomgraph(m, size, edgecount):
	edge = 0
	while edge < edgecount:
		i = random.randrange(0, size)
		j = random.randrange(0, size)
		while i == j:
			j = random.randrange(0, size)
      
		if m[i][j] < 0:
			m[i][j] = 0
			edge = edge + 1

def findzeroinrow(m, size, row, nonexhaustednodes):
	col = -1
	j = 0
	while col < 0 and j < size:
		#print('m['+str(row)+']['+str(j)+'] ='+str(m[row][j]))
		if m[row][j] == 0:
			col = j
		j = j + 1
	added = False
	while j < size and not added:
		if m[row][j] == 0:
			#there are more edges to be explored from this node
			nonexhaustednodes.add(row)
			added = True
		j = j + 1
	return col

def findunexplorededge(m, size, row, exhaustedsegments):
	print('exhaustedsegments ' + str(exhaustedsegments))
	unexplorededge = -1
	j = 0
	while unexplorededge < 0 and j < size:
		segid = m[row][j]
		if segid > -1 and segid not in exhaustedsegments:
			unexplorededge = j	# note it is the destination of that non-exhausted edge
		j = j + 1
	return unexplorededge

def traversegraph(m, size):
	pathsfound = []
	cyclesfound = []
	crtsegmentid = 0
	exhaustedsegments = set()
	nonexhaustednodes = set()
	# add the starting node
	nonexhaustednodes.add(0)
	# keep identifying new segments and path until there are no more nodes with
	# non-travelled edges
	iteration = 1
	while len(nonexhaustednodes) > 0:
		print('run: ' + str(iteration))
		print(nonexhaustednodes)
		crtsegmentid = crtsegmentid + 1
		curpath = set();
		done = False
		currow = 0		# always start from node 0
		lastedge = -1
		while not done:
			curpath.add(currow)
			zerocol = findzeroinrow(m, size, currow, nonexhaustednodes)
			print('findzeroinrow: ' + str(zerocol))
			if zerocol == -1:	
				# we did not find any unexplored edge
				# we will have to pick an edge which down the line has atleast
				# some part unexplored
				zerocol = findunexplorededge(m, size, currow, exhaustedsegments)
				if zerocol == -1:
					# we are done here, it is a dead end; we cannot go anywhere
					done = True
					# for the current node either there are any zeros nor any non-exhausted edges
					# we need to remove it from the nonexhausted node list
					nonexhaustednodes.remove(currow)
					print('removed ' + str(currow))
				else:
					if m[currow][zerocol] == lastedge and lastedge > -1:
						print ('actually we are done with this edge since it did not yield any zeros')
						exhaustedsegments.add(lastedge)
						done = True
					else:
						lastedge = m[currow][zerocol]
						print('findunexplorededge: ' + str(zerocol) + ' edge is: ' + str(lastedge))
						currow = zerocol
			else:
				# clear out any edge used since we did find zero
				lastedge = -1
				m[currow][zerocol] = crtsegmentid
				# are we at destination?
				if zerocol == size-1:
					# we have reached our destination, this the 'path'
					print('reached destination')
					pathsfound.append(curpath)
					##we are done here
					done = True
				else:
					if zerocol in curpath:
						# we got a cycle
						print('got cycle')
						curpath.add(zerocol)
						cyclesfound.append(curpath)
						done = True
					else:
						# we have to still to move forward
						print('keep moving')
						currow = zerocol
			iteration = iteration + 1
			if iteration == 25:
				print('going in the loop probably...')
				done = True
	print('found cycles:')
	print(cyclesfound)
	print('found paths:')
	print(pathsfound)


size = 3
# no edge from 0th element
m = [[-1, 0, -1], [-1, -1, 0], [-1, -1, -1]]
printmatrix(m, size)
traversegraph(m, size)

