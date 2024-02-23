'''
DFS 기본 알고리즘
'''
def traversal(root):
	if root is None:
		return
	traversal(root.left)
	traversal(root.right)
 
# preorder
def preorder(root):
	if root is None:
		return
	print(root)
	preorder(root.left)
	preorder(root.right)

# inorder
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)

# postorder
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root)