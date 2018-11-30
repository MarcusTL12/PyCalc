import math


def primes(n:int) -> list:
	factors = []
	if n < 0:
		factors.append(-1)
		factors.append(1)
		n *= -1
	
	more = False
	i = 2

	while i <= math.sqrt(n):
		while n % i == 0:
			if not more:
				factors.append(i)
				factors.append(1)
				more = True
			else:
				factors[-1] += 1
			n /= i
		more = False
		if i == 2:
			i += 1
		else:
			i += 2
	if n != 1:
		factors.append(int(n))
		factors.append(1)
	return factors if len(factors) != 0 else [1, 1]


def primes_to_string(p:list) -> str:
	ret = ''
	for i in range(int(len(p) / 2)):
		if p[2 * i] == -1:
			ret += '-'
		else:
			if len(ret) > 0 and ret != '-':
				ret += ' * '
			ret += str(p[2 * i]) + ('^' + str(p[2 * i + 1]) if p[2 * i + 1] > 1 else '')
	return ret
	
