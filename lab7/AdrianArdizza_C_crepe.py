def unpack(item):
    lst = []
    if isinstance(item, tuple):
        if len(item) == 1:
            return unpack(item[0])
        elif len(item) > 1:
            # If there is more than one item, we must iterate through it and unpack every single item.
            # To do this recursively without a for loop, we first try to unpack the first index by recursively
            # calling unpack(item[0]), afterwards we try to unpack the next item along and repeat until we get a flattened string.
            lst.append(unpack(item[0]))
            lst.append(unpack(item[1:]))
        elif len(item) == 0:
            return ''  # If the length of the unpacked item is equal to 0, the function returns an empty string to the next function
        
        # Finally, we return the flattened objects to the next function in the call stack.
        return ' '.join(filter(str.strip, lst)) 
    else:
        # If the item is not a tuple, then we simply return the item (ex: if the item was a string)
        return item

user_input = eval(input('Masukkan isi Crepes: '))
unpacked = unpack(user_input)
# This if block is used to check if the unpacked tuple is empty/not, if it is empty then we print 'kosong'.
if len(unpacked.split()) == 0:
    print('kosong')
else:
    print(unpacked)
