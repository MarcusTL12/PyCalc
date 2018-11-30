import numpy as np
import copy
from pprint import pprint
from fractions import Fraction

frac = True
denom_lim = 100000
num_dec = 12


def toFrac(arg):
	return Fraction(arg).limit_denominator(denom_lim)


def chkFrac(fra, arg):
	return abs(float(fra) - arg) < 10**(-14)


def floatformat(arg):
	if frac:
		fra = toFrac(arg)
		if chkFrac(fra, arg):
			return str(fra)
		narg = arg / np.pi
		fra = toFrac(narg)
		if chkFrac(fra, narg):
			return str(fra) + ' π'
		narg = arg / np.exp(1)
		fra = toFrac(narg)
		if chkFrac(fra, narg):
			return str(fra) + ' e'
		narg = arg**2
		fra = toFrac(narg)
		if chkFrac(float(fra), narg):
			return '√( ' + str(fra) + ' )'
	return round(arg, num_dec)


def listformat(arg, prevpoints=[]):
	prevpoints = copy.copy(prevpoints)
	isnparray = isinstance(arg, np.ndarray)
	if isnparray:
		arg = list(np.asarray(arg))
	if isinstance(arg, (list, tuple, dict)):
		prevpoints.append(arg)
		istup = isinstance(arg, tuple)
		isdict = isinstance(arg, dict)
		ret = list(arg.items()) if isdict else list(copy.copy(arg))
		if isdict:
			arg = list(arg.items())
		for i in range(len(arg)):
			seen_before = False
			for j in prevpoints:
				if id(arg[i]) == id(j):
					ret[i] = '[...]'
					seen_before = True
					break
			if not seen_before:
				if isinstance(arg[i], float):
					ret[i] = floatformat(arg[i])
				elif isinstance(arg[i], (list, tuple, np.ndarray)):
					ret[i] = listformat(arg[i], prevpoints)
		if isnparray:
			return np.array(ret)
		elif istup:
			return tuple(ret)
		elif isdict:
			return dict(ret)
		else:
			return ret
	return arg


def pfprint(arg):
	if isinstance(arg, float):
		print(floatformat(arg))
	elif isinstance(arg, (list, tuple, dict, np.ndarray)):
		data = listformat(arg, [])
		if isinstance(arg, np.ndarray):
			print(data)
		else:
			pprint(data)
	else:
		pprint(arg)
		