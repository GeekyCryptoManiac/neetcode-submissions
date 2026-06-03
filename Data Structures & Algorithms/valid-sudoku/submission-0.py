class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 sets for each group
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(81):
            r = i // 9        # integer division in Python
            c = i % 9
            box = (r // 3) * 3 + c // 3

            val = board[r][c]

            if val == '.':    # skip empties FIRST
                continue

            # check all 3 groups
            if val in rows[r]: return False
            if val in cols[c]: return False
            if val in boxes[box]: return False

            # no duplicate found, add to all 3 groups
            rows[r].add(val)
            cols[c].add(val)
            boxes[box].add(val)

        return True