from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        1. Initialize an empty stack `stack`.
        2. Create an array `result` of the same length as `nums`, filled with `-1`.
        3. Iterate over the array `nums` with index `i`:
            a. While `stack` is not empty and `nums[stack.top()] < nums[i]`:
                i. Pop the top index from `stack`.
                ii. Set `result[popped_index] = i - popped_index`.
            b. Push the current index `i` onto the `stack`.
        4. Return the `result` array.
        '''
        stack = deque()
        result = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result