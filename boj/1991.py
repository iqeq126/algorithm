import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)
input, print = sys.stdin.readline, sys.stdout.write
tree = defaultdict()
N = int(input())
root = 'A'
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

def preorder(node):
    print(node.value)
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])

def inorder(node):
    if node.left:
        inorder(tree[node.left])
    print(node.value)
    if node.right:
        inorder(tree[node.right])

def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    print(node.value)

for i in range(N):
    node = list(input().split())
    if node[0] == root:
        tree[root] = Node()
        tree[root].value = node[0]
        if node[1] != '.':
            tree[root].left = node[1]
            tree[node[1]] = Node()
            tree[node[1]].value = node[1]
        if node[2] != '.':
            tree[root].right = node[2]
            tree[node[2]] = Node()
            tree[node[2]].value = node[2]
    else:
        if node[1] != '.':
            tree[node[0]].left = node[1]
            tree[node[1]] = Node()
            tree[node[1]].value = node[1]
        if node[2] != '.':
            tree[node[0]].right = node[2]
            tree[node[2]] = Node()
            tree[node[2]].value = node[2]
preorder(tree[root])
print("\n")
inorder(tree[root])
print("\n")
postorder(tree[root])
