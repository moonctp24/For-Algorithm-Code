'''
Maximum Depth of Binary Tree
주어진 binary tree의 최대 깊이를 반환

0 <= 노드갯수 <= 10^4
'''
from collections import deque

def maxDepth(tree):    
    # visited = []
    maxD = 0
    
    if tree is None:
        return maxD
    
    q = deque()
    q.append((tree, 1))
    while q:
        cur_node, cur_d = q.popleft()
        # visited.append(cur_node)
        maxD = cur_d
        if cur_node.left:
            q.append((cur_node.left, cur_d + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_d + 1))
    return maxD

# tree = [3, 9, 20, None, None, 15, 7]

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v
root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))