# w,h,b =map(int,input().split()) #def

n = int(input())  #개수를 입력받아 n에 정수로 저장
d = [[0 for col in range(19)] for row in range(19)]


for i in range(n):
  x,y = map(int,input().split())
  d[int(x-1)][int(y-1)]=1



# for i in range(n):



for i in range(19):
  for j in range(19):
    print(d[i][j],end=" ")
  print()




#
# d=[]        #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# for i in range(24):  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
#  d.append(0)#각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.
#
# for i in range(n):
# d[a[i]] += 1
# temp=a[0]
# for i in range(1,n):
# if temp<a[i]:
# temp=temp
# else:
# temp=a[i]
#
# print(temp)
#
#
#
#


