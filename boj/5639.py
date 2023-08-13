"""import sys
sys.setrecursionlimit(10 ** 9)
input, print = sys.stdin.readline, sys.stdout.write
class Node:
    def __init__(self, N=None):
        self.data = N
        self.left = self.right = None

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self.data != None:
            print(str(self.data) + "\n")

    def insert(self, N):
        if self.data == None:
            self.data = N
        else:
            if self.data < N:
                if self.right == None:
                    self.right = Node(N)
                else:
                    self.right.insert(N)
            else:
                if self.left == None:
                    self.left = Node(N)
                else:
                    self.left.insert(N)
node = Node()
while True:
    try:
        N =int(input())
        node.insert(N)
    except:
        break
node.postorder()"""
import sys
print, input = sys.stdout.write, sys.stdin.readline
sys.setrecursionlimit(int(1e8))
tree = []
def postorder(s, e):
    if s > e:
        return
    root = tree[s]
    idx = s + 1

    while idx <= e:
        if tree[idx] > root:
            break
        idx += 1

    postorder(s + 1, idx - 1)
    postorder(idx, e)
    if root:
        print(str(root) + "\n")

while True:
    try:
        N = int(input())
        tree.append(N)
    except:
        break
postorder(0, len(tree) - 1)