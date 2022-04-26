def solution(record):
    temp=[]
    answer = []
    dic={}
    for i in range(len(record)):
        temp.append(record[i].split())
        if len(temp[i])==3:
            dic[temp[i][1]]=temp[i][2]
    # print(temp)
    for i in temp:
        if i[0]=='Enter':
            answer.append(dic[i[1]]+"님이 들어왔습니다.")
        elif i[0]=='Leave':
            answer.append(dic[i[1]]+"님이 나갔습니다.")

    return answer

# a=4
# if a<3:
#     print('a')
# elif a==3:
#     print('b')
