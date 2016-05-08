
def printd(l):
    pstr=''
    for i,v in enumerate(l):
        for j,k in enumerate(v):
           pstr += str(k) + '\t'
        pstr += '\n'
    print pstr

class Solution(object):

    def calUnidirectHealth(self, m_health, x):
        return max(1, m_health - x) 

    def calBidrectHealth(self, down_min, right_min, x):
        return min(self.calUnidirectHealth(down_min, x),self.calUnidirectHealth(right_min,x))

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        #printd(dungeon)
        m, n = len(dungeon), len(dungeon[0])
        min_health = [[0 for x in range(n)] for y in range(m)]
        min_health[-1][-1] = self.calUnidirectHealth(1,dungeon[-1][-1])

        for i in range(m - 2, -1, -1):
            min_health[i][-1] = self.calUnidirectHealth(min_health[i + 1][-1],dungeon[i][-1])
        for i in range(n - 2, -1, -1):
            min_health[-1][i] = self.calUnidirectHealth(min_health[-1][i + 1],dungeon[-1][i])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_health[i][j] =\
                self.calBidrectHealth(min_health[i + 1][j], min_health[i][j + 1], dungeon[i][j])

        #printd(min_health)
        return min_health[0][0]

s = Solution()
dungeon = [
[-2,-3,3],
[-5,-10,1],
[10,30,-5]
]
dungeon = [[2,1],[1,-1]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]] 
#dungeon = [[-3,0,-3],[-3,-2,-3],[-3,0,1]]
print s.calculateMinimumHP(dungeon)
