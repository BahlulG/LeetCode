class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Turn lists into sets in order to delete duplicate values
        set1 = set(nums1)
        set2 = set(nums2)

        # Return a new set with elements common to the set1 and set2
        return (set2 & set1)