class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def checkMax(self, a, b, c):
        m = a

        if (m < b):
            m = b
        if (m < c):
            m = c
        return m

    def minimize(self, A, B, C):
        i, j, k = 0, 0, 0

        sol = 2 ** 31
        i_max = 2 ** 31

        while (i < len(A) or j < len(B) or k < len(C)):
            sol = min(sol, self.checkMax(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])))

            if (i + 1 < len(A)):
                temp1 = self.checkMax(abs(A[i + 1] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i + 1]))

            else:
                temp1 = i_max

            if (j + 1 < len(B)):
                temp2 = self.checkMax(abs(A[i] - B[j + 1]), abs(B[j + 1] - C[k]), abs(C[k] - A[i]))
            else:
                temp2 = i_max

            if (k + 1 < len(C)):
                temp3 = self.checkMax(abs(A[i] - B[j]), abs(B[j] - C[k + 1]), abs(C[k + 1] - A[i]))
            else:
                temp3 = i_max

            temp = min(temp1, temp2)
            temp = min(temp, temp3)

            if (temp == i_max):
                return sol
            elif (temp == temp1):
                i += 1

            elif (temp == temp2):
                j += 1

            else:
                k += 1


        return sol
