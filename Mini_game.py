def minion_game(string):
    # your code goes here
    stuart_count = 0
    kevin_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = string.lower()
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_count += len(s) - i
        else:
            stuart_count += len(s) - i
    
    if kevin_count > stuart_count:
        print(f"Kevin {kevin_count}")
    elif stuart_count > kevin_count:
        print(f"Stuart {stuart_count}")
    else:
        print("Draw")
            

if __name__ == '__main__':
    s = input()
    minion_game(s)