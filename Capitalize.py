def solve(s):
    result = ""
    newWord = True

    for char in s:
        if newWord and char.isalpha():
            result += char.upper()
            newWord = False
        else:
            result += char
            
        if char == " ":
            newWord = True
        else:
            newWord = False
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()