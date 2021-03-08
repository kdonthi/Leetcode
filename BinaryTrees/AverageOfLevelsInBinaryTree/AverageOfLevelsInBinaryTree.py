# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    totalList = []
    numInLevel = []
    def recursiveFunc (self, root: TreeNode, level:int) -> List[float]:
        if root:
            if (len(self.totalList) < level + 1):
                self.totalList.append(root.val)
                self.numInLevel.append(1)
            else:
                self.totalList[level] += root.val
                self.numInLevel[level] += 1
            self.recursiveFunc(root.left, level + 1)
            self.recursiveFunc(root.right, level + 1)
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.totalList.clear()
        self.numInLevel.clear()
        self.recursiveFunc(root, 0) #call the root the "zeroth" level
        avgList = []
        for i,j in zip(self.totalList, self.numInLevel):
            avgList.append(i / j)
        return (avgList)
#Time Complexity is O(n) because we go through each value once to add its value to totalList
#Space Complexity is (O(N + log(n) + log(n)))
