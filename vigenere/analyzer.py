__author__ = 'Aface'

from vigenere import statistics

class VigenereAnalyzer(): #Анализ шифротекста
    def __init__(self):
        self.stats_frequency = statistics.frequency_english
        self.alphabet = statistics.english_alphabet
        self.alphabet_indexes = statistics.english_alphabet_indexes
        self.alphabet_values = statistics.english_alphabet_values
        self.index = 0.0667
        self.matches_table_length = int(len(self.alphabet) / 2)
        self.matches_table = {offset: 0
                              for offset
                              in range(1, self.matches_table_length)} #range(1, int(len(self.alphabet) / 2))
        self.key_length = None
        self.replacement_tables = []
        self.frequency_tables = []
        self.key_index = 0



    @staticmethod
    def shift(text, l):
        result = ""
        for i in range(len(text) - l):
            result += text[i + l]
        for i in range(l):
            result += text[i]
        return result

    def add_matches_info(self, text):
        #if len(text) < int(len(self.frequency) / 2):
            #raise Exception("String too short")
        shift = self.matches_table_length if self.matches_table_length <= len(text) else len(text)
        for i in range(1, shift):
            shifted = self.shift(text, i)
            for j in range(len(text)):
                if text[j] == shifted[j] and text[i] in self.alphabet:
                    self.matches_table[i] += 1

    def add_frequency_info(self, text):
        for i in range(len(text)):
            if text[i] in self.alphabet:
                self.frequency_tables[self.key_index % self.key_length][text[i]] += 1
            self.key_index += 1

    def decode(self, text):
        result = ""
        for i in range(len(text)):
            if text[i] in self.alphabet:
                result += self.replacement_tables[self.key_index % self.key_length][text[i]]
            else:
                result += text[i]
            self.key_index += 1
        return result

    def count_matches(self):
        total_matches = 0
        for offset in self.matches_table.keys():
            total_matches += self.matches_table[offset]
        for offset in self.matches_table.keys():
            self.matches_table[offset] /= total_matches
            self.matches_table[offset] /= 2

    def count_frequencies(self):
        for table in self.frequency_tables:
            total_chars = 0
            for c in table.keys():
                total_chars += table[c]
            for c in table.keys():
                table[c] = 100 * table[c] / total_chars


    def set_key_length(self, key_length):
        self.key_length = key_length
        for i in range(self.key_length):
            self.frequency_tables.append({c: 0 for c in self.alphabet})

    def make_replacement_tables(self):
        for i in range(self.key_length):
            current_table = {c: None for c in self.alphabet}
            for c_table in current_table.keys():
                min_d = 100.0
                min_c = None
                for c_freq in self.frequency_tables[i]:
                    current_d = abs(self.frequency_tables[i][c_table] - self.stats_frequency[c_freq])
                    if current_d < min_d:
                        min_d = current_d
                        min_c = c_freq
                current_table[c_table] = min_c
            self.replacement_tables.append(current_table)

    def find_key(self):
        key = ""
        for i in range(self.key_length):
            current_key_candidates = []
            for c_table in self.alphabet:
                min_d = 100.0
                min_c = None
                for c_freq in self.frequency_tables[i]:
                    current_d = abs(self.frequency_tables[i][c_table] - self.stats_frequency[c_freq])
                    if current_d < min_d:
                        min_d = current_d
                        min_c = c_freq
                c1 = self.alphabet_indexes[c_table]
                c2 = self.alphabet_indexes[min_c]
                current_key_candidates.append(self.alphabet_values[
                    (self.alphabet_indexes[c_table]
                     + self.alphabet_indexes[min_c])
                    % len(self.alphabet)])
            import collections
            counter = collections.Counter(current_key_candidates)
            print(counter)
            key += counter.most_common(1)[0][0]
        return key


def make_string(text):
    result = ""
    for i in range(len(text)):
        if text[i] in statistics.frequency_english.keys():
            result += text[i]
    return result


if __name__ == "__main__":
    filename = 'king'
    is_shuffled_alphabet = False

    va = VigenereAnalyzer()
    f = open('_' + filename + '.txt', 'r')
    f1 = open('____' + filename + '.txt', 'w')
    current_text = ""

    for line in f:
        va.add_matches_info(line)

    va.count_matches()
    print(va.matches_table)

    va.set_key_length(int(input("Key: ")))

    f.seek(0)
    for line in f:
        va.add_frequency_info(line)

    va.count_frequencies()

    for table in va.frequency_tables:
        print(table)

    if not is_shuffled_alphabet:
        print(va.find_key())
        for table in va.replacement_tables:
            print(table)
    else:
        va.make_replacement_tables()
        for table in va.replacement_tables:
            print(table)

        f.seek(0)
        va.key_index = 0
        for line in f:
            f1.write(va.decode(line))


