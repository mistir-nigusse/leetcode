class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSort(nums)
        return nums

    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2  
            left_half = nums[:mid]  
            right_half = nums[mid:]
            
            self.mergeSort(left_half)
            self.mergeSort(right_half)
            
            i = j = k = 0  
            
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1
            
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1
            
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1
