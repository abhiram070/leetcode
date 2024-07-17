class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        def is_common_prefix(length):
            prefix = strs[0][:length]
            for string in strs:
                if not string.startswith(prefix):
                    return False
            return True

        min_length = min(len(s) for s in strs)
        low, high = 0, min_length

        while low <= high:
            mid = (low + high) // 2
            if is_common_prefix(mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][: (low + high) // 2]
