if __name__ == '__main__':
    s = input()
    
    alphanumeric = [True for i in s  if i.isalnum()]
    if True in alphanumeric:
        print(True)
    else:
        print(False)
        
    alphabetical = [True for i in s  if i.isalpha()] 
    if True in alphabetical:
        print(True)
    else:
        print(False)    
    
    digit = [True for i in s  if i.isdigit()]
    if True in digit:
        print(True)
    else:
        print(False)    
    
    lowercase = [True for i in s  if i.islower()]
    if True in lowercase:
        print(True)
    else:
        print(False)
        
    uppercase = [True for i in s  if i.isupper()]
    if True in uppercase:
        print(True)
    else:
        print(False)
