def convert_to_eligma(string):
    offset = 0
    alpha = ''
    cipher_text = ''

    # Add all numeric chars to offset, and all alphabetical chars to a new string.
    for c in string:
        if c.isnumeric():
            offset += int(c)
        else:
            alpha += c
    else:
        string = ''  # Clean old string for GC (saves RAM :D)

    for item in alpha:
        ''' 
        Overflow algorithm. 
        the range for characters in unicode is 97-122 (a-z), hence if we subtract by 97 and modulo, 
        we can account for offset overflows.
        This basically concatenates a character to cipher_text based on the ciphered char's offset from 'a'
        '''
        cipher_offset = (ord(item) + offset - ord('a')) % 26
        cipher_text += (chr(ord('a') + cipher_offset))

    return cipher_text

initial_string = input("Masukkan string yang ingin di encode: ")
encrypted_string = convert_to_eligma(initial_string)

print(encrypted_string)