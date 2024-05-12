class Solution(object):
    def insertion_sort(self,arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge_and_sort(self,arr1, arr2):
        merged_array = arr1 + arr2  # Concatenate the two arrays
        self.insertion_sort(merged_array)  # Sort the merged array using insertion sort
        return merged_array 

    def findMedianSortedArrays(self, nums1, nums2):
        new_arr = self.merge_and_sort(nums1, nums2)
        if len(new_arr)%2 == 0:
            mid = len(new_arr) / 2
            median = (new_arr[mid] + new_arr[mid-1]) / 2.0
            return median
        else:
            mid = int(len(new_arr) / 2)
            median = new_arr[mid]
            return median
sol = Solution()
nums1 = [1,3]   
nums2 = [2]
median = sol.findMedianSortedArrays(nums1,nums2)
print(median)