def solution(data, first=12, second=2):
    #Make copy of the data
    data = data[::]

    data[1] = first
    data[2] = second

    i = 0
    while i < len((data)):
        if data[i] == 99:
            break  # break if values is 99

        elif data[i] in [1, 2]:
            first_pos = data[i + 1]
            second_pos = data[i + 2]
            result_pos = data[i + 3]

            if data[i] == 1:
                data[result_pos] = data[first_pos] + data[second_pos]
            elif data[i] == 2:
                data[result_pos] = data[first_pos] * data[second_pos]

            i += 4 # We processed first 4 values so we jump those positions
            continue # Continue execution
        i += 1
    return data[0]


if __name__ == '__main__':
    result = 0

    with open('intcode.txt', 'r') as f:
        data = list(map(int, f.read().split(',')))

    print('Answer: %s' % solution(data))
