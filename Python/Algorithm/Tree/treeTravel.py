"""
BAEKJOON 1991번 트리 순회
https://www.acmicpc.net/problem/1991
"""
from collections import deque

import sys
input = sys.stdin.readline

tree = {}

n = int(input())
for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

preO = ''
inO = ''
postO = ''

def preorder(root):
    global preO
    preO += root
    
    if tree[root][0] != '.':
        preorder(tree[root][0])
    else: pass
    
    if tree[root][1] != '.':
        preorder(tree[root][1])
    else: return
    
def inorder(root):
    global inO
    
    if tree[root][0] != '.':
        inorder(tree[root][0])
    else: pass
    
    inO += root
    
    if tree[root][1] != '.':
        inorder(tree[root][1])
    else: return
    
def postorder(root):
    global postO
    
    if tree[root][0] != '.':
        postorder(tree[root][0])
    else: pass
    
    if tree[root][1] != '.':
        postorder(tree[root][1])
    else: pass
    
    postO += root
    return

preorder('A')
inorder('A')
postorder('A')

print(preO)
print(inO)
print(postO)
