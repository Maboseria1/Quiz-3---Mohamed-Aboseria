class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0 
        ones = 0
        twos = 0

        # check count
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        
        # build the array using the count 
        i = 0

        for _ in range(zeros):
            nums[i] = 0
            i += 1

        for _ in range(ones):
            nums[i] = 1
            i += 1

        for _ in range(twos):
            nums[i] = 2
            i += 1
