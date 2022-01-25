# leetcode 543
# 14-43 이진 트리의 직경
# 이진 트리의 루트가 주어지면 트리 지름의 길이를 반환합니다.
# 이진 트리의 지름은 트리의 두 노드 사이에서 가장 긴 경로의 길이입니다.
# 이 경로는 루트를 통과할 수도 있고 통과하지 않을 수도 있습니다.
# 두 노드 사이의 경로 길이는 두 노드 사이의 모서리 수로 표시됩니다.

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    print('idx,len(lst)',idx,len(lst))
    print('lst: ',lst)

    if idx < len(lst):
        if lst[idx] is None:
            return
        parent = TreeNode(lst[idx])
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    # print('treenode: ',TreeNode(lst[idx]))
    # print('parent: ',parent.val)
    return parent

tree = [1, 2, 3, 4, 5]

make_tree_by(tree,1)

#  최하단 (parent.left = leaf) 노드에서 출발 >> parent노드로 간다.이때 parent까지의 cnt++ 저장
#                      >> parent.right의 right leaf까지 간다. // 다시 leaf 까지의 cnt 따로 저장.
#                      >> 재귀를 이용해서 이전 cnt와의 비교를 하면서 더 큰값을 계속 cnt에 갱신하며 반복
#   parent.val

# def longestPath(lst):
#     cnt=0
#     root = make_tree_by(lst, 0)
#
#     def dfs():
#
#         pass
#
# longestPath(tree)