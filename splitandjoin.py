def split_and_join(line):
    spl_lis = line.split(" ")
    result ="-".join(spl_lis)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)