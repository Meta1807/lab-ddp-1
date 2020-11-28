webinarList = [set(), set(), set()]  # Initialize a list whose items are empty sets
attendanceCount = {}  # Initialize a dictionary for storing attendance count based on name

for i in range(0, 3):
    for j in range(int(input(f'Nama yang akan dicatat untuk Webinar {i}: '))):
        nama = input(f'Masukkan nama {j + 1}')
        if nama:
            webinarList[i].add(nama)  # Python sets will automatically truncate duplicates.

for i in webinarList:
    for j in i:
        if j not in attendanceCount.keys():
            attendanceCount[j] = 1  # Add a new key into the dictionary if it doesn't exist
        else:
            attendanceCount[j] += 1  # Increment value with key of the attendant's name by 1

unionSet = webinarList[0] & webinarList[1] & webinarList[2]

print('Peserta yang datang ke Webinar Donat DUAARRR!!!:')
for index, item in enumerate(sorted(attendanceCount.items(), key=lambda x: -x[1])):
    if index != len(attendanceCount.items()) - 1:
        print(f'{item[0]}({item[1]})', end=', ')
    else:
        print(f'{item[0]}({item[1]})')
print('Peserta yang datang ke seluruh Webinar Donat DUAARRR!!!:')
print(*unionSet, sep=", ")
