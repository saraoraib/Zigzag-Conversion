class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        k, direction = 0, 1

        for c in s:
            rows[k] += c
            if k == 0:
                direction = 1
            elif k == numRows - 1:
                direction = -1
            k += direction

        return ''.join(rows)