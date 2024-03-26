class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid rows
        for i in range(9):
            count = Counter(board[i])
            if len(count) == 1:
                continue
            if sorted(count.values())[-2] > 1:
                print('row')
                return False

        for i in range(9):
            ls = []
            for j in range(9):
                ls.append(board[j][i])
            count = Counter(ls)
            if len(count) == 1:
                continue
            if sorted(count.values())[-2] > 1:
                # print(count.values()[1])
                print('column ', i)
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                ls = []
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        ls.append(board[m][n])
                count = Counter(ls)
                if len(count) == 1:
                    continue
                if sorted(count.values())[-2]> 1:
                    print('box')
                    return False

        return True
        