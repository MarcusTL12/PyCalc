import sys
sys.path.append('./PyScr/')
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
import copy
import pfprint
import primefac
from scipy.special import comb as choose

_ = None

def ppprint(arg):
	global _
	pfprint.pfprint(arg)
	_ = arg

def frac():
	pfprint.frac = not pfprint.frac
	return _

def denom_lim(n):
	pfprint.denom_lim = n

def num_dec(n):
	pfprint.num_dec = n

def pltclr():
	plt.cla()
	plt.clf()
	plt.close()

def fact(n):
	return math.factorial(n)

def primesS(n):
	return primefac.primes_to_string(primefac.primes(n))

def primes(n):
	return primefac.primes(n)

sys.displayhook = ppprint

predef_globals = len(globals()) + 1
def loc():
	return dict(list(globals().items())[predef_globals:])
