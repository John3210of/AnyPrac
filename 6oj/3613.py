# https://www.acmicpc.net/problem/3613

import sys
input = sys.stdin.readline
def is_java(name):
    if name[0].isupper():
        return False
    if '_' in name:
        return False
    return True

def is_cpp(name):
    if name[0] == '_' or name[-1] == '_':
        return False
    # if '__' in name:
    #     return False
    for i in range(len(name) - 1):
        if name[i] == '_' and name[i + 1] == '_':
            return False
    if any(c.isupper() for c in name):
        return False
    return True

if __name__ == "__main__":
    name = list(input().strip())
    result=''
    if is_cpp(name):
        for i in range(len(name)):
            if name[i]=='_':
                name[i+1]=name[i+1].upper()
            else:
                result+=name[i]
    elif is_java(name):
        for i in range(len(name)):
            if name[i].isupper():
                name[i]=name[i].lower()
                result+='_'
            result+=name[i]
    else:
        result='Error!'
    print(result)

