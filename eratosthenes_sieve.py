# ******************************************************************************
#
# Name:    Sieve of Eratosthenes
# Author:  Vadim Korotkikh
# Email:   va.korotki@gmail.com
# Date:    January 2017
# Version: 1.0
# Description: Find prime numbers
#
# ******************************************************************************
# Begin Imports
import math
import numpy as np


def main():
	m_sieve()


def m_sieve():
	is_prime 		= np.ones((100,), dtype=bool)
	is_prime[:2] 	= 0
	n_max	= int(np.sqrt(len(is_prime)))

	for j in range(2, n_max):
		is_prime[2*j::j] = False
	# np.nonzero(a) - Returns a tuple of arrays, one for each dim in a,
	# containing the indices of nonzero elements in each dimension
	primes	= np.nonzero(is_prime)
	for i in range(0, len(primes)):
		print(primes[i])


if __name__ == "__main__":
	main()
