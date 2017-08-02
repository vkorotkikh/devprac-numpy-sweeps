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
import itertools
import numpy as np


def main():
	m_sieve()
	pres = rwh_primes2_python3(100)

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

def rwh_primes2_python3(n):
	izip = itertools.zip_longest
	chain = itertools.chain.from_iterable
	compress = itertools.compress
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    zero = bytearray([False])
    size = n//3 + (n % 6 == 2)
    sieve = bytearray([True]) * size
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        start = (k*k+4*k-2*k*(i&1))//3
        sieve[(k*k)//3::2*k]=zero*((size - (k*k)//3 - 1) // (2 * k) + 1)
        sieve[  start ::2*k]=zero*((size -   start  - 1) // (2 * k) + 1)
    ans = [2,3]
    poss = chain(izip(*[range(i, n, 6) for i in (1,5)]))
    ans.extend(compress(poss, sieve))
    return ans

if __name__ == "__main__":
	main()
