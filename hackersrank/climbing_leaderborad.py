#!/bin/python3
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    answer=[]
    ranked=sorted((set(ranked)), reverse=True)
    idx=len(ranked)-1
    for p in player:
        while ranked[idx] <= p and idx >= 0:
            idx-=1
        if idx<0:
            answer.append(1)
        else:
            answer.append(idx+2)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
