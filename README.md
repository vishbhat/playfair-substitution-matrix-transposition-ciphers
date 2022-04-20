# playfair-substitution-matrix-transposition-ciphers
The code is to emulate playfair substitution cipher and matrix transposition cipher. The plain/cipher text and the key are provided in two text files message.txt and key.txt in resources/playfairSubstitution or resources/mantrixTransposition directory. It is assumed that the message and key are provided in upper case alphabets only for matrix transposition, but the code is structured to convert alphabets to upper case if given in lower case and ignore any numbers and punctuations.In case of matrix transposition it is assumed that the message provided contains uppercase letters, lowercase letters, numbers, and spaces, where spaces are represented by %. The code is not structured to replace space with a %, hence the input message must contain % in place of space. The key must be provided with comma as the separating delimiter. For example, if the key is [1,2,3,4] then in the key.txt file it must be provided as 1,2,3,4.
* *Date Created*: 15 MAR 2022
* *Last Modification Date*: 20 APR 2022

## Authors

* [Vishwanath Hosdurga Suresh](mailto:vishubhat239@gmail.com)

## Built with
* [Python](https://www.python.org)
