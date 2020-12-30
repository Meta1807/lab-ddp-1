class Hero():
    def __init__(self, name, hp, attack):
        """
        Constructor untuk class Hero, akan dipanggil saat inisiasi objek dan saat dipanggil dengan super().__init__
        """
        self.__name = name
        self.__attack = int(attack)
        self.__hp = int(hp)

    # Getter
    def get_name(self) -> str:
        """
        Getter untuk atribut name, akan return atribut nama dari Hero.
        """
        return self.__name

    def get_hp(self) -> int:
        """
        Getter untuk atribut hp, akan return atribut HP dari Hero
        """
        return self.__hp

    def get_attack(self) -> int:
        """
        Getter untuk atribut attack, akan return atribut attack dari HP hero
        """
        return self.__attack

    # Setter
    def set_hp(self, hp) -> int:
        """
        Setter untuk atribut hp, apabila parameter hp positif maka dia akan set atribut hp menjadi parameter, kalau tidak negatif atau 0
        akan set atribut hp menjadi 0.
        """
        if hp > 0:
            self.__hp = hp
        else:
            self.__hp = 0

    def attack(self, other) -> None:
        """
        Method untuk menyerang lawan, base attack function memanggil method damaged di class other.
        """
        other.damaged(self.get_attack())

    def damaged(self, attack) -> None:
        """
        Method untuk mengubah status apabila diserang lawan, set hp menjadi value hp sekarang dikurang attack yang dialami.
        """
        self.set_hp(self.get_hp() - attack)

    def is_alive(self) -> bool:
        """
        Method untuk mengecek apakah karakter masih hidup atau sudah mati.
        """
        if self.get_hp() == 0:
            return False
        else:
            return True

    def __str__(self) -> str:
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'HERO':10s}| {self.get_hp():5d}"


class Support(Hero):
    def __init__(self, name, hp, attack, atribut_khusus=20):
        super().__init__(name, hp, attack)  # Memanggil constructor object dari parent.
        self.__heal_amount = int(atribut_khusus)

    def get_heal_amount(self) -> int:
        """
        Getter untuk atribut heal_amount, akan return atribut heal amount dari class Support
        """
        return self.__heal_amount

    def heal(self, other) -> None:
        """
        Method untuk menambah hp hero lain, akan inkremen nilai hp dari karakter lain sebanyak atribut heal amount
        dari Healer
        """
        if other != self:
            other.set_hp(other.get_hp() + self.get_heal_amount())

    def __str__(self) -> str:
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'Support':10s}| {self.get_hp():5d}"

    def __add__(self, other):
        """
        Method untuk melakukan operator overloading (+)
        """
        return Support(f"{self.get_name()}_{other.get_name()}", self.get_hp() + other.get_hp(), self.get_attack() + other.get_attack(), self.get_heal_amount() + other.get_heal_amount())


class Warrior(Hero):
    def __init__(self, name, hp, attack, atribut_khusus=20):
        # HINT: gunakan method super() & gunakan default parameter
        super().__init__(name, hp, attack)
        self.__extra_attack = atribut_khusus

    def get_extra_attack(self) -> int:
        """
        Getter untuk atribut extra_attack akan return atribut extra_attack dari Warrior.
        """
        return self.__extra_attack

    def attack(self, other) -> None:
        """
        Method untuk menyerang lawan, untuk Warrior akan mengurangi sebanyak atribut attack Warrior ditambah dengan atribut extra_attacknya.
        """
        other.damaged(self.get_attack() + self.get_extra_attack())

    def __str__(self) -> str:
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'Warrior':10s}| {self.get_hp():5d}"

    def __add__(self, other):
        """
        Method untuk melakukan operator overloading (+)
        """
        if type(self) == type(other):
            return Warrior(f"{self.get_name()}_{other.get_name()}", self.get_hp() + other.get_hp(), self.get_attack() + other.get_attack(), self.get_extra_attack() + other.get_extra_attack())


class Tank(Hero):
    def __init__(self, name, hp, attack, atribut_khusus=20):
        # HINT: gunakan method super() & gunakan default parameter
        super().__init__(name, hp, attack)
        self.__shield = int(atribut_khusus)

    def get_shield(self) -> int:
        """
        Getter untuk atribut shield
        """
        return self.__shield

    def set_shield(self, shield) -> None:
        """
        Setter untuk atribut shield
        """
        self.__shield = int(shield)

    def damaged(self, attack) -> None:
        """
        Method untuk mengubah status apabila diserang lawan, untuk shield, attack akan mengurangi value dari shield terlebih dahulu
        sebelum HP, sehingga kondisi yang harus di cek adalah apakah attack lebih besar sama dengan shield atau tidak.
        """
        if self.get_shield() >= attack:
            self.set_shield(self.get_shield() - attack)
        else:
            self.set_hp(self.get_hp() + self.get_shield() - attack)
            self.set_shield(0)

    def __str__(self) -> str:
        """
        Method untuk mengembalikan representasi String
        """
        return f"{self.get_name():20s}| {'Tank':10s}| {self.get_hp():5d}"

    def __add__(self, other):
        """
        Method untuk melakukan operator overloading (+)
        """
        if type(self) == type(other):
            return Tank(f"{self.get_name()}_{other.get_name()}", self.get_hp() + other.get_hp(), self.get_attack() + other.get_attack(), self.get_shield() + other.get_shield())

# NOTE: method main() & get_hero() tidak perlu diubah


def get_hero(name, list_hero):
    """
    Method untuk mengembalikan hero dengan name sesuai parameter
    """
    for hero in list_hero:
        if hero.get_name() == name:
            return hero


def main():
    list_hero = []

    banyak_hero = int(input("Masukkan jumlah hero : "))

    for i in range(banyak_hero):
        input_hero = input("Masukkan detail hero : ")
        detail_hero = input_hero.split()
        tipe = detail_hero[0]
        nama = detail_hero[1]
        hp = int(detail_hero[2])
        attack = int(detail_hero[3])
        atribut_tambahan = detail_hero[4]
        if tipe == "SUPPORT":
            if atribut_tambahan != "DEFAULT":
                list_hero.append(
                    Support(nama, hp, attack, int(atribut_tambahan)))
            else:
                list_hero.append(Support(nama, hp, attack))
        elif tipe == "WARRIOR":
            if atribut_tambahan != "DEFAULT":
                list_hero.append(
                    Warrior(nama, hp, attack, int(atribut_tambahan)))
            else:
                list_hero.append(Warrior(nama, hp, attack))
        elif tipe == "TANK":
            if atribut_tambahan != "DEFAULT":
                list_hero.append(Tank(nama, hp, attack, int(atribut_tambahan)))
            else:
                list_hero.append(Tank(nama, hp, attack))

    perintah = input("Masukkan perintah : ")
    list_perintah = perintah.split()
    while list_perintah[0] != "EXIT":
        if list_perintah[0] == "ATTACK":
            karakter1 = get_hero(list_perintah[1], list_hero)
            karakter2 = get_hero(list_perintah[2], list_hero)
            if (karakter1 != None and karakter2 != None):
                karakter1.attack(karakter2)
                if not karakter2.is_alive():
                    list_hero.remove(karakter2)
                print(f"{karakter1.get_name()} berhasil menyerang {karakter2.get_name()}")
                print(f"Nyawa {karakter2.get_name()} tersisa {karakter2.get_hp()}")
            else:
                print("Karakter tidak ditemukan")

        elif list_perintah[0] == "HEAL":
            karakter1 = get_hero(list_perintah[1], list_hero)
            karakter2 = get_hero(list_perintah[2], list_hero)
            if (karakter1 != None and karakter2 != None):
                if isinstance(karakter1, Support):
                    if karakter1 != karakter2:
                        karakter1.heal(karakter2)
                        print(f"{karakter1.get_name()} berhasil meng-heal {karakter2.get_name()}")
                        print(f"Nyawa {karakter2.get_name()} menjadi {karakter2.get_hp()}")
                    else:
                        print(f"{karakter1.get_name()} tidak dapat meng-heal dirinya sendiri")
                else:
                    print(f"{karakter1.get_name()} bukan merupakan Support")
            else:
                print("Karakter tidak ditemukan")

        elif list_perintah[0] == "GABUNGKAN":
            karakter1 = get_hero(list_perintah[1], list_hero)
            karakter2 = get_hero(list_perintah[2], list_hero)
            if type(karakter1) == type(karakter2):
                if (karakter1 != None and karakter2 != None):
                    combined_hero = karakter1 + karakter2
                    print(f"{karakter1.get_name()} berhasil bergabung dengan {karakter2.get_name()}", end=" ")
                    print(f"menjadi {combined_hero.get_name()}")
                    list_hero.remove(karakter1)
                    list_hero.remove(karakter2)
                    list_hero.append(combined_hero)
                else:
                    print("Karakter tidak ditemukan")
            else:
                print("Gagal menggabungkan karena tipe kedua karakter berbeda")

        perintah = input("Masukkan perintah : ")
        list_perintah = perintah.split()

    print("\nKarakter yang masih hidup:")
    print("-"*40)
    print("Nama                | Tipe      | HP   ")
    print("-"*40)
    for hero in list_hero:
        print(hero)


if __name__ == "__main__":
    main()
