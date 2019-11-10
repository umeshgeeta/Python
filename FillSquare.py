# author: Umesh Patil
# November 9, 2019

# The populates cells of a given m by m matrix by numbers 0 to 9 in clockwise manner.

# Global variable to generate numbers to be placed in the matrix cell
num = 0;

# Generates the next number in the sequence, wraps at 10 and starts from 0 after 9.
def getnextnum():
  global num
  if num < 9:
    num = num + 1
  else:
    num = 0
  return num

# Creates a 2 dimensional array initialized to 0.
def matrix(size):
  # Creates a list containing size lists, each of size items, all set to 0
  w, h = size, size;
  matrix = [[0 for x in range(w)] for y in range(h)] 
  return matrix
  
 # Prints the matrix as m lines, each with m columns separated by a single space.
def printmatrix(m, size):
  for i in range(size):
    line = ''
    for j in range(size):
      line = line + str(m[i][j]) + ' '
    print(line)
    
# Fills the given submatrix in clockwise manner.
def fillsubmatrix(m, i, j, size):
  filled = 0
  startX = i
  startY = j
  limit = startY + size
  while j < limit:
    m[i][j] = getnextnum()
    j = j + 1
    filled = filled + 1
    
  j = j - 1
  i = i + 1
  limit = startX + size
  while i < limit:
    m[i][j] = getnextnum()
    i = i + 1
    filled = filled + 1
    
  i = i - 1
  j = j - 1
  limit = startY - 1
  while j > limit:
    m[i][j] = getnextnum()
    j = j - 1
    filled = filled + 1
  
  j = startY
  i = i - 1
  limit = startX
  while i > limit:
    m[i][j] = getnextnum()
    i = i - 1
    filled = filled + 1
    
  return filled
  
 # Populates the given matrix by numbers, invokes fill matrix on smaller and smaller
 # inner matries untill all cells are populated.
def populatematrix(m, size):
  expected  = size * size
  filled = 0
  i = 0
  j = 0
  s = size
  while filled < expected:
    f = fillsubmatrix(m, i, j, s)
    filled = filled + f
    i = i + 1
    j = j + 1
    s = s - 2

    
size = 7
m = matrix(size)
populatematrix(m, size)
printmatrix(m, size)
