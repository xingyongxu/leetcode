# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

def parse(nested_list, rc):
    for e in nested_list:
        if e.isInteger():
            rc.append(e.getInteger())
        else:
            parse(e.getList(),rc)

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.rc = []
        parse(nestedList,self.rc)
        self.it = iter(self.rc)
        self.nt = 0

    def next(self):
        """
        :rtype: int
        """
        return self.nt

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.nt = self.it.next()
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
