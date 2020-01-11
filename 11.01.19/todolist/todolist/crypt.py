def cryptChar(char):
    new_char = chr(ord(char)-3)
    if new_char < 'A':
        return chr(ord(new_char) + 26)
    return new_char


def cryptText(text):
    new_text = ""
    for c in text:
        if 'A' <= c <= 'Z':
            new_text += cryptChar(c)
        else:
            new_text += c
    return new_text