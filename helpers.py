alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabet_position(letter):
    if letter.lower() in alphabet:
        letter = letter.lower()
        for x in range(len(alphabet)):
            if alphabet[x]==letter:
                return int(x)
    else:
        return -1

def rotate_character(char, rot):
    if alphabet_position(char)>=0:
        NewLetter_position = alphabet_position(char) + rot
        if NewLetter_position > 25:
            while NewLetter_position > 25:
                NewLetter_position = NewLetter_position - 26
            NewLetter = alphabet[NewLetter_position]
        if NewLetter_position <= 25:
            NewLetter = alphabet[NewLetter_position]
        if char == char.upper():
            NewLetter = alphabet[NewLetter_position].upper()
        return NewLetter
    else:
        return char