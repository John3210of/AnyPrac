import sys
input = sys.stdin.readline

if __name__ == "__main__":

    n, m = map(int, input().split())
    poketmon={}
    poketmon_reverse={}
    
    for i in range(1,n+1):
        name=input().strip()
        poketmon[i] = name
        poketmon_reverse[name]=i
    quizs=[]
    for _ in range(m):
        quiz = input().strip()
        try:
            quiz = int(quiz)
        except:
            pass
        quizs.append(quiz)
    
    for quiz in quizs:
        if type(quiz)==int:
            print(poketmon[quiz])
        else:
            print(poketmon_reverse[quiz])