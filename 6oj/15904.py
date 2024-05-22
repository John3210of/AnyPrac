# https://www.acmicpc.net/problem/15904
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solution():
    return 0

if __name__ == "__main__":
    '''
    완탐?
    '''
    words = list(map(str,input().split()))
    string='UCPC'
    spells=[]
    answer=''
    for word in words:
        spells.extend(list(word))
    idx=0
    for s in string:
        while idx<len(spells):
            if s==spells[idx]:
                idx+=1
                answer+=s
                break
            else:
                idx+=1
    if answer==string:
        print('I love UCPC')
    else:
        print('I hate UCPC')
            
            