def print_pattern(rows):
    curr_char = 'A'
    curr_num = 2

    for i in range(1, rows + 1):
        for j in range(i):
            if i % 2 == 0:
                print(curr_num, end=' ')
                curr_num += 1
            else:
                print(curr_char, end=' ')
                curr_char = chr(ord(curr_char) + 1)
        print()


num_rows = 5
print_pattern(num_rows)
