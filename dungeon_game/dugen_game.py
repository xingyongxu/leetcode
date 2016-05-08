
def printd(l):
    pstr=''
    for i,v in enumerate(l):
        for j,k in enumerate(v):
           pstr += str(k) + '\t'
        pstr += '\n'
    print pstr

class Solution(object):

    def line_next_health(self, m_health, c_health, x):
        if c_health + x > 0:
            return m_health, c_health + x
        else:
            return m_health - (c_health + x) + 1, 1

    def next_health(self, up_min, left_min, up_crt, left_crt, x):
        d_min, d_crt = self.line_next_health(up_min, up_crt,x)
        r_min, r_crt = self.line_next_health(left_min,left_crt,x)
        if d_min < r_min:
            return d_min,d_crt
        elif d_min  == r_min:
            return (d_min,d_crt) if d_crt > r_crt else (r_min,r_crt)
        else:
            return r_min,r_crt

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        printd(dungeon)
        m, n = len(dungeon), len(dungeon[0])
        min_health = [[0 for x in range(n)] for y in range(m)]
        crt_health = [[0 for x in range(n)] for y in range(m)]

        min_health[0][0] = 1 if dungeon[0][0] > 0 else 1 - dungeon[0][0]
        crt_health[0][0] = min_health[0][0] + dungeon[0][0]
        for i in range(1,m):
            min_health[i][0],crt_health[i][0] = self.line_next_health(min_health[i-1][0],crt_health[i-1][0],dungeon[i][0])
        for i in range(1,n):
            min_health[0][i],crt_health[0][i] = self.line_next_health(min_health[0][i-1],crt_health[0][i-1],dungeon[0][i])

        for i in range(1,m):
            for j in range(1,n):
                min_health[i][j], crt_health[i][j] =\
                self.next_health(min_health[i-1][j],min_health[i][j-1],crt_health[i-1][j],crt_health[i][j-1],dungeon[i][j])

        printd(min_health)

        print '************'

        printd(crt_health)

        return min_health[-1][-1]

s = Solution()
dungeon = [
[-2,-3,3],
[-5,-10,1],
[10,30,-5]
]
dungeon = [[2,1],[1,-1]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]] 
#dungeon = [[-3,0,-3],[-3,-2,-3],[-3,0,1]]
s.calculateMinimumHP(dungeon)
