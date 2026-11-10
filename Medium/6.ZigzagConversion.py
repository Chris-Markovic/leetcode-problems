#My solution O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        direction = 1
        if len(s) <= numRows:
            return s
        elif len(s) <= 1:
            return s
        elif numRows == 1:
            return s

        curr_row = 0
        for i in range(len(s)):
            rows[curr_row] += s[i]
            if curr_row == numRows-1:
                direction = -1
            elif curr_row == 0:
                direction = 1
            curr_row += direction
        final_string = ""
        for row in rows:
            final_string += row
        return final_string