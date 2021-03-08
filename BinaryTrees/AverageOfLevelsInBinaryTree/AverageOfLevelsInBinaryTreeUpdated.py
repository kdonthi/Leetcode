class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        listOfNodes = []
        currLevel = [root]
        while currLevel:
            listOfNodes.append(currLevel) #appended the previous level
            currLevel = []
            for node in listOfNodes[len(listOfNodes) - 1]:
                if node.right:
                    currLevel.append(node.right)
                if node.left:
                    currLevel.append(node.left)
        for i in range(len(listOfNodes)):
            avg = 0
            for j in listOfNodes[i]:
                avg += j.val
            avg /= len(listOfNodes[i])
            listOfNodes[i] = avg
        return (listOfNodes)

# Time Complexity is O(2N) or O(N) because we go through each node twice, once to get their values and once to get their averages
# Space Complexity is the size of the subtree of each node * the number of nodes which is O(N^2)
