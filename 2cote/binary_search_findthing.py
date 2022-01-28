# 부품찾기 p197
# N=5, lst=[8,3,7,9,2]

# input 가게의 물건갯수 + 가게의 물건 제품번호
# input 찾을 물건 갯수 + 찾을 물건의 제품 번호

# find[0]~[M-1] 까지가 thing[0][N-1]에 있으면 yes yes no ....
class treenode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 어떻게 해야 빨리 찾을수 있을지..
# sort해서 midium값 기준으로 tree를 만들고 탐색한다.?
# for i in find > find[i] is in thing?
# 불균형트리일수도 있는데 고유번호라고 했으니 중복index가 없는 균형 트리로 풀자
#                     7
#                 2         8
#             3  null     9   null
#         null  null  NULL NULL

# 트리만들어
def maketree(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = treenode(lst[mid])
    node.left = maketree(lst[:mid])
    node.right = maketree(lst[mid + 1:])

    return node


# main 함수
def search(thing, find):
    # result=[] 원래 이렇게 하려고 했음.
    result = ['no'] * len(find)  # yes no를 넣을 list
    root = maketree(thing)

    def dfs(find, root):
        if not root:
            return
        for i in range(len(find)):
            if find[i] == root.val:
                print('find[i]: ', i, find[i])
                result[i] = 'yes'

            elif find[i] < root.val:
                dfs(find, root.left)
                # if not root.left: 이렇게 하려고 했는데 no가 너무많이나옴
                #     result.append('no')
            elif find[i] > root.val:
                dfs(find, root.right)

    dfs(find, root)
    print(result)
    return result


#                     7
#                 2         8
#             3  null     9   null
#         null null    null null
thing = [8, 3, 7, 9, 2]  # [2,3,7,8,9]
find = [5, 7, 9]
thing.sort()

search(thing, find)

###############################################
# class treenode:
#
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def maketree(lst):
#     if not lst:
#         return None
#
#     mid = len(lst) // 2
#
#     node = treenode(lst[mid])
#     node.left = maketree(lst[:mid])
#     node.right = maketree(lst[mid + 1:])
#
#     return node
#
#
# def search(thing, find):
#     result = ['no'] * len(find)
#     root = maketree(thing)
#
#     def dfs(find, root):
#         if not root:
#             return
#         for i in range(len(find)):
#             if find[i] == root.val:
#                 print('find[i]: ', i, find[i])
#                 result[i] = 'yes'
#             elif find[i] < root.val:
#                 dfs(find, root.left)
#             elif find[i] > root.val:
#                 dfs(find, root.right)
#
#     dfs(find, root)
#     print(result)
#     return result
#
#
# thing = [8, 3, 7, 9, 2]
# find = [5, 7, 9]
# thing.sort()
#
# search(thing, find)
