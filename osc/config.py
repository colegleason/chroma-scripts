

"""
Right now, its an offset 6 by 8 grid.

       2         4         6
  1         3         5
       8(B)      10        12
  7         9         11
       14        16(X)     18(X)
  13        15        17 
       20        22        24
  19        21        23
       26        28        30
  25        27        29
       32        34        36
  31        33        35
       38        40        42
  37        39        41
       44        46        48
  43        45        47


 - or -

order = [
  0,   1,   2,   3,   4,   5,
  6,   7,   8,   9,   10,  11,
  12,  13,  14,  15,  16,  17,
  18,  19,  20,  21,  22,  23,
  24,  25,  26,  27,  28,  29,
  30,  31,  32,  33,  34,  35,
  36,  37,  38,  39,  40,  41,
  42,  43,  44,  45,  46,  47,
]
"""



order = [
  43,  36,  41,  45,  44,  47,
  38,  39,  42,  46,  37,  40,
  34,  35,  33,  32,  24,   0,
  20,  23,  21,  25,  18,  27,
  29,  17,  28,  26,  19,  30,
   6,  22,  16,  15,  10,  31,
   2,   4,   3,  12,  11,  13,
   7,   1,   5,   8,   9,  14,
]

def maplights(array):
	"""
	Given a list of n tuples in the form of (R,G,B), return a list of the same size,
	corresponding to how they're arranged on the ceiling.
	"""
	out = [(0,0,0)]*len(order)
	for i in range(len(order)):
	  try:
	    out[order[i]] = array[i]
	  except IndexError:
	    pass
	
	return out
	
