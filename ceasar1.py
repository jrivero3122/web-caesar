from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    NewList = []
    for x in text:
        #print(x)
        NewList.append(rotate_character(x,rot))
    return ''.join(NewList)

#print(encrypt('Hello, World!',5))