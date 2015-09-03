'''
请找出无向图中相连要素的个数。
图中的每个节点包含其邻居的 1 个标签和 1 个列表。（一个无向图的相连节点（或节点）是一个子图，其中任意两个顶点通过路径相连，且不与超级图中的其它顶点相连。）

思路：建立一个result数组用来存放结果，对于访问过的节点用set()函数来存放（因为节点带有信息，存入数组后续判断不灵活，所以采用set()）,对图的每个节点进行遍历，对每一个节点对其邻居节点进行递归循环，将这些相连的节点放入同一个数组，再将这些子结果加入最终的结果中。
'''


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
            results = []
            visited = set()
            for node in nodes:
                if node not in visited:
                    result = []
                    self.bfs(node, result, visited)
                    result.sort()
                    results.append(result)
            return results
            
    def bfs(self, node, result, visited):
        visited.add(node)
        result.append(node.label)
        for i in node.neighbors:
            if i not in visited:
                self.bfs(i, result, visited)
