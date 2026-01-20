class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        import math
        max_p = int(math.sqrt(r)) + 1
        sieve = [True] * (max_p + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(max_p)) + 1):
            if sieve[i]:
                for j in range(i*i, max_p + 1, i):
                    sieve[j] = False
        cnt = 0
        for p in range(2, max_p + 1):
            if sieve[p] and l <= p*p <= r:
                cnt += 1
        return r - l + 1 - cnt