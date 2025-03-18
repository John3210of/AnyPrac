class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        '''
        [1,1,0], [0,1,1] 100
        [1,0,1], [1,0,1] 010
        [0,0,0]  [0,0,0] 111
        
        y축 대칭이동후, 뒤집기
        '''
        horizontal_image = []
        for im in image:
            horizontal_image.append(([int(not x) for x in im[::-1]])) 
        return horizontal_image
 
 # 시간복잡도, 공간복잡도 O(n*m) 