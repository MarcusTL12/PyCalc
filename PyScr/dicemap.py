a = [[[str(i + 1) + str(j + 1) + 2 * str(k + 1) if (i != j and i != k and j != k) else '    ' for k in range(6)] for j in range(6)] for i in range(6)]

b = [[[[str(i + 1) + str(j + 1) + str(k + 1) + str(l + 1) if (i != j and i != k and i != l and j != k and j != l and k != l) else '    ' for l in range(6)] for k in range(6)] for j in range(6)] for i in range(6)]
