def alphabet_position(letter):
    return "abcdefghijklmnopqrstuvwxyz".index(letter.lower())

def rotate_character(char, rot):
    if not(char.isalpha()):
        return char
    elif char.isupper():
        return "abcdefghijklmnopqrstuvwxyz"[(alphabet_position(char) + rot)%26].upper()
    else:
        return "abcdefghijklmnopqrstuvwxyz"[(alphabet_position(char) + rot )%26]

def encrypt(text, rot):
    #if text == '':
    #    return "You must provide a string to encrypt."
    if str(rot).isdigit():
        rot = int(rot)
    else:
        rot = 13
    return ''.join([rotate_character(c, rot) for c in text])
