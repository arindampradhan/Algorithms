# Seive of erotosthenes
import math

class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        primes = [1] * (A+1)
        primes[0] = 0
        primes[1] = 0
        
        for i in range(2, math.ceil(math.sqrt(A))):
            j = 2
            while i*j <= A:
                primes[j*i] = 0
                j = j + 1
        
        ans = []
        for a,b in enumerate(primes):
            if b == 1:
                ans.append(a)

        return ans

