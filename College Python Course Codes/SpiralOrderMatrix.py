class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        seen = set()
        res = []

        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        direction = 'right'
        while True:
            res.append(matrix[i][j])
            seen.add((i, j))

            if direction == 'right':
                j += 1
                if j == n or (i, j) in seen:
                    direction = 'down'
                    j -= 1
                    i += 1
                    if i == m or (i, j) in seen:
                        return res

            elif direction == 'down':
                i += 1
                if i == m or (i, j) in seen:
                    direction = 'left'
                    i -= 1
                    j -= 1
                    if j < 0 or (i, j) in seen:
                        return res

            elif direction == 'left':
                j -= 1
                if j < 0 or (i, j) in seen:
                    direction = 'up'
                    j += 1
                    i -= 1
                    if i == 0 or (i, j) in seen:
                        return res

            else:
                # direction == 'up':
                i -= 1
                if i < 0 or (i, j) in seen:
                    direction = 'right'
                    i += 1
                    j += 1
                    if j == n or (i, j) in seen:
                        return res