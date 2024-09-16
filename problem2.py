# Чтение данных из input2.txt
with open('input2.txt', 'r') as file:
    # Считываем количество векторов и их размерность
    n, k = map(int, file.readline().split())

    # Считываем все векторы
    vectors = [tuple(map(int, file.readline().split())) for _ in range(n)]

# Сортировка векторов в лексикографическом порядке
vectors.sort()

# Запись отсортированных векторов в output.txt
with open('output2.txt', 'w') as file:
    for vector in vectors:
        file.write(' '.join(map(str, vector)) + '\n')
