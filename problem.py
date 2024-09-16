def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):  # l - количество рассматриваемых матриц
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def optimal_parenthesization(s, i, j):
    if i == j:
        return f"A{i + 1}"
    else:
        return f"({optimal_parenthesization(s, i, s[i][j])} x {optimal_parenthesization(s, s[i][j] + 1, j)})"

# Чтение входных данных
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    p = []
    for _ in range(n):
        rows, cols = map(int, file.readline().split())
        if not p:
            p.append(rows)
        p.append(cols)

# Вычисление минимального количества операций и оптимальной расстановки скобок
m, s = matrix_chain_order(p)
print(m)
print(s)
optimal_parens = optimal_parenthesization(s, 0, n - 1)

# Запись результата в выходной файл
with open('output.txt', 'w') as file:
    file.write(f"{m[0][n - 1]}\n")
    file.write(optimal_parens +'\n')
