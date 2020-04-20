class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # it's like binary search, except there are more comparisons
        def _binary_search(left=0, right=len(nums)-1):
            if left > right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= target and target <= nums[mid]:
            # normal binary search
                return _binary_search(left, mid-1)
            elif nums[left] > nums[mid] and nums[left] <= target and nums[right] <= target :
            # rise and dip on left side, if it's rising
                return _binary_search(left, mid-1)
            elif nums[left] > nums[mid] and target <= nums[mid] and nums[right] >= target:
                return _binary_search(left, mid-1)
            else:
                return _binary_search(mid+1,right)
            
        return _binary_search()
        