"""
import sys

input = sys.stdin.readline
prin = sys.stdout.write

childl = [0 for _ in range(26)]
childr = [0 for _ in range(26)]


def preorder(idx):
    prin(chr(idx + A))
    if childl[idx] != ord('.') - A:
        preorder(childl[idx])
    if childr[idx] != ord('.') - A:
        preorder(childr[idx])


def inorder(idx):
    if childl[idx] != ord('.') - A:
        inorder(childl[idx])
    prin(chr(idx + A))
    if childr[idx] != ord('.') - A:
        inorder(childr[idx])


def postorder(idx):
    if childl[idx] != ord('.') - A:
        postorder(childl[idx])
    if childr[idx] != ord('.') - A:
        postorder(childr[idx])
    prin(chr(idx + A))


n = int(input())
A = ord('A')
for _ in range(n):
    a, b, c = input().split()
    childl[ord(a) - A] = ord(b) - A
    childr[ord(a) - A] = ord(c) - A

preorder(0)
print()
inorder(0)
print()
postorder(0)
"""
class Node:
    def __init__(self,item,left,right):
        self.item=item
        self.left=left
        self.right=right
def preorder(node):
    print(node.item,end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right !='.':
        preorder(tree[node.right])
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item,end='')
    if node.right != '.':
        inorder(tree[node.right])
def postorder(node):
    if node.left !='.':
        postorder(tree[node.left])
    if node.right!='.':
        postorder(tree[node.right])
    print(node.item,end='')
if __name__=="__main__":
    N=int(input())
    tree={}
    for _ in range(N):
        node,left,right=map(str,input().split())
        tree[node]=Node(item=node,left=left,right=right)
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])