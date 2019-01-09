class Playfair(object):
    LETTER_PAIR = letter_pair = ('I', 'J')
    DEFAULT_TABLE = ['A', 'B', 'C', 'D', 'E',
                     'F', 'G', 'H', 'I', 'K',
                     'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, key, letter='X', ):
        assert isinstance(key, str)
        assert isinstance(letter, str) and len(letter) == 1
        self.key = key.upper()
        self.letter = letter
        self.table = self.generate_table(self.key)

    @classmethod
    def generate_table(cls, key):
        assert isinstance(key, str)
        default_table = cls.DEFAULT_TABLE.copy()
        key_table = list()
        for each_alphabet in key.replace(cls.LETTER_PAIR[1], cls.LETTER_PAIR[0]):
            if each_alphabet.isalpha() and each_alphabet in default_table:
                key_table.append(each_alphabet)
                default_table.remove(each_alphabet)
        for each_alpha in default_table:
            key_table.append(each_alpha)
        return key_table

    def print_table(self):
        print('PlayFair Table (Key: \"{}\"):'.format(self.key))
        for idx in range(0, 25, 5):
            print(self.table[idx:idx + 5])

    def group(self, data):
        assert isinstance(data, str)
        counter = 0
        backup = ''
        group = ''
        for each_alphabet in data:
            if each_alphabet.isalpha():
                if backup.upper() == each_alphabet.upper():
                    group += self.letter + each_alphabet
                    counter += 2
                else:
                    group += each_alphabet
                    counter += 1
                backup = each_alphabet
            else:
                group += each_alphabet
        return group if counter % 2 == 0 else group + self.letter

    def encrypt(self, data):
        assert isinstance(data, str)
        counter = 0
        ciphertext = ''
        buffer = ''
        group = self.group(data)
        for each_alphabet in group:
            if each_alphabet.isalpha():
                counter += 1
                buffer += each_alphabet
                if counter == 2:
                    begin_idx = self.table.index(buffer[0].upper())
                    begin_row = int(begin_idx / 5)
                    begin_column = begin_idx % 5
                    end_idx = self.table.index(buffer[-1].upper())
                    end_row = int(end_idx / 5)
                    end_column = end_idx % 5
                    if begin_row == end_row:
                        # SAME ROW
                        begin_idx = begin_row * 5 + (begin_column + 1) % 5
                        end_idx = end_row * 5 + (end_column + 1) % 5
                    elif begin_column == end_column:
                        # SAME COLUMN
                        begin_idx = (begin_row + 1) % 5 * 5 + begin_column
                        end_idx = (end_row + 1) % 5 * 5 + end_column
                    else:
                        begin_idx = begin_row * 5 + end_column
                        end_idx = end_row * 5 + begin_column
                    ciphertext += self.table[begin_idx] if buffer[0].isupper() else self.table[begin_idx].lower()
                    ciphertext += buffer[1:-1]
                    ciphertext += self.table[end_idx] if buffer[-1].isupper() else self.table[end_idx].lower()
                    counter = 0
                    buffer = ''
            elif counter == 0:
                ciphertext += each_alphabet
            else:
                buffer += each_alphabet
        return ciphertext

    def decrypt(self, data):
        assert isinstance(data, str)
        counter = 0
        plaintext = ''
        buffer = ''
        for each_alphabet in data:
            if each_alphabet.isalpha():
                counter += 1
                buffer += each_alphabet
                if counter == 2:
                    begin_idx = self.table.index(buffer[0].upper())
                    begin_row = int(begin_idx / 5)
                    begin_column = begin_idx % 5
                    end_idx = self.table.index(buffer[-1].upper())
                    end_row = int(end_idx / 5)
                    end_column = end_idx % 5
                    if begin_row == end_row:
                        # SAME ROW
                        begin_idx = begin_row * 5 + (begin_column - 1) % 5
                        end_idx = end_row * 5 + (end_column - 1) % 5
                    elif begin_column == end_column:
                        # SAME COLUMN
                        begin_idx = (begin_row - 1) % 5 * 5 + begin_column
                        end_idx = (end_row - 1) % 5 * 5 + end_column
                    else:
                        begin_idx = begin_row * 5 + end_column
                        end_idx = end_row * 5 + begin_column
                    plaintext += self.table[begin_idx] if buffer[0].isupper() else self.table[begin_idx].lower()
                    plaintext += buffer[1:-1]
                    plaintext += self.table[end_idx] if buffer[-1].isupper() else self.table[end_idx].lower()
                    counter = 0
                    buffer = ''
            elif counter == 0:
                plaintext += each_alphabet
            else:
                buffer += each_alphabet
        return plaintext


if __name__ == '__main__':
    alphabet_Key = 'playfair example'
    data = 'Hide the gold in the tree stump'
    key = Playfair(key=alphabet_Key)
    ciphertext = key.encrypt(data)
    print('Data: {}'.format(data))
    key.print_table()
    print('Ciphertext: {}'.format(ciphertext))
    print('Plaintext: {}'.format(key.decrypt(ciphertext)))
