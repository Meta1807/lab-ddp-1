def sublist_sort(to_sort, order):  # Sorting function (selection sort algorithm implemented by myself)
    list_length = len(to_sort)
    while list_length != 0:
        largest_item = 0
        largest_in_sub = 0
        for i, item in enumerate(to_sort[:list_length]):
            if int(item) >= largest_item:  # If the number is higher than the current maximum, set it as the new maximum
                largest_item = item
                largest_in_sub = i
        to_sort.append(to_sort.pop(largest_in_sub))  # Append largest number in sublist to the end of the list
        list_length -= 1  # Reduce size of the sublist

    if order == 'ascending':
        to_sort.reverse()
    return to_sort

in_filename = input("Masukkan nama file input: ")

try:
    """
    TODO - Task 1
     > Menerima Input
     > Membaca File
     > Menghitung minimum, maksimum, serta range 
       dari karakter pada baris-baris yang ada 
     > Menulis output program file yang sama tanpa 
       menghilangkan isi file yang sebelumnya
    """
    # Define 4 variables for holding characters and number of lines (line_length is a list, and all other variables are ints)
    line_length = []
    line_minimum = 0
    line_maximum = 0
    line_range = 0
    # Open the specified input file and count the inputs.
    with open(in_filename, 'r') as data:
        lines = data.readlines()
        number_of_lines = len(lines)  # Get the number of lines.
        for line in lines:
            line = line.strip()  # Strip all newline characters from the line.
            if len(line) != 0:  # Do not append length of line if it is 0
                line_length.append(len(line))

        if line_length:  # Output to file if file is not empty
            line_length = sublist_sort(line_length, 'ascending')  # Sort lines in ascending order to find min and max

            line_minimum = line_length[0]  # Min is at the beginning of the list after being sorted
            line_maximum = line_length[-1] # Max is at the end of list after being sorted
            line_range = line_maximum - line_minimum

            # Print Min, Max, and Range to output file
            with open(in_filename, 'a+') as output:
                print("#" * 10, file=output)
                print(f'Min: {line_minimum}', file=output)
                print(f'Max: {line_maximum}', file=output)
                print(f'Range: {line_range}', file=output)
        else:
            with open(in_filename, 'a+') as output:
                print('NULL', file=output)

except FileNotFoundError: # Diisi error handling file error
	print("File tidak ditemukan :(")

except Exception:
    print("An exception has occurred!")

else: # Diisi statement yang dijalankan ketika program berjalan tanpa error
	print(f"Output berhasil ditulis pada {in_filename}")

input("Program selesai. Tekan enter untuk keluar...")
