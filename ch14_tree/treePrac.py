# 이진트리의 높이가 log n 임을 알아야한다.

# level이 k일때 각level의 최대 원소의 갯수는 2^k 개.

#이때 높이가 level = h 라면

#등비급수 시그마 n=1 부터 2^n n->h
# N(갯수)  = 2^(h+1) -1 이다.

# 따라서 N+1=2^(h+1)
# => log2(N+1)=h+1
# => h = log2(N+1)-1

from collections import deque

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = deque([root])
    print('makelist+limit_before q: ', limit)

    while q:
        print('lst: ', lst)
        if len(lst) > limit:
            break
        print('q: ',q)
        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst