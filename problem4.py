import itertools

# Чтение числа n из файла input.txt
with open('input4.txt', 'r') as file:
    n = int(file.readline().strip())

# Генерация всех перестановок чисел от 1 до n
permutations = itertools.permutations(range(1, n + 1))

# Запись перестановок в файл output.txt
with open('output4.txt', 'w') as file:
    for perm in permutations:
        file.write(' '.join(map(str, perm)) + '\n')
