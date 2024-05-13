# https://www.acmicpc.net/problem/1991
# treenode 클래스로 구현하여 inorder,postorder,preorder 선언
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(tree):
    if tree is None:
        return
    print(tree.val,end='')  # 먼저 루트 노드를 출력
    preorder(tree.left)
    preorder(tree.right)

def inorder(tree):
    if tree is None:
        return
    inorder(tree.left)
    print(tree.val,end='') # 루트 노드를 출력
    inorder(tree.right)

def postorder(tree):
    if tree is None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.val,end='')  # 마지막으로 루트 노드를 출력

if __name__ == "__main__":
    n = int(input())
    nodes={}
    for _ in range(n):
        data, left, right = input().split()
        if data not in nodes:
            nodes[data] = TreeNode(data)
        if left != '.':
            if left not in nodes:
                nodes[left] = TreeNode(left)
            nodes[data].left=nodes[left]
        if right !='.':
            if right not in nodes:
                nodes[right] = TreeNode(right)
            nodes[data].right = nodes[right]
        
    root=nodes['A']
    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)