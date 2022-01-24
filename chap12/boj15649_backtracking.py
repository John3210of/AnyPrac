# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# n,m=map(int,input('n,m: ').split())
#
# # 조건1)1~n까지 리스트를 만든다. // 원소가 m개여야 하는 조합을 리스트로 출력한다.
# num=[]
# result=[]
#
# for i in range(1,n+1):  # 조건1)1~n까지 리스트를 만들고
#     num.append(i)
#
# def dfs(result):        # result[0]= num[0],num[1],...,num[m-1]
#                         # result[1]= num[0],num[1],...,num[m-2],num[m-1]
#     for i in num:
#         if len(result)<m:
#             result.append(i)
#
#


# 조건2) 조합이 중복되어서는 안되고, 사전식 순서로 정렬하여 출력해야한다.
#
#

# def permutation(arr, r):
#     # 1.
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#     print('used: ',used)
#
#     def generate(chosen, used):
#         # 2.
#         print('chosen,used: ',chosen,used)
#         if len(chosen) == r:     # r = 2
#             print('return 전 chosen',chosen)
#             return
#
#         # 3.
#         for i in range(len(arr)): # len arr = 4
#             print('if not used[i]: ',used[i],i)
#             if not used[i]:
#                 print('used[i]: ',used[i])
#                 chosen.append(arr[i])
#                 print('chosen: ',chosen)
#                 used[i] = 1
#                 print('used 재귀전 : ')
#                 generate(chosen, used)
#                 used[i] = 0
#                 print('재귀후 pop할 chosen: ',chosen)
#                 chosen.pop()
#
#     generate([], used)
#


##################################
n,m=map(int,input().split())
# 조건1)1~n까지 리스트를 만든다. // 원소가 m개여야 하는 조합을 리스트로 출력한다.
num=[]
for i in range(1,n+1):  # 조건1)1~n까지 리스트를 만들고
    num.append(i)



n = len(num)
visited = [0] * n
arr = [0] * m
# result=[]


def permu(level):
    # 종료조건
    if level >= m:  # level==m이라고 해도 되지만 일반적으로 크게해주는게 좋다.
        for i in range(len(arr)):
            arr[i]=str(arr[i])
        result=' '.join(arr)
        print(result)
        return

    for i in range(n):
        if visited[i]==1:
            continue  # 사용됐다면 continue
        visited[i] = 1  # 사용중
        arr[level] = num[i]
        permu(level + 1)
        # arr[level] = 0  # level해제작업
        visited[i] = 0  # 사용해제

permu(0)
