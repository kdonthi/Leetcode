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
