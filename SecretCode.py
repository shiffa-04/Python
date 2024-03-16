
#//////////////Encryption?////////////////////
import string
import random


message = input("Enter Message: ")

#///////////////encoding//////////////////
if len(message) < 3:
    finalString = " "
    for i in range(len(message)-1,-1,-1):
        finalString = finalString + message[i]
    print(finalString)
elif len(message) >=3:
     msgList = list(message)
     firstLetter = msgList.pop(0)
     msgList.append(firstLetter)
     for i in range(3):
         randomLetter1 = random.choice(string.ascii_letters)
         msgList.append(randomLetter1)

         randomLetter2 = random.choice(string.ascii_letters)
         msgList.insert(i,randomLetter2)
     finalString =""
     for i in msgList:
        finalString = finalString + i
     print(finalString)

decoding = input("want to decode the message, Enter encrypted message : ")
# if decoding =="Y":

if len(decoding) < 3:
    result = " "
    for i in range(len(decoding)-1,-1,-1):
        result = result + decoding[i]
    print(result)
elif len(decoding) >= 3:
    msgList = list(decoding)
    # firstLetter = msgList.pop(0)
    # msgList.append(firstLetter)
    for i in range(3):
       msgList.pop(0)
       msgList.pop()
    lastLetter = msgList.pop()
    msgList.insert(0,lastLetter)

    finalString =""
    for i in msgList:
        finalString = finalString + i
    print(finalString)
