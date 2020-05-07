# author: Umesh Patil
# May 2020

# Problem: 	We are given a nearly sorted array of integers. Find the minimum 
#			number of deletions to obtain the largest possible sorted subsequence.
#
#			We essentially focus on finding the largest sorted subsequence 
#			and the deletion count is trivial; simply substract the length of the
#			found subsequence from the length of the given array.
#
# Source:	HackerRank
#			TBD - find the URL and add it here.
#
# Solution:	Basic idea is as we traverse the input array, we track possible
#			subsequences. For ever incominh number we try to find a subsequence
#			which is already largest so as we build on it. If the incoming number
#			is not on the top then we compare it with other subsequences as well
#			evaluate whether by breaking the largest (or for that matter any other)
#			subsequence can we get a longer subsequence by adding the incoming.
#
#			Primarily the solution is single pass, so time complexity is O(n) 
#			while it needs lot of space. Optimization needs to be done in terms of
#			how subsequences are 'tracked'. For example, if we are 'half-past'
#			the array; subsequences which are must smaller than the longer one can
#			be trimmed and so on.
#
# Assumptions:	All are positive integers and we are given 'ascending' order and
#			expected to return in ascending order.
#
# Implementation:	We have Subsequence class and SubsequenceDictory with the
#			tuple of (subsequence length, top value) as the key. For replicating,
#			we make a copy of the list up to a point and then append the incoming.
#			

class Subsequence:

	def __init__(self):
		self.ss = list()
		self.top = None

	def topval(self):
		return self.top

	def len(self):
		return len(self.ss)

	def add(self, ele):
		self.ss.append(ele)
		self.top = ele

	def where(self, middle):
		i = self.len() - 1
		while i > -1 and middle < self.ss[i]:
			i = i - 1
		return i+1

	def replicate(self, middle):
		rs = Subsequence()
		w = self.where(middle)
		if w > 0:
			rs.ss = self.ss[:]
			rs.ss = rs.ss[:w]
			rs.top = rs.ss[w-1]
		rs.add(middle)
		return rs

	def key(self):
		return (len(self.ss), self.top)

	def printss(self):
		print(str(self.ss) + ' key: ' + str(self.key()))


class SubsequenceDictionary:

	def __init__(self):
		self.ssd = dict()

	def find(self, incoming):
		foundkey = None
		foundkeylegth = 0
		keys = list(self.ssd)
		for k in keys:
			ss = self.ssd[k]
			#ss.printss()
			top = ss.topval()
			if incoming >= top:
				# it can go on this subsequence
				if k[0] > foundkeylegth:
					foundkeylegth = k[1]
					foundkey = k
				# else we ignore
			else:
				w = self.ssd[k].where(incoming)
				if w >= foundkeylegth:
					foundkeylegth = w
					foundkey = k
				# else we ignore
		return foundkey

	def place(self, incoming):
		fk = self.find(incoming)
		if fk == None:
			s = Subsequence()
			s.add(incoming)
			self.ssd[s.key()] = s
		else:
			s = self.ssd.get(fk)
			if incoming >= s.topval():
				s.add(incoming)
				# the subsequence is changed
				# we need to update the dictionary
				# we kick out the old key & it's subsequence
				# and set the new subsequence to new key
				self.ssd.pop(fk)
				self.ssd[s.key()] = s
			else:
				r = s.replicate(incoming)
				self.ssd[r.key()] = r

	def printsd(self):
		#print('keys: ' + str(self.ssd.keys()))
		keys = list(self.ssd)
		for k in keys:
			self.ssd[k].printss()

	def maxsubseqlength(self):
		maxl = 0
		keys = list(self.ssd)
		for k in keys:
			print(k)
			if k[0] > maxl:
				maxl = k[0]
		return maxl

if __name__ == '__main__':

	sd = SubsequenceDictionary()
	sd.printsd()

	ar = [1, 2, 8, 3, 4, 15, 5, 6, 7, 2, 12, 13, 9, 10, 11]
	arl = len(ar)
	for i in range(arl):
		sd.place(ar[i])
	sd.printsd()
	maxssl = sd.maxsubseqlength()
	print('maximum length subsequence: ' + str(maxssl))
	print ('minimum number of deletions to get largest sorted subsequence: ' + str(arl-maxssl))

	#Output seen is:
	#[1, 2, 3, 4, 5, 6, 7, 12, 13] key: (9, 13)
	#[1, 2, 2] key: (3, 2)
	#[1, 2, 3, 4, 5, 6, 7, 9, 10, 11] key: (10, 11)
	#[1, 2, 8, 15] key: (4, 15)
	#(9, 13)
	#(3, 2)
	#(10, 11)
	#(4, 15)
	#maximum length subsequence: 10
	#minimum number of deletions to get largest sorted subsequence: 5


