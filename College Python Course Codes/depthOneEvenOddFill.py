def outer(mat):
    n = 0

    def inner(matX):
        nonlocal n
        if (len(matX)) % 2 == 0:

            n = 0
            filler(n, matX)

        else:

            n = 1
            filler(n, matX)

    inner(mat)


def filler(n, mat):
    m = 0
    while m < len(mat):
        count = 0
        a = m + 1

        while count < a:
            mat[m].append(n)
            n += 2
            count += 1
        m += 1


mat_1 = [[], [], [], []]
mat_2 = [[], [], []]
outer(mat_1)
outer(mat_2)
print(mat_1)
print(mat_2)