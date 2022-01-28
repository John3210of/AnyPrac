# leetcode 617. 14-46 두 이진 트리의 병합
# 두 개의 이진 트리 root1과 root2가 제공됩니다.

# 그들 중 하나를 다른 하나를 덮기 위해 배치할 때 두 트리의 일부 노드는 겹치고 다른 노드는 겹치지 않는다고 상상해 보세요.
# 두 트리를 새로운 이진 트리로 병합해야 합니다. 병합 규칙은 두 노드가 겹치면 노드 값을 합산하여 병합된 노드의 새 값으로 합산하는 것입니다.
# 그렇지 않으면 NOT null 노드가 새 트리의 노드로 사용됩니다.
# 병합된 트리를 반환합니다.
# 참고: 병합 프로세스는 두 트리의 루트 노드에서 시작해야 합니다.

# 로직1) 재귀함수 (노드 val을 받는다. 양 노드를 더한다.)
#       왼쪽으로 가면서 재귀함수, 오른쪽으로 가면서 재귀함수
# 로직2) if node.val==0 이라면 ?

from collections import deque


class TreeNode:  # clear

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tr_lst1 = [1, 3, 2, 5, None, None, None]
tr_lst2 = [2, 1, 3, None, 4, None, 7]


def maketree(lst, idx):  # clear
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value == None:
            return
        parent = TreeNode(value)
        parent.left = maketree(lst, 2 * idx + 1)
        parent.right = maketree(lst, 2 * idx + 2)
    return parent


def mergetree(tr_lst1, tr_lst2):
    print(maketree(tr_lst1, 0).val)  # maketree 검증
    t1 = maketree(tr_lst1, 0)  # list를 tree로 바꿔줌
    t2 = maketree(tr_lst2, 0)  #

    def recur(t1, t2):  # tree 1과 2를 입력해서 시작
        if t1 and t2:  # 둘 다 value가 None이 아니라면
            node = TreeNode(t1.val + t2.val)
            node.left = recur(t1.left, t2.left)
            node.right = recur(t1.right, t2.right)
            return node
        else:
            return t1 or t2

    root = recur(t1, t2)
    # return node

    if len(tr_lst1) >= len(tr_lst2):
        length = len(tr_lst1)
    else:
        length = len(tr_lst2)  # clear

    ## tree형태의 node를 반환하고 다시 list 형태로 바꿔준다.
    return make_lst_by_bst(root, length - 1)


def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    print("tree > list", lst)

    return lst


mergetree(tr_lst1, tr_lst2)
