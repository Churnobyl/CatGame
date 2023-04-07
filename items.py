from object import *

# 아이템 - 윤성훈

# 아이템 클래스


class Item():
    def __init__(self, name, explanation):
        self.name = name
        self.explanation = explanation

# 장비템


class Equipment_Item(Item):
    def __init__(self, name, explanation, attack_effect):
        super().__init__(name, explanation)
        self.attack_effect = attack_effect

    def equip(self, player):
        if bool(player.eq) == False:
            player.attack += self.attack_effect
            player.eq = self.name
            print(f"{player.name}의 공격력이 {self.attack_effect}만큼 증가했습니다!")
            return True
        else:
            print(f"{player.name}가 이미 장비 착용중!")
            return False

# 포션


class Potion_Item(Item):
    def __init__(self, name, explanation, hp_effect, mp_effect, price, num):
        super().__init__(name, explanation)
        self.hp_effect = hp_effect
        self.mp_effect = mp_effect
        self.price = price
        self.num = num

    def take_potion_hp(self, player):
        self.num -= 1
        self.player = player
        player.HP += self.hp_effect
        print(f"{player.name}의 HP가 {self.hp_effect}만큼 회복됐습니다!")

    def take_potion_mp(self, player):
        self.num -= 1
        self.player = player
        player.MP += self.mp_effect
        print(f"{player.name}의 MP가 {self.mp_effect}만큼 회복됐습니다!")

    def __str__(self):
        return f"{self.num}"

# 펫


class Pet(Item):
    def __init__(self, name, explanation, defense, price, state):
        super().__init__(name, explanation)
        self.defense = defense
        self.price = price
        self.state = state

    def upgrade_defense(self, other):
        other.defense += self.defense

# ------------------


# 장비템 인스턴스
equipment1 = Equipment_Item(
    "날카로운 발톱", "공격력을 10만큼 올려줍니다.", 10)  # 냥검사 전용 아이템
equipment2 = Equipment_Item("방울", "공격력을 10만큼 올려줍니다.", 10)  # 냥법사 전용 아이템
equipment3 = Equipment_Item("새총", "공격력을 10만큼 올려줍니다.", 10)  # 냥궁수 전용 아이템
equipment4 = Equipment_Item("장난감 막대", "공격력을 10만큼 올려줍니다.", 10)  # 냥힐러 전용 아이템


# 포션 인스턴스
potion1 = Potion_Item("참치캔", "HP를 20만큼 채워줍니다.", 20, 0, 10, 0)
potion2 = Potion_Item("츄르", "MP를 20만큼 채워줍니다.", 0, 20, 10, 0)
potion3 = Potion_Item("북어포", "HP를 50만큼 채워줍니다.", 50, 0, 25, 0)
potion4 = Potion_Item("캣닢", "MP를 50만큼 채워줍니다.", 0, 50, 25, 0)

total_potions = 0

# 펫 인스턴스
pet1 = Pet('털뭉치', '방어력을 5만큼 증가시켜줍니다.', 5, 100, 0)
pet2 = Pet('캔디볼', '방어력을 10만큼 증가시켜줍니다.', 10, 200, 0)
pet3 = Pet('도토리볼', '방어력을 15만큼 증가시켜줍니다.', 15, 300, 0)

pets = {
    "1": Pet('털뭉치', '방어력을 5만큼 증가시켜줍니다.', 5, 100, 0),
    "2": Pet('캔디볼', '방어력을 10만큼 증가시켜줍니다.', 10, 200, 0),
    "3": Pet('도토리볼', '방어력을 15만큼 증가시켜줍니다.', 15, 300, 0)
}
