from string import ascii_uppercase
from ciphers.constants import *
import operator

OPERATOR = {
    ENCRYPT: operator.add,
    DECRYPT: operator.sub
}


class PlayfairSubstitutionCipher(object):

    def __init__(self):
        pass

    def encrypt(self, msg_file, key_file):
        try:
            plain_text = self.__clean_input(self.__read_file(msg_file))
            key = self.__clean_input(self.__read_file(key_file))
            plain_text_matrix = self.__get_text_matrix(plain_text)
            key_matrix = self.generate_key(key)
            encrypted_msg = self.__resolve_from_key_matrix(key_matrix, plain_text_matrix, ENCRYPT)
            return encrypted_msg
        except Exception as e:
            print("Could not encrypt message due to: {}".format(e))

    def decrypt(self, msg_file, key_file):
        try:
            cipher_text = self.__clean_input(self.__read_file(msg_file))
            key = self.__clean_input(self.__read_file(key_file))
            cipher_text_matrix = self.__get_text_matrix(cipher_text.upper().replace(' ', ''))
            key_matrix = self.generate_key(key)
            decrypted_msg = self.__resolve_from_key_matrix(key_matrix, cipher_text_matrix, DECRYPT)
            return decrypted_msg
        except Exception as e:
            print("Could not decrypt message due to: {}".format(e))

    @staticmethod
    def generate_key(secret_key):
        try:
            secret_key = list(dict.fromkeys(secret_key.upper().replace('J', 'I')))
            for c in ascii_uppercase:
                if c == 'J':
                    continue
                if c not in secret_key:
                    secret_key.append(c)
            key_matrix = [secret_key[i:i+5] for i in range(0, len(secret_key), 5)]
            return key_matrix
        except Exception as e:
            print("Could not generate key matrix due to: {}".format(e))

    def __resolve_from_key_matrix(self, key_matrix, text_matrix, operation):
        message = []
        for i, j in text_matrix:
            i_i, i_j = self.__get_index_from_key_matrix(i, key_matrix)
            j_i, j_j = self.__get_index_from_key_matrix(j, key_matrix)
            i_i, i_j, j_i, j_j = self.__handle_same_row_col(i_i, i_j, j_i, j_j, operation)
            message.extend([key_matrix[i_i][j_j], key_matrix[j_i][i_j]])
        return "".join(message)

    @staticmethod
    def __handle_same_row_col(i_i, i_j, j_i, j_j, operation):
        if i_i == j_i:
            o_i_j = i_j
            i_j = OPERATOR[operation](j_j, 1) % 5
            j_j = OPERATOR[operation](o_i_j, 1) % 5
        if i_j == j_j:
            i_i = OPERATOR[operation](i_i, 1) % 5
            j_i = OPERATOR[operation](j_i, 1) % 5
        return i_i, i_j, j_i, j_j

    @staticmethod
    def __get_text_matrix(text):
        text_matrix = list()
        i = 0
        while True:
            unit = [text[i]]
            for c in text[i+1:]:
                if c not in unit:
                    unit.append(c)
                    i = i + 1
                else:
                    unit.append('Q') if unit[0] == 'X' else unit.append('X')
                break
            if len(unit) == 1:
                if unit[0] == 'Z':
                    unit.append('X')
                else:
                    unit.append('Z')
            text_matrix.append(unit)
            i = i + 1
            if i >= len(text):
                break
        return text_matrix

    @staticmethod
    def __get_index_from_key_matrix(c, key_matrix):
        for i in range(0, 5):
            try:
                j = key_matrix[i].index(c)
                return i, j
            except ValueError:
                continue
            except Exception as e:
                print("Could not find index of {} due to: {}".format(c, e))

    @staticmethod
    def __read_file(input_file):
        try:
            input_file = open(input_file, "r")
            return "".join([line.strip() for line in input_file.readlines()])
        except FileNotFoundError as e:
            print("Could not read file {} due to: {}".format(input_file, e))
        finally:
            input_file.close()

    @staticmethod
    def __clean_input(input_text):
        input_text = input_text.upper().replace(" ", "").replace('J', 'I')
        clean_text = [c for c in input_text if c.isalpha()]
        return "".join(clean_text)
