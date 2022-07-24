import string
from collections import OrderedDict


class Cipher:
    """ Implement The Keyword encoding and decoding for latin alphabet.
        The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
        Add the provided keyword at the begining of the alphabet.
        A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
        Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching
        to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order,
        excluding those already used in the key.
    """

    all_alphabets = list(string.ascii_uppercase)

    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.encrypting = list(OrderedDict.fromkeys(list(self.keyword) + self.all_alphabets))

    def encode(self, msg):
        encoding_text = ''
        for i in range(len(msg)):
            if msg[i] != ' ':
                encoding_text = encoding_text + self.encrypting[self.all_alphabets.index(msg[i].upper())]
            else:
                encoding_text = encoding_text + ' '
        print(encoding_text)

    def decode(self, msg):
        decoding_text = ''
        for i in range(len(msg)):
            if msg[i] != ' ':
                decoding_text = decoding_text + self.all_alphabets[self.encrypting.index(msg[i].upper())]
            else:
                decoding_text = decoding_text + ' '
        print(decoding_text)


if __name__ == '__main__':
    cipher = Cipher("crypto")
    cipher.encode("Hello world")
    cipher.decode("Fjedhc dn atidsn")
