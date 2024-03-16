def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):

        decimal_num = str(i).rjust(width)

        octal_num = oct(i)[2:].rjust(width)

        hexadecimal_num = hex(i)[2:].upper().rjust(width)

        binary_num = bin(i)[2:].rjust(width)


        print(f"{decimal_num} {octal_num} {hexadecimal_num} {binary_num}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)