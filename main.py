from ciphers.playfairSubstitutionCipher import PlayfairSubstitutionCipher
from ciphers.matrixTranspositionCipher import MatrixTranspositionCipher


def execute():

    while True:
        cipher = int(input("\n1.Playfair Substitution Cipher\n2.Matrix Transposition Cipher\n3.Exit\nEnter your choice:"))
        if cipher == 1:
            print("\nPlayfair Substitution Cipher")
            while True:
                operation = int(input("1.Encrypt message\n2.Decrypt message\n3.Exit\nEnter your choice: "))
                playfair_substitution_cipher = PlayfairSubstitutionCipher()
                if operation == 1:
                    cipher = playfair_substitution_cipher.encrypt("resources/playfairSubstitution/message.txt",
                                                                  "resources/playfairSubstitution/key.txt")
                    print("Encrypted message: {}".format(cipher))
                    break
                elif operation == 2:
                    plain_text = playfair_substitution_cipher.decrypt("resources/playfairSubstitution/message.txt",
                                                                      "resources/playfairSubstitution/key.txt")
                    print("Decrypted message: {}".format(plain_text))
                    break
                elif operation == 3:
                    break
                else:
                    print("Select the correct option")
        elif cipher == 2:
            print("Matrix Transposition Cipher")
            while True:
                operation = int(input("1.Encrypt message\n2.Decrypt message\n3.Exit\nEnter your choice: "))
                matrix_transposition_cipher = MatrixTranspositionCipher()
                if operation == 1:
                    cipher = matrix_transposition_cipher.encrypt("resources/matrixTransposition/message.txt",
                                                                 "resources/matrixTransposition/key.txt")
                    print("Encrypted message: {}".format(cipher))
                    break
                elif operation == 2:
                    plain_text = matrix_transposition_cipher.decrypt("resources/matrixTransposition/message.txt",
                                                                     "resources/matrixTransposition/key.txt")
                    print("Decrypted message: {}".format(plain_text))
                    break
                elif operation == 3:
                    break
                else:
                    print("Select the correct option")
        elif cipher == 3:
            exit()
        else:
            print("Select the correct option")


if __name__ == '__main__':
    execute()
