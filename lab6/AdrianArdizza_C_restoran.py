class Data():
    def __init__(self, menuData: dict):
        '''
            [ARGUMENTS]
            - self: Refers to the object's own properties
            - menuData: Dictionary containing all menu items and their respective values (also a dictionary with keys for price and flavor)

            [DESCRIPTION]
            This function is called on object initialization, and sets the object's menu properties to the given menuData. It also initializes
            the bought and income property for later use in the program.
        '''
        self.menu = menuData
        self.bought = set()
        self.income = 0
    
    def beliNama(self, donut: str):
        ''' Registers a purchase of a donut (by name) and increments it to income.

            [ARGUMENTS]
            - self: Refers to the object's own properties
            - donut: String that represents the requested menu item

            [DESCRIPTION]
            This method increments the income counter by the price of the specified donut and registers it into the self.bought set.

        '''
        if donut in self.menu.keys():
            self.income += self.menu[donut]['harga']
            self.bought.add(donut)
            print(f'{donut} terjual dengan harga {self.menu[donut]["harga"]}')
        else:
            print(f'Tidak ada Donat DUARRR!!! dengan nama {donut} :(')
    
    def beliRasa(self, rasa: str):
        ''' Registers a purchase of the most expensive donut in a flavor category.

            [ARGUMENTS]
            - self: refers to the object's own properties
            - rasa: String that refers to a flavor category
            
            [DESCRIPTION]
            This method first groups all donuts with the requested flavor into a single list. Afterwards, it finds the donut with the highest
            price in that list, registers it's name into the self.bought set, and increments the object's income property by it's price.

        '''
        listRasa = []
        for key, value in self.menu.items():
            if value['rasa'] == rasa:
                listRasa.append((key, value))  # Append a tuple with the item's key-value pair into listRasa
        if (listRasa):
            maxPrice = max(listRasa, key=lambda x: x[1]['harga'])  # Sort by price using an anonymous lambda function
            self.income += maxPrice[1]['harga']
            self.bought.add(maxPrice[0])
            print(f'{maxPrice[0]} terjual dengan harga {maxPrice[1]["harga"]}')
        else:
            print(f'Tidak ada Donut DUARRR!!! dengan rasa {rasa} :(')

while True:
    jumlahMenu = input('Masukkan Jumlah Donat DUAARRR!!!: ')
    if jumlahMenu.isnumeric():
        jumlahMenu = int(jumlahMenu)
        break
    else:
        print('Input harus berupa angka.')


menuDict = {}

for i in range(jumlahMenu):
    userInput = input(f'Data {i + 1}: ').split()
    menuDict[userInput[0]] = {'harga': int(userInput[1]), 'rasa': userInput[2]}

dataRestoran = Data(menuDict)

while True:
    jumlahPembeli = input('Masukkan Jumlah Pembeli: ')
    if jumlahPembeli.isnumeric():
        jumlahPembeli = int(jumlahPembeli)
        break
    else:
        print('Input harus berupa angka.')

for i in range(jumlahPembeli):
    arguments = input(f'Pembeli {i + 1}: ').split()
    if arguments[0] == 'BELI_NAMA':
        dataRestoran.beliNama(arguments[1])
    if arguments[0] == 'BELI_RASA':
        dataRestoran.beliRasa(arguments[1])

print('\n')
print(f'Donat Terjual:', end = " ")
print(*dataRestoran.bought, sep=', ')
print(f'Total Pendapatan: {dataRestoran.income}')
    