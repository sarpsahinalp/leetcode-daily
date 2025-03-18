class Solution:
    def longestNiceSubarray(self, nums) -> int:
        res = 1
        currentWindow = [nums[0]]

        cur = 1
        for i in range(1, len(nums)):
            lastMarked = -1
            for index in range(len(currentWindow)):
                if currentWindow[index] & nums[i] != 0:
                    lastMarked = index

            if lastMarked == -1:
                currentWindow.append(nums[i])
                cur += 1
            else:
                currentWindow = currentWindow[lastMarked+1:]
                currentWindow.append(nums[i])
                cur = len(currentWindow)
                print(currentWindow)
            
            res = max(res, cur)
        
        return res