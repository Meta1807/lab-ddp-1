# a-z is 97-122
# A-Z is 65-90
alphabet = {}

for i in range(65, 91):
    alphabet[chr(i)] = i - 65

for i in range(97, 123):
    alphabet[chr(i)] = i - 71

def convert_to_eligma(string):
    offset = 0
    alpha = ''
    cipher_text = ''
    
    for c in string:
        if c.isnumeric():
            offset += int(c)
        else:
            alpha += c

    for item in alpha:
        # Overflow algorithm (the range for characters in unicode is 97-122 (a-z), hence if we subtract by 97 and modulo, 
        # we can account for offset overflows)
        cipher_offset = (alphabet[item] + offset) % 52
        cipher_text += list(alphabet.keys())[cipher_offset]
    return cipher_text

initial_string = input("Masukkan string yang ingin di encode: ")
encrypted_string = convert_to_eligma(initial_string)

print(encrypted_string)