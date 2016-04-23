import math
class Solution(object):
'''
for sigma Ai = M, if Ai == Aj for any i,j,  products got the extremum. but there're exceptions
2**3 < 3**2   and  3**4 > 4 ** 3, so need replace the partation.
'''
    def __init__(s):
        s.par = []
    def integerBreak(s, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 7:
            return n/2 * (n - n/2)
        for i in range(n/2,2,-1):
            if n  > math.ceil(1.*(i**i)/((i-1)**(i-1))):
                product,j = 1,i
                while j > 0:
                    product *= n/j
                    s.par.append(n/j)
                    n -= n/j
                    j -= 1
                rc2 = s.par.count(2) / 3
                rc3 = s.par.count(4) / 3
                if rc2 > 0 :
                    product = product * (9 ** rc2)  / (8 ** rc2)
                if rc3 > 0:
                    product = product * (81 **rc3) / (64 **rc3)
                return product


