from fractions import Fraction
import numpy as np

a = [Fraction(22 / 7)]

for i in range(8, 1000000):
	frac = Fraction(np.pi).limit_denominator(i)
	if abs(float(a[-1]) - np.pi) > abs(float(frac) - np.pi):
		a.append(frac)

