
class MatrixTranspositionCipher(object):

    def __init__(self):
        pass

    def encrypt(self, msg_file, key_file):
        plain_text = self.__read_file(msg_file)
        key = [int(c) for c in self.__read_file(key_file).split(',')]
        plain_text = [c for c in plain_text]
        message_matrix = [plain_text[i:i+len(key)] for i in range(0, len(plain_text), len(key))]
        if len(message_matrix[-1]) < len(key):
            for i in range(len(message_matrix[-1]), len(key)):
                message_matrix[-1].append('%')
        encrypted_msg = []
        for k in key:
            for row in message_matrix:
                encrypted_msg.append(row[k-1])
        encrypted_msg = "".join(encrypted_msg)
        return encrypted_msg

    def decrypt(self, msg_file, key_file):
        cipher_text = self.__read_file(msg_file)
        key = [int(c) for c in self.__read_file(key_file).split(',')]
        cipher_text = [c for c in cipher_text]
        row_size = len(cipher_text)//len(key)
        message_matrix = [cipher_text[i:i + row_size] for i in range(0, len(cipher_text), row_size)]
        decrypted_msg = []
        for i in range(0, row_size):
            for j in range(0, len(key)):
                index = key.index(j+1)
                decrypted_msg.append(str(message_matrix[index][i]))
        decrypted_msg = "".join(decrypted_msg)
        decrypted_msg = decrypted_msg.replace('%', '')
        return decrypted_msg

    @staticmethod
    def __read_file(input_file):
        try:
            input_file = open(input_file, "r")
            return "".join([line.strip() for line in input_file.readlines()])
        except FileNotFoundError as e:
            print("Could not read file {} due to: {}".format(input_file, e))
        finally:
            input_file.close()
