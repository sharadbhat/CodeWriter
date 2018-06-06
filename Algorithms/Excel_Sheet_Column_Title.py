# LeetCode
# https://leetcode.com/problems/excel-sheet-column-title/description/

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        l = []
        while True:
            if (n % 26) == 0:
                l = ['Z'] + l
            else:
                l = [chr(64 + n % 26)] + l

            n = (n - 1) // 26

            if n == 0:
                break
        return ''.join(l)
