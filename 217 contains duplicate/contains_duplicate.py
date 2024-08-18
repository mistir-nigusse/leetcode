class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checked = set()
        for num in nums:
            if num in checked:
                return True  
            checked.add(num)
        return False  