frequency_english = {'a': 8.167,
                     'b': 1.492,
                     'c': 2.782,
                     'd': 4.253,
                     'e': 12.702,
                     'f': 2.228,
                     'g': 2.015,
                     'h': 6.094,
                     'i': 6.966,
                     'j': 0.153,
                     'k': 0.772,
                     'l': 4.025,
                     'm': 2.406,
                     'n': 6.749,
                     'o': 7.507,
                     'p': 1.929,
                     'q': 0.095,
                     'r': 5.987,
                     's': 6.327,
                     't': 9.056,
                     'u': 2.758,
                     'v': 0.978,
                     'w': 2.360,
                     'x': 0.150,
                     'y': 1.974,
                     'z': 0.074}
frequency_english1 = {
                'a': 8.369698473393854,
                'b': 1.6206051694445256,
                'c': 1.6495209288070287,
                'd': 5.236352126448525,
                'e': 12.455942234157448,
                'f': 2.4463006071397295,
                'g': 2.4199845296126563,
                'h': 6.6077983157710385,
                'i': 6.229886672115357,
                'j': 0.04989564785895677,
                'k': 0.8869931988674509,
                'l': 4.371479027408856,
                'm': 2.4191179690008466,
                'n': 7.026575133541551,
                'o': 7.807255027875887,
                'p': 1.279864415190169,
                'q': 0.05523183688957646,
                'r': 6.00836641466476,
                's': 6.033861540033276,
                't': 8.924844566391313,
                'u': 2.6098981289588137,
                'v': 0.8050348083715229,
                'w': 2.691628477188476,
                'x': 0.05135511836305788,
                'y': 1.9004586386059137,
                'z': 0.042050993899413296 }
english_alphabet = sorted(list(frequency_english.keys()))
english_alphabet_indexes = dict(zip(english_alphabet, range(0, len(frequency_english))))
english_alphabet_values = dict(zip(range(0, len(frequency_english)), english_alphabet))

def count_matches(path1, path2): #подсчет процента соответствия 2 файлом
    f1 = open(path1, 'r')
    f2 = open(path2, 'r')
    matches = 0
    sum = 0
    while 1:
        line1 = f1.readline()
        line2 = f2.readline()
        if not line1 or not line2:
            break
        for i in range(len(line1)):
            if line1[i] == line2[i] and line1[i] in english_alphabet:
                matches += 1
            sum += 1
    return matches * 100 / sum

if __name__ == "__main__":
    filename = "king"
    #print(matches("shining.txt", "____shining.txt"))
    print(count_matches(filename + ".txt", "____" + filename + ".txt"))