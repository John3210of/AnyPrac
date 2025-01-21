class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        순회하다가 값이 튀어야 하는곳이 나온다면
         1 2 3 1 2 1
        [1 2 3 2 2 1]

         1 2 1 1 1 1 1
         1 2 3 1 1 1 1
         1 2 3 4 1 1 1
         1 2 3 4 2 1 1
         1 2 3 4 2 2 1 << 여기가 문제가 됨
        [1 2 3 4 3 2 1]

         1 2 1 1 1 1 1 : 2
         1 2 3 1 1 1 1 : 3
         1 2 3 1 1 1 1 : 
         1 2 3 1 2 1 1 : 
         1 2 3 1 2 1 1 : 
         1 2 3 1 2 1 1 : 
        [1 2 3 1 3 2 1]
        >>로 순회한다면 값이 커지고 난후 <<로 가면서 갱신시켜줘야함

        0. candies = [1] * len(ratings) 리스트를 초기화
        1. 리스트를 버블 형태로 순회한다.
            만약 앞뒤보다 큰 수라면, max(index-1,index+1)+1 을 한다.
            만약 앞보다 큰 수라면, candies[index] = [index-1] + 1 을 해주고 순회를 이어나간다.
            만약 뒤보다 큰 수라면, candies[index] = [index+1] + 1 을 하고, 역방향으로 순회를 시켜 
            값을 갱신해나가다가 [index-k] 쪽이 더 작아지거나, 크면서 candies도 크다면 종료한다.
        
        흠 굳이 그럴필요 있나 그냥 >> 갔다가 << 가면 될것 같은데
        '''
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
