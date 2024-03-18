import textwrap

def wrap(string, max_width):
    finalString = ""
    tempString = ""
    for i in string:
        tempString +=i
        if len(tempString) == max_width:
            finalString += tempString +'\n'
            tempString = ""
    if tempString:
        finalString += tempString
    return finalString
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)