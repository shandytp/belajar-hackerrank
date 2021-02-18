def print_func(n):
    for i in range(n):
        if i < 150:
            result = i + 1
            print(result, end='')
        else:
            break

print_func(15)