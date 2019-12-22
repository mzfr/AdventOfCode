from part1 import solution

with open('intcode.txt', 'r') as f:
        data = list(map(int, f.read().split(',')))

for i in range(100):
    for j in range(100):
        if solution(data, i, j) == 19690720:
            print('Second part answer: %s' % str(100 * i + j))
            break
