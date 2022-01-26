from collections import deque

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(lst):   #2

    if not lst:

        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid + 1:])
    print('sorted_arrray_to_bst_node: ', node.val)

    return node


def test_sorted_array_to_bst(lst):      #1
    if not lst:
        return []
    root = sorted_array_to_bst(lst)     #return node
    print('test+sorted+array+to+bst/// root: ', root)
    print('list: ', lst)

    return make_lst_by_bst(root, len(lst))


def make_lst_by_bst(root, limit):       #3
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


lst = [-10, -3, 0, 5, 9]

test_sorted_array_to_bst(lst)

##############################################################################

# from ch14_tree.binarytree.prac import sorted_array_to_bst, make_lst_by_bst
#
#
# def test_sorted_array_to_bst(lst):
#     if not lst:
#         return []
#     root = sorted_array_to_bst(lst)
#     return make_lst_by_bst(root, len(lst))
#
#
#
# assert test_sorted_array_to_bst(lst=[-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5]
# assert test_sorted_array_to_bst(lst=[-10, -7, -3, -1, 0, 1, 4, 5, 7, 9]) == [1, -3, 7, -7, 0, 5, 9, -10, None, -1, None]
#########################################################
