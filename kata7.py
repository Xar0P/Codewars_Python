# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# SUCESS

def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = []

    for letter in message:
        if letter in alphabet_upper:
            i = alphabet_upper.index(letter)
            position = (i + 13) - len(alphabet_upper)

            new_message.append(alphabet_upper[position])
        elif letter in alphabet:
            i = alphabet.index(letter)
            position = (i + 13) - len(alphabet)

            new_message.append(alphabet[position])
        else:
            new_message.append(letter)

    return "".join(new_message)


print(rot13("Uma frase bem grande pra fazer um teste bom: 10 + 15 = 98"))
