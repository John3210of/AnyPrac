class Solution:

    candidates=[2,3,6,7]
    target=7

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum,index,path):
            # dfs(5,0,[2])
            if csum<0:
                return
            if csum==0:
                result.append(path)
                return
            for i in range(index,len(candidates)): # (0,4)
                # cum = 7 // index =0 , path=[]
                dfs(csum-candidates[i],i,path+[candidates[i]])

                        # 5  ,0,[]+[2]=[2,2,3]



        dfs(target,0,[])

        return result

candidates=[2,3,6,7]
target=7

def combinationSum(candidates, target):
    results = []

    # at each iteration we will update the list of targets
    targets = [[target]]

    while targets:
        next_targets = []
        for cur_sequence in targets:
            cur_target = cur_sequence[0]
            for candidate in candidates:
                # to avoid duplicates we only add the candidate sequences in ascending order
                if (len(cur_sequence) == 1 or cur_sequence[1] >= candidate):
                    if candidate < cur_target:
                        next_targets.append([cur_target - candidate, candidate] + list(cur_sequence[1:]))
                    elif candidate == cur_target:
                        results.append(cur_sequence)
        targets = next_targets
        print('targets: ',targets)
        print('================')
        print('result',results)

    return

if __name__ == "__main__":
    print(combinationSum(candidates,target))
