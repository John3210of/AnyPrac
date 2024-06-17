import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solution(truth,parties):
    truth=set(truth)
    for _ in range(len(parties)):
        for party in parties:
            if set(party)&truth:
                    truth.update(set(party))
    count=0
    for party in parties:
        if not set(party)&truth:
            count+=1
    return count

if __name__ == "__main__":
    n,m=map(int,input().split())
    truth=list(map(int, input().split()))
    parties=[]
    for _ in range(m):
            party = list(map(int,input().split()))
            parties.append(party[1:])
    if len(truth)==1:
        print(m)
    else:
        truth=truth[1:]
        print(solution(truth,parties))