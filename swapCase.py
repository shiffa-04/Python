def swap_case(s):
    newString =""
    for i in s:
        if i.isupper():
            newString += i.lower()
        elif i.islower():
            newString +=i.upper()
        else:
            newString += i
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)