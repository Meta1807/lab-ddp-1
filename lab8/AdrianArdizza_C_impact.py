class Anemo:
    def __init__(self, name, hp, atk, em):
        self.name = name
        self.atk = int(atk)
        self.hp = int(hp)
        self.em = int(em)
    
    def attack(self, other):
        other.hp -= self.atk
    
    def elemental_skill(self, other):
        if self.em > other.em:
            if isinstance(other, Hydro) or isinstance(other, Pyro):
                other.hp -= (self.em + other.em)
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name:<20}| {int(self.hp)}"
        

class Pyro:
    def __init__(self, name, hp, atk, em):
        self.name = name
        self.atk = int(atk)
        self.hp = int(hp)
        self.em = int(em)

    def attack(self, other):
        other.hp -= self.atk

    def elemental_skill(self, other):
        if self.em > other.em:
            if isinstance(other, Hydro):
                other.hp -= 1.5 * self.em
            elif isinstance(other, Anemo):
                other.hp -= (self.em + other.em)
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name:<20}| {int(self.hp)}"


class Hydro:
    def __init__(self, name, hp, atk, em):
        self.name = name
        self.atk = int(atk)
        self.hp = int(hp)
        self.em = int(em)

    def attack(self, other):
        other.hp -= self.atk

    def elemental_skill(self, other):
        if self.em > other.em:
            if isinstance(other, Anemo):
                other.hp -= (self.em + other.em)
            elif isinstance(other, Pyro):
                other.hp -= (self.em * 2)


    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name:<20}| {int(self.hp)}"


def main():
    characters = {}
    while True:
        user_input = input('Masukkan karakter: ')
        if user_input:
            name, vision, hp, atk, em = user_input.split(' ')
            if vision == 'Anemo':
                characters[name] = Anemo(name, hp, atk, em)
            elif vision == 'Pyro':
                characters[name] = Pyro(name, hp, atk, em)
            elif vision == 'Hydro':
                characters[name] = Hydro(name, hp, atk, em)
            else:
                print(f"[ERROR] {vision}: Vision tidak valid")
        else:
            break
        
    # Mencetak interaksi yang dilakukan
    inp = input("\nKarakter yang berinteraksi: ")   
    while inp != "":
        name1, name2 = inp.split()
        char1 = characters.get(name1)
        char2 = characters.get(name2)

        if char1.is_alive() and char2.is_alive():
            char1.attack(char2)
            print(f"{char1.name} menyerang {char2.name} sebesar {char1.atk}")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
            inp = input("\nKarakter yang berinteraksi: ")
            continue
        
        if char1.is_alive() and char2.is_alive():
            char2.attack(char1)
            print(f"{char2.name} menyerang {char1.name} sebesar {char2.atk}")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
            inp = input("\nKarakter yang berinteraksi: ")
            continue

        if char1.is_alive() and char2.is_alive():
            char1.elemental_skill(char2)
            char2.elemental_skill(char1)
            
            if type(char1) == type(char2):
                print("Tidak terjadi reaksi elemen")
            else:
                if isinstance(char1, Anemo) or isinstance(char2, Anemo):
                    print("Terjadi reaksi elemen Swirl!")
                    if char1.em > char2.em:
                        damager = char1.name
                        damaged = char2.name
                    elif char2.em > char1.em:
                        damager = char2.name
                        damaged = char1.name

                    if char1.em != char2.em:
                        print(f"{damager} melukai {damaged} sebesar {char1.em + char2.em}!")
                    else:
                        print("Tidak ada yang terluka")
                else:
                    print("Terjadi reaksi elemen Vaporize!")
                    if char1.em > char2.em:
                        damager = char1.name
                        damaged = char2.name
                    elif char2.em > char1.em:
                        damager = char2.name
                        damaged = char1.name

                    if char1.em != char2.em:
                        if isinstance(characters[damager], Pyro):
                            damage = int(1.5 * characters[damager].em)
                        else:
                            damage = 2 * characters[damager].em
                        print(f"{damager} melukai {damaged} sebesar {damage}!")

                    else:
                        print("Tidak ada yang terluka")
        else:
            if not char1.is_alive():
                print(f"{char1.name} sudah mati.")
            elif not char2.is_alive():
                print(f"{char2.name} sudah mati.")
                
        inp = input("\nKarakter yang berinteraksi: ")
    

    print("\nKarakter yang masih hidup:")
    print("-"*27)
    print("Nama                | HP")
    print("-"*27)
    for char in characters:
        if characters[char].is_alive():
            print(characters[char])

if __name__ == '__main__':
    main()
