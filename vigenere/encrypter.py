__author__ = 'Aface'

import statistics

class VigenereSquare(): #Класс представляет квадрат виженера
    def __init__(self, alphabet, is_shuffle=False):
        self.square = []
        from copy import copy
        current_alphabet = copy(alphabet)
        if is_shuffle:
            from random import shuffle
            shuffle(current_alphabet)
        self.square.append(current_alphabet)
        for i in range(1, len(current_alphabet)):
            current_alphabet = copy(current_alphabet)
            self.square.append(self.shift(current_alphabet))


    @staticmethod
    def shift(l):
        t = l[0]
        for i in range(len(l) - 1):
            l[i] = l[i + 1]
        l[len(l) - 1] = t
        return l

    def __str__(self):
        result = ""
        for alphabet in self.square:
            for c in alphabet:
                result += c + ' '
            result += '\n'
        return result

    def __getitem__(self, c):
        i, j = c
        index = self.square[0].index(j)
        index2 = self.square[index].index(i)
        return self.square[0][index2]


class VigenereEncrypter(): #Шифрование текста
    def __init__(self):
        self.alphabet = statistics.english_alphabet
        self.square = VigenereSquare(self.alphabet, False)
        self.key_index = 0

    def encrypt(self, text, key):
        encrypted_text = ""
        for i in range(len(text)):
            if text[i] in self.alphabet:
                encrypted_text += self.square[key[self.key_index % len(key)], text[i]]
            else:
                encrypted_text += text[i]
            self.key_index += 1
        return encrypted_text




if __name__ == '__main__':
    filename = "king"
    vc = VigenereEncrypter()
    input_f = open(filename + '.txt', 'r')
    output_f = open('_' + filename + '.txt', 'w')
    input_f2 = open('_' + filename + '.txt', 'r')
    output_f2 = open('__' + filename + '.txt', 'w')

    for line in input_f:
        output_f.write(vc.encrypt(line, "asdf"))
    vc.key_index = 0
    #for line in input_f2:
        #output_f2.write(vc.encrypt(line, "qwer"))
    print(vc.square)
    s = vc.encrypt("ab cd", "bf")
    vc.key_index = 0
    print(s)
    print(vc.encrypt(s, "bf"))