# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AY2hmhc6cSsDFATh&categoryId=
# AY2hmhc6cSsDFATh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1 소수그래프
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_complete_graph(n):
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph[i].append(j)
            graph[j].append(i)
    return graph

def get_total_neighbors(graph):
    return sum(len(neighbors) for neighbors in graph.values())

def remove_edges_to_prime_sum(graph):
    count=0
    final_graph=[]
    while count < (n*(n-3))//2:
        removed = False
        is_all_prime = all(is_prime(len(neighbors)) for neighbors in graph.values())
        total_neighbors = get_total_neighbors(graph)//2
        if is_prime(total_neighbors) and is_all_prime:
            final_graph = {vertex: neighbors[:] for vertex, neighbors in graph.items()}
            return final_graph
        for vertex, neighbors in graph.items():
            if removed:
                break
            for neighbor in neighbors[:]:
                if len(graph[vertex]) > 2 and len(graph[neighbor]) > 2:
                    graph[vertex].remove(neighbor)
                    graph[neighbor].remove(vertex)
                    removed = True
                    break
        count+=1
    return final_graph

def convert_to_undirected_graph(graph):
    undirected_graph = {}
    for vertex, neighbors in graph.items():
        undirected_graph[vertex] = []
        for neighbor in neighbors:
            if neighbor > vertex:
                undirected_graph[vertex].append(neighbor)
    return undirected_graph

input_data = []
t = int(input())
for _ in range(t):
    n = int(input())
    input_data.append(n)
output_data = []
for n in input_data:
    complete_graph = generate_complete_graph(n)
    a = remove_edges_to_prime_sum(complete_graph)
    b = convert_to_undirected_graph(a)
    c = get_total_neighbors(b)
    output_data.append((b, c))
for b, c in output_data:
    print(c)
    for k,v in b.items():
        for i in v:
            print(f'{k} {i}')


# # 테스트
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     complete_graph = generate_complete_graph(n)
#     a=remove_edges_to_prime_sum(complete_graph)
#     b=convert_to_undirected_graph(a)
#     print(get_total_neighbors(b))
#     for k,v in b.items():
#         for i in v:
#             print(f'{k} {i}')
