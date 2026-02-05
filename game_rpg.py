# LATIHAN 1 
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


print("\n=== LATIHAN 1 ===")
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

hero1.hp = 500
print("HP Layla setelah diubah:", hero1.hp)

# LATIHAN 2 
print("\n=== LATIHAN 2 ===")
print("--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

# LATIHAN 3 
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana tidak cukup!")


print("\n=== LATIHAN 3 ===")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

# LATIHAN 5 
from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class HeroUnit(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


print("\n=== LATIHAN 5 ===")
h = HeroUnit("Alucard")
m = Monster("Serigala")

h.info()
m.info()

# LATIHAN 6 
class BaseHero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")


class MageHero(BaseHero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api!")


class ArcherHero(BaseHero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh!")


class FighterHero(BaseHero):
    def serang(self):
        print(f"{self.nama} (Fighter) menyerang dengan pedang!")


class HealerHero(BaseHero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")


print("\n=== LATIHAN 6 ===")
print("--- PERANG DIMULAI ---")

pasukan = [
    MageHero("Eudora"),
    ArcherHero("Miya"),
    FighterHero("Zilong"),
    MageHero("Gord"),
    HealerHero("Estes")
]

for pahlawan in pasukan:
    pahlawan.serang()
