'''
Lowest Common Ancestor Of A Binary Tree
* leetcode 문제인데 트리구성을 플랫폼에서 자체적으로 해줘서 트리만들기, 호출 부분 없음

문제에서 Binary Tree 하나와 해당 트리에 속한 두 개의 노드가 주어진다. 이 때, 두 노드의 공통 조상중 가장 낮은 node 찾기

2 <= 노드개수 < 10^5
모든 노드 value는 유니크하다
p != q
모든 q, p는 노드에 있다.
'''
def findLCA(root, p, q): # postorder
    if root is None:
        return None
    if root is p or root is q:
        return root
    
    l = findLCA(root.left, p, q)
    r = findLCA(root.right, p, q)
    if root == l or root == r :
        return root
    elif l and r:
        return root
    return l or r

# findLCA([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4))