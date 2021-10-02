# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
# SUCCESS test ssh

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.letter_to_index = dict(zip(alphabet, range(len(alphabet))))
        self.index_to_letter = dict(zip(range(len(alphabet)), alphabet))


    def encode(self, message):
        encrypted = ''

        # transformar a mensagem para o tamanho da key
        split_message = [message[i:i + len(self.key)] for i in range(0, len(message), len(self.key))]

        # converter a mensagem
        for each_split in split_message:
            i = 0
            for letter in each_split:
                if not letter in self.alphabet:
                    encrypted += letter
                    i+=1
                else:
                    # (index da palavra + index da chave) % tamanho do alfabeto
                    number = (self.letter_to_index[letter] + self.letter_to_index[self.key[i]]) % len(self.alphabet)
                    # depois de pegar o index da letra, adiciona ela na mensagem final
                    encrypted += self.index_to_letter[number]
                    i+=1

        return encrypted

    def decode(self, message):
        if message.isupper():
            return message

        decrypted = ''

        # transformar a mensagem para o tamanho da key
        split_decrypted = [message[i:i + len(self.key)] for i in range(0, len(message), len(self.key))]

        # converter a mensagem
        for each_split in split_decrypted:
            i = 0
            for letter in each_split:
                if not letter in self.alphabet:
                    decrypted += letter
                    i+=1
                else:
                    # (index da palavra - index da chave) % tamanho do alfabeto
                    number = (self.letter_to_index[letter] - self.letter_to_index[self.key[i]]) % len(self.alphabet)
                    # depois de pegar o index da letra, adiciona ela na mensagem final
                    decrypted += self.index_to_letter[number]
                    i+=1

        return decrypted


v = VigenereCipher('password','abcdefghijklmnopqrstuvwxyz')

print(v.encode("it's a shift cipher!"))