import os
import platform
import random
import re
import time


# 레벨업마다 전체스탯이 오르는 함수입니다. 20퍼센트씩(15.0) 오르는 것으로 임의 조정해놨습니다.. 오류.. 뜰지도 모르겠습니다... :>...
def sh_state_up(a):
    return int(a * 1.2)

# 레벨업마다 max_exp의 값이 오르는 함수입니다.. 80퍼센트씩 오르는 것으로 임의 조정해놨습니다. 경험치 드랍량 보면서 조절해야겠슴당


def sh_max_exp_up(a):
    return int(a * 1.8)


class Object():

    def __init__(self, name, level, HP, MP, attack, defense, speed, skill=None) -> None:
        self.name = name
        self.level = level
        self.max_HP = HP
        self.HP = HP
        self.max_MP = MP
        self.MP = MP
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.skill = skill

    # 일반공격_플레이어_몬스터_전부사용 / 공격력비례 랜덤값 / 몬스터의 방어력비례(40퍼) 뎀감 / 전부 임의값입니다

    def normal_attack(self, monster):
        first_damage = random.randint(
            int(self.attack * 0.7), int(self.attack * 1.2))
        damage = first_damage - int(monster.defense * 0.4)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        # time.sleep(2)
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True

    def status(self):
        print(f"{self.name} LV.{self.level} : EXP {self.exp}/{self.max_exp}\n   HP {self.HP}/{self.max_HP} | MP {self.MP}/{self.max_MP}")

    # 클래스 호출 시 문자열 출력

    def __str__(self):
        if self.HP == 0:
            return "기절"
        else:
            return self.name


class Character(Object):
    def __init__(self, name, level, HP, MP, attack, defense, speed, skill, eq='', exp=0, max_exp=100) -> None:
        super().__init__(name, level, HP, MP, attack, defense, speed, skill)
        self.exp = exp
        self.max_exp = max_exp
        self.eq = eq

    # 특수공격_냥검사 / 마나값 임의 / 공격값은 공격력비례 임의의 랜덤(기본 ~ +50%)값 - 몬스터의 방어력비례(30퍼) / 임의값입니다

    def dealing_Skill(self, monster):
        self.MP = max(self.MP - 30, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        first_damage = random.randint(self.attack, int(self.attack * 1.5))
        damage = first_damage - int(monster.defense * 0.3)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 특수공격_냥법사 / 마나값, 디벞값은 방어력비례 임의의 랜덤(기본 ~ +30%)값으로 주었습니다

    def debuff_Skill(self, monster):
        self.MP = max(self.MP - 40, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        debuff = random.randint(self.defense, int(self.defense * 1.5))
        monster.defense = max(monster.defense - debuff, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}의 방어력을 {debuff}만큼 깎았습니다.")
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 특수공격_냥궁수 / 마나값 임의 / 공격값은 스피드비례 임의의 랜덤(기본 ~ +50%)값 - 몬스터 방어력비례(30퍼) / 임의값입니다

    def shooting_Skill(self, monster):
        self.MP = max(self.MP - 30, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        first_damage = random.randint(self.speed, int(self.speed * 1.5))
        damage = first_damage - int(monster.defense * 0.3)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 특수공격_냥힐러 / 마나값, 힐링값 임의로 주었습니다 / 지금 print 문이.. self.name이 시전하면서 self.name이 회복하는거라.. 이게 자힐로 들어가는 방법밖에.. 어떡할가여.. :>?

    def healing_Skill(self, friend, monster):
        self.MP = max(self.MP - 50, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        heal = int(self.max_HP * 0.3)
        if friend.max_HP >= friend.HP + heal:
            friend.HP += heal
        elif friend.max_HP < friend.HP + heal:
            heal -= (friend.HP+heal - friend.max_HP)
        healing = heal
        print(f"{self.name}의 {self.skill}! {self.name}의 HP를 {healing}만큼 회복했습니다.")
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    def level_plus1(self):
        self.max_HP = sh_state_up(self.max_HP)
        self.HP = sh_state_up(self.HP)
        self.max_MP = sh_state_up(self.max_MP)
        self.MP = sh_state_up(self.MP)
        self.attack = sh_state_up(self.attack)
        self.defense = sh_state_up(self.defense)
        self.speed = sh_state_up(self.speed)

    # exp의 값이 max_exp의 값과 같거나 넘칠 때 레벨업과 레벨업 print 출력, exp값 유지하는 대신 max_exp의 값만 비례값으로 올라갑니다.
    # 전투 종료시 경험치 드랍과 함께 매번 추가해주시는 함수와 같다고 생각해주시면 될 것 같습니다. return 선언 방식이 잘못되었다면 주석 달아주시거나 말 걸어주세요!!

    def level_up(self, _exp):
        self.exp = _exp
        while True:
            if self.exp >= self.max_exp:
                self.level += 1
                print(f'{self.name}가 LV.{self.level}로 레벨업했습니다!')
                self.max_exp = sh_max_exp_up(self.max_exp)
                self.level_plus1()
            else:
                break
            print(self.max_HP, self.HP, self.max_MP, self.MP,
                  self.attack, self.defense, self.speed)
        return

#   캐릭터 전투시작 & 디폴트 스테이터스 창
    def status(self):
        print(f"{self.name} LV. {self.level} || EXP: ({self.exp} / {self.max_exp}) || HP: ({self.HP} / {self.max_HP}) || MP: ({self.MP} / {self.max_MP})")

#   캐릭터 올 스테이터스 창 /
    def all_status(self):
        print(f"EXP: ({self.exp} / {self.max_exp}) || HP: ({self.HP} / {self.max_HP}) || MP: ({self.MP} / {self.max_MP})\n   ATK: {self.attack} || DEF: {self.defense} || SPD: {self.speed} || eq='' ")


class Monster(Object):
    def __init__(self, name, level, HP, MP, attack, defense, speed) -> None:
        super().__init__(name, level, HP, MP, attack, defense, speed)
        weight = round(level / 100, 2)  # 레벨/100배 증가
        self.HP = int(HP * (1 + weight))
        self.max_HP = int(HP * (1 + weight))
        self.MP = int(MP * (1 + weight))
        self.max_MP = int(MP * (1 + weight))
        self.attack = int(attack * (1 + weight))
        self.defense = int(defense * (1 + weight))
        self.speed = int(speed * (1 + weight))

    # 몹 전투시작 디폴트 스테이터스
    def monster_status(self):
        print(f"{self.name} LV. {self.level} || HP: ({self.HP} / {self.max_HP}) || ATK: {self.attack} || DEF: {self.defense} || SPD: {self.speed}")


class Boss(Monster):
    def __init__(self, name, level, HP, MP, attack, defense, speed, skill) -> None:
        super().__init__(name, level, HP, MP, attack, defense, speed)
        self.skill = skill

    # 슈뢰딩거의상_자식_5턴 / 공격값은 체력비례 랜덤(기본~ +50%)값 - 캐릭터의 방어력비례(30%) / 임의값입니다
    def box_shot(self, monster):
        first_damage = random.randint(self.HP, int(self.HP * 1.5))
        damage = first_damage - int(monster.defense * 0.3)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 잼민스킬_돌던지기_5턴 / 잼민무리.. 중간보스지만 2명이면 좋을 것 같아요 인당 1캐릭씩 랜덤타깃으로 생각했습니다
    # 공격값은 스피드비례 랜덤(기본 ~ +50%)값 - 캐릭터의 방어력비례(30%) / 임의값입니다
    # Print문 검토 필요@@!!
    def boss_attack(self, monster):
        first_damage = random.randint(self.speed, int(self.speed * 1.5))
        damage = first_damage - int(monster.defense * 0.3)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.hp == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 제리의볼링쇼/ 4턴마다 / 광역스킬 / 공격값은 공격력비례 랜덤(기본+20% ~ +60%) - 캐릭터방어력비례(30%) / 임의값입니다
    def jerry_attack(self, monster):
        first_damage = random.randint(
            int(self.attack * 1.2), int(self.attack * 1.6))
        damage = first_damage - int(monster.defense * 0.3)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.hp == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 보스 전투시작 총 스테이터스
    def boss_status(self):
        print(f"{self.name} LV. {self.level} || HP: ({self.HP} / {self.max_HP}) || MP: ({self.MP} / {self.max_MP})\n   ATK: {self.attack} || DEF: {self.defense} || SPD: {self.speed} || SKILL: {self.skill}")


# 아이템 - 윤성훈


class Item():
    def __init__(self, name, explanation):
        self.name = name
        self.explanation = explanation


class Equipment_Item(Item):
    def __init__(self, name, explanation, attack_effect):
        super().__init__(name, explanation)
        self.attack_effect = attack_effect

    def equip(self, player):
        self.player = player
        player.attack += self.attack_effect
        print(f"{player.name}의 공격력이 {self.attack_effect}만큼 증가했습니다!")
        print(player.attack)
        print(self.name)


class Potion_Item(Item):
    def __init__(self, name, explanation, hp_effect, mp_effect, num):
        super().__init__(name, explanation)
        self.hp_effect = hp_effect
        self.mp_effect = mp_effect
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


class Pet(Item):
    def __init__(self, name, explanation, defense, price):
        super().__init__(name, explanation)
        self.defense = defense
        self.price = price

    def upgrade_defense(self, other):
        other.defense += self.defense


#
characters = {
    "1": Character("냥검사", 1, 1500, 300, 150, 200, 130, "냥냥펀치",),
    "2": Character("냥법사", 1, 1200, 500, 120, 130, 100, "하악질"),
    "3": Character("냥궁수", 1, 1000, 400, 180, 100, 180, "꾹꾹이"),
    "4": Character("냥힐러", 1, 1400, 500, 90, 160, 140, "그루밍")
}

character_skills = {
    "냥냥펀치": characters["1"].dealing_Skill,
    "하악질": characters["2"].shooting_Skill,
    "꾹꾹이": characters["3"].debuff_Skill,
    "그루밍": characters["4"].healing_Skill
}

# player = Character("냥검사", 1, 150, 30, 15, 20, 13)
# player = Character("냥법사", 1, 120, 50, 12, 13, 10)
# player = Character("냥궁수", 1, 100, 40, 18, 10, 18)
# player = Character("냥힐러", 1, 140, 50, 9, 16, 14)

bosses = [
    Boss("슈뢰딩거", 1, 1500, 300, 150, 200, 130, "슈뢰딩거의상 자식"),
    Boss("잼민이", 1, 1200, 500, 120, 130, 100, "돌 던지기"),
    Boss("잼순이", 1, 1000, 400, 180, 100, 180, "꼬리 당기기"),
    Boss("제리", 1, 1400, 500, 90, 160, 140, "볼링쇼")
]

bosses_skills = [
    bosses[0].box_shot,
    bosses[1].boss_attack,
    bosses[2].boss_attack,
    bosses[3].jerry_attack
]

# ------------------

# # 장비 아이템 장착
# equipment_items = {
#     "1": Equipment_Item("날카로운 발톱", "공격력을 10만큼 올려줍니다.", 10),  # 냥검사 전용 장비
#     "2": Equipment_Item("방울", "공격력을 10만큼 올려줍니다.", 10),  # 냥법사 전용 장비
#     "3": Equipment_Item("새총", "공격력을 10만큼 올려줍니다.", 10),  # 냥궁수 전용 장비
#     "4": Equipment_Item("장난감 막대", "공격력을 10만큼 올려줍니다.", 10)  # 냥힐러 전용 장비
# }
# equipment_items["1"].equip(characters["1"])  # 냥검사에 날카로운 발톱 장착
# equipment_items["2"].equip(characters["2"])  # 냥법사에 날카로운 발톱 장착
# equipment_items["3"].equip(characters["3"])  # 냥궁수에 날카로운 발톱 장착
# equipment_items["4"].equip(characters["4"])  # 냥힐러에 날카로운 발톱 장착

equipment1 = Equipment_Item("날카로운 발톱", "공격력을 10만큼 올려줍니다.", 10)  # 냥검사 전용 아이템
equipment2 = Equipment_Item("방울", "공격력을 10만큼 올려줍니다.", 10)  # 냥법사 전용 아이템
equipment3 = Equipment_Item("새총", "공격력을 10만큼 올려줍니다.", 10)  # 냥궁수 전용 아이템
equipment4 = Equipment_Item("장난감 막대", "공격력을 10만큼 올려줍니다.", 10)  # 냥힐러 전용 아이템


# 물약 사용

# potion_items = {
#     "참치캔": Potion_Item("참치캔", "HP를 20만큼 채워줍니다.", 20, 0, 0),
#     "츄르": Potion_Item("츄르", "MP를 20만큼 채워줍니다.", 0, 20, 0),
#     "북어포": Potion_Item("북어포", "HP를 50만큼 채워줍니다.", 50, 0, 0),
#     "캣닢": Potion_Item("캣", "MP를 50만큼 채워줍니다.", 0, 50, 0)
# }

potion1 = Potion_Item("참치캔", "HP를 20만큼 채워줍니다.", 20, 0, 0)
potion2 = Potion_Item("츄르", "MP를 20만큼 채워줍니다.", 0, 20, 0)
potion3 = Potion_Item("북어포", "HP를 50만큼 채워줍니다.", 50, 0, 0)
potion4 = Potion_Item("캣닢", "MP를 50만큼 채워줍니다.", 0, 50, 0)

total_potions = 0

pet1 = Pet('털뭉치', '방어력을 5만큼 증가시켜줍니다.', 5, 10)
pet2 = Pet('캔디볼', '방어력을 10만큼 증가시켜줍니다.', 10, 15)
pet3 = Pet('도토리볼', '방어력을 15만큼 증가시켜줍니다.', 15, 20)


# 일반배틀 준비
def prebattle():
    battle_character = []
    for i in player_character_list:
        if i.HP != 0:
            battle_character.append(i)

    if len(battle_character) == 0:
        print("싸울 수 있는 고양이가 없습니다. 마을로 돌아갑니다.")
        time.sleep(2)
        town()

    # 일반 던전 몬스터 가중치
    sum_ = 0
    for i in player_character_list:
        sum_ += i.level
    avg_lv = sum_ // 3 + random.randint(1, 5)

    # Monster List - 스텟 조정 필요
    monster_list = [
        Monster("쥐", avg_lv, 100, 40, 20, 20, 7),
        Monster("까치", avg_lv, 100, 40, 20, 20, 7),
        Monster("바퀴벌레", avg_lv, 100, 30, 30, 20, 7),
        Monster("뱀", avg_lv, 100, 40, 20, 20, 7)
    ]

    # 전투에 나올 몬스터
    battle_monster = []

    # 몬스터 뽑기
    for i in range(random.randint(1, 3)):
        battle_monster.append(monster_list.pop(
            random.randint(0, len(monster_list)-1)))

    # 전투 시작
    battle(battle_character, battle_monster)


# 전투
def battle(players, monsters):
    os.system(clear)
    print("길을 걷다 천적을 발견했다!")
    # time.sleep(2)
    print(*monsters, end=" ")
    print("이(가) 튀어나왔다!")
    # time.sleep(2)
    print("가라!", end=" ")
    print(*players, end=" ")
    print(" ")
    # time.sleep(2)

    # 턴 시작 판정
    player_avg_speed = 0
    monster_avg_speed = 0
    for stat in players:
        player_avg_speed += stat.speed
    for stat in monsters:
        monster_avg_speed += stat.speed

    status = ''
    earned_exp = 0

    if player_avg_speed / len(players) >= monster_avg_speed / len(monsters):
        status = 'player turn'
        print("재빠른 고양이들이 선공을 잡았다")
        time.sleep(2)
    else:
        status = 'monster turn'
        print("아뿔싸! 적이 먼저 공격해왔다")
        time.sleep(2)

    # 턴 시작
    while True:
        if status == 'player turn':
            os.system(clear)
            for i in range(len(players)):
                # os.system(clear)
                for k in range(len(players)):
                    # 캐릭터 기본 스테이터스 창
                    print(
                        f"{players[k]} Lv. {players[k].level} HP: ({players[k].HP} / {players[k].max_HP}) MP: ({players[k].MP} / {players[k].max_MP})")

                print("")
                for j in range(len(monsters)):
                    print(
                        f"{monsters[j]} Lv. {monsters[j].level} HP: ({monsters[j].HP} / {monsters[j].max_HP}) MP: ({monsters[j].MP} / {monsters[j].max_MP})")

                print("")
                action = input(
                    f"{players[i]}가 대기중입니다. 어떻게 하시겠습니까? [ 1) 일반공격 2) 스킬:{players[i].skill} 3) 포션 사용 4) 도망친다 ] : ")
                if action.isdigit() == False:
                    print("정수를 입력해주세요.")
                    time.sleep(2)
                #  -- 동작 안함 --
                elif bool(re.search(f"[1-4]", action)) == False:
                    print("잘못 입력했습니다. 다시 시도하세요.")
                    time.sleep(2)
                else:
                    if action == '1':
                        print("어떤 대상을 공격하시겠습니까?  ", end="")
                        print(''.join([f"{x}) {y} " for x, y in enumerate(
                            [x for x in monsters if x.HP != 0], start=1)]))
                        target = input()
                        if target.isdigit() == False:
                            print("정수를 입력해주세요.")
                            # time.sleep(2)
                        elif bool(re.search(f"[1-{len(monsters)}]", target)) == False:
                            print("잘못 입력했습니다. 다시 시도하세요.")
                            # time.sleep(2)
                        else:
                            target_monster = monsters[int(target) - 1]
                            check_ = players[i].normal_attack(target_monster)
                            if check_ == True:
                                earned_exp += int(target_monster.level * 2 * random.randint(
                                    1, 2) + target_monster.max_HP * 1.2 * random.randint(1, 2))
                                target_monster = '기절'
                                cache = []
                                for i in monsters:
                                    if i.HP != 0:
                                        cache.append(i)
                                monsters = cache
                            if len(monsters) == 0:
                                print("승리!")
                                time.sleep(2)
                                # drop_item(earned_exp)
                                players[0].level_up(earned_exp)
                                players[1].level_up(earned_exp)
                                players[2].level_up(earned_exp)
                                town()

                    elif action == '2':
                        print("어떤 대상을 스킬공격하시겠습니까?  ", end="")
                        print(''.join([f"{x}) {y} " for x, y in enumerate(
                            [x for x in monsters if x.HP != 0], start=1)]))
                        target = input()
                        if target.isdigit() == False:
                            print("정수를 입력해주세요.")
                            # time.sleep(2)
                        elif bool(re.search(f"[1-{len(monsters)}]", target)) == False:
                            print("잘못 입력했습니다. 다시 시도하세요.")
                            # time.sleep(2)
                        else:
                            target_monster = monsters[int(target) - 1]
                            skill_find = character_skills[players[i].skill]
                            print(players[i].skill, skill_find)
                            check_ = skill_find(target_monster)
                            if check_ == True:
                                earned_exp += int(target_monster.level * 2 * random.randint(
                                    1, 2) + target_monster.max_HP * 1.2 * random.randint(1, 2))
                                target_monster = '기절'
                                cache = []
                                for i in monsters:
                                    if i.HP != 0:
                                        cache.append(i)
                                monsters = cache

                            if len(monsters) == 0:
                                print("승리!")
                                time.sleep(2)
                                drop_item(earned_exp)
                                # players[0].level_up(earned_exp)
                                # players[1].level_up(earned_exp)
                                # players[2].level_up(earned_exp)
                                # town()

                    elif action == '3':
                        total_potions = potion1.num + potion2.num + potion3.num + potion4.num
                        if total_potions > 0:
                            while True:
                                print(
                                    '================== 현재 소모품 ==================')
                                print(
                                    f'1. 참치캔: {potion1.explanation}|{potion1.num}개')
                                print(
                                    f'2.  츄르 : {potion2.explanation}|{potion2.num}개')
                                print(
                                    f'3. 북어포: {potion3.explanation}|{potion3.num}개')
                                print(
                                    f'4.  캣닢 : {potion4.explanation}|{potion4.num}개')

                                use_potion = input(
                                    '\n사용하실 소매품의 번호를 하나만 입력해주세요:')

                                if use_potion == '1':
                                    if bool(potion1.num) == False:
                                        print('\n현재 소유하고 계신 참치캔이 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        continue
                                    else:
                                        potion1.take_potion_hp(players[i])
                                        break

                                if use_potion == '2':
                                    if bool(potion2.num) == False:
                                        print('현재 소유하고 계신 츄르가 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        continue
                                    else:
                                        potion2.take_potion_mp(players[i])
                                        break

                                if use_potion == '3':
                                    if bool(potion3.num) == False:
                                        print('현재 소유하고 계신 북어포가 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        continue
                                    else:
                                        potion3.take_potion_hp(players[i])
                                        break

                                if use_potion == '4':
                                    if bool(potion4.num) == False:
                                        print('현재 소유하고 계신 캣닢이 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        continue
                                    else:
                                        potion4.take_potion_mp(players[i])
                                        break
                        else:
                            print('현재 소유하신 소모품이 없습니다!')

                    elif action == '4':
                        # 각 고양이의 속도에 따라 탈출할 확률 다름
                        if players[i].speed * (1 + random.randint(1, 10) / 10) > monster_avg_speed:
                            os.system(clear)
                            print("탈출에 성공했습니다.")
                            time.sleep(2)
                            print("마을로 돌아갑니다.")
                            time.sleep(2)
                            town()

            status = 'monster turn'

        elif status == 'monster turn':
            for j in range(len(monsters)):
                os.system(clear)

                targeted_player = random.randint(0, len(players) - 1)
                check_ = monsters[j].normal_attack(players[targeted_player])
                if check_ == True:
                    players[targeted_player] = '기절'
                    cache = []
                    for i in players:
                        if i == 0:
                            cache.append(i)
                    players = cache

                if len(players) == 0:
                    print("패배...")
                    time.sleep(2)
                    lose()

            status = 'player turn'


# 보스배틀 준비
def prebossbattle():
    battle_character = []
    for i in player_character_list:
        if i.HP != 0:
            battle_character.append(i)

    # 고양이 셋 다 기절해 있다면
    if len(battle_character) == 0:
        print("싸울 수 있는 고양이가 없습니다. 마을로 돌아갑니다.")
        time.sleep(2)
        town()

    # 고양이 셋 중 하나라도 기절해 있으면 의사 물어보기
    if len(battle_character) != len(player_character_list):
        question = input(
            "고양이들 중에 싸울 수 없는 고양이가 있는 것 같아요. 그래도 싸우시겠습니까? [ 1) 네 2) 마을로 돌아갈래요 ]")
        if question == '1':
            print("좋은 자신감이에요")
            time.sleep(2)
        else:
            town()

    # 나올 보스
    if boss_clear[0] == 0:
        battle_monster = [bosses[0]]
    elif boss_clear[0] == 1:
        battle_monster = [bosses[1], bosses[2]]
    elif boss_clear[0] == 2:
        battle_monster = [bosses[3]]

    # 전투 시작
    battle(battle_character, battle_monster)


def drop_item(exp):
    os.system(clear)

    # 경험치 획득
    print(f"고양이들은 각각 {exp}의 경험치를 얻었다.")
    for i in player_character_list:
        i.exp += exp
        if i.exp >= i.max_exp:
            i.level += 1
            i.exp = i.exp - i.max_exp
            i.max_exp = int((i.max_exp) * 1.03)
            print(f"{i}가 {i.level}로 레벨업했다!")
            time.sleep(1)

    print(" ")

    # 소지금 획득
    earned_money = int(exp * round(random.random(), 2))
    player_money[0] += earned_money
    print(f"{earned_money}$를 획득했습니다.")
    print("")
    input("\t 마을로 돌아가려면 아무 키나 누르세요.")
    print("")
    os.system(clear)
    town()

    # 보상 획득
    # earn_random = input("보상을 획득하자! 1, 2, 3중에 숫자를 고르세요 : ")
    # if earn_random.isdigit() == False:
    #     print("정수를 입력해주세요.")
    #     time.sleep(2)
    # elif bool(re.search(f"[1-3]", earn_random)) == False:
    #     print("잘못 입력했습니다. 다시 시도하세요.")
    #     time.sleep(2)
    # else:
    #     if earn_random == random.randint(1, 3):
    #         pass


def lose():
    pass


# 마을
def town():

    # 마을에서 행동 리스트
    town_action = {
        '1': prebattle,
        '2': prebossbattle,
        '3': inn,
        '4': buy_item
    }

    while True:
        # os.system(clear)
        for i in range(len(player_character_list)):
            print(
                f"{player_character_list[i]} Lv. {player_character_list[i].level} HP: ({player_character_list[i].HP} / {player_character_list[i].max_HP}) MP: ({player_character_list[i].MP} / {player_character_list[i].max_MP})")
        print(f"소지금: {player_money[0]}$")
        action = input("어디로 갈까요? [ 1)길거리 2)높은 탑 3)여관 4)상점 ] : ")
        if action.isdigit() == False:
            print("정수를 입력해주세요.")
            time.sleep(2)
        elif bool(re.search(f"[1-{len(town_action)}]", action)) == False:
            print("잘못 입력했습니다. 다시 시도하세요.")
            time.sleep(2)
        else:
            town_action[str(action)]()


def inn():
    inn_action = {
        '1': recovery_in_inn,
        '2': town
    }
    while True:
        os.system(clear)
        print("어서오세요~고양이 카페입니다. 쉬고 가실건가요?")
        time.sleep(1)
        print("요금은 30$입니다")
        time.sleep(1)
        print(f"소지금: {player_money[0]}$")
        action = input("1)쉬기 2)돌아가기 : ")
        if action.isdigit() == False:
            print("정수를 입력해주세요.")
            time.sleep(1)
        elif bool(re.search(f"[1-{len(inn_action)}]", action)) == False:
            print("잘못 입력했습니다. 다시 시도하세요.")
            time.sleep(1)
        elif player_money[0] < 30:
            print("돈도 없는 주제에. 저리 꺼져")
            time.sleep(2)
            print("마을로 돌아갑니다")
            time.sleep(2)
            town()
        else:
            inn_action[str(action)]()


def recovery_in_inn():

    player_money[0] -= 30

    for i in player_character_list:
        i.HP = i.max_HP
        i.MP = i.max_MP

    print("고양이 카페에서 푹 쉬었더니 고양이들의 체력이 회복되었습니다")
    time.sleep(3)
    print("마을로 돌아갑니다")
    time.sleep(3)

    town()

# store - 양예린

# 소모품/아이템 클래스에 가격을 인자로 넣어주는 것도 괜찮을거같아요..price
# 소모품은 hp,mp 상승
# 장비는 일단 공격력상승 이니까
# 펫?같은거를 만들어서 돈을 더 얻는다거나 / 방어력 상승?


# potion_items = {
#     "참치캔": Potion_Item("참치캔", "HP를 20만큼 채워줍니다.", 20, 0,0),
#     "츄르": Potion_Item("츄르", "MP를 20만큼 채워줍니다.", 0, 20, 0),
#     "북어포": Potion_Item("북어포", "HP를 50만큼 채워줍니다.", 50, 0, 0),
#     "캣닢": Potion_Item("캣", "MP를 50만큼 채워줍니다.", 0, 50, 0)
# }

# 금액제한


def buy_item():
    os.system(clear)
    print('    어서오세요! 냥냥상점입니다.*^^*')
    print('======================================')
    if player_money[0] >= 30:
        while True:
            print('\n구매하실 물건을 선택해주세요.')
            choice = input('<소모품: 1> <장비: 2> < 귀여운 pet : 3>\n:')
            if choice == '1':
                print('================메뉴판================')
                print(' 참치캔: HP를 20만큼 채워줍니다.| $10')
                print('  츄르 : MP를 20만큼 채워줍니다.| $10')
                print(' 북어포: HP를 50만큼 채워줍니다.| $25')
                print('  캣닢 : MP를 50만큼 채워줍니다.| $25')

                while True:
                    choice_potion = input('1) 참치캔 | 2) 츄르 | 3) 북어포 | 4) 캣닢\n:')
                    if choice_potion == '1':
                        print('참치캔을 구입하셨습니다!')
                        potion1.num += 1
                        player_money[0] -= 10  # potion1.price
                        break

                    elif choice_potion == '2':
                        print('츄르를 구입하셨습니다!')
                        potion2.num += 1
                        player_money[0] -= 10  # potion2.price
                        break

                    elif choice_potion == '3':
                        print('북어포을 구입하셨습니다!')
                        potion3.num += 1
                        player_money[0] -= 25  # potion3.price
                        break

                    elif choice_potion == '4':
                        print('캣닢을 구입하셨습니다!')
                        potion4.num += 1
                        player_money[0] -= 25  # potion4.price
                        break

                    else:
                        print('1, 2, 3, 4 중에 선택해주십시오.')
                        continue

            elif choice == '2':
                print('장비 구매를 원하시는군요!')
                print('장비 구매의 가격은 $30 입니다.')
                browse_equipment = {
                    "냥검사": equipment1.equip,
                    "냥법사": equipment2.equip,
                    "냥궁수": equipment3.equip,
                    "냥힐러": equipment4.equip
                }

                choice_equipment = input('구매하시겠습니까? y/n로 선택해주세요!\n:')

                if choice_equipment == 'y':
                    for i in range(len(player_character_list)):
                        if bool(player_character_list[i].eq) == False:
                            print(f'{player_character_list[i]}', end=' ')
                    print(' 의 장비를 구매하실 수 있습니다.')

                    select = input("1,2,3:")
                    if select == '1':
                        browse_equipment[player_character_list[0].name](
                            player_character_list[0])
                    elif select == '2':
                        browse_equipment[player_character_list[1].name](
                            player_character_list[1])
                    elif select == '3':
                        browse_equipment[player_character_list[2].name](
                            player_character_list[2])

                elif choice_equipment == 'n':
                    continue
                else:
                    print('y/n로 선택해주세요!')
                    break

            elif choice == '3':
                print("\n귀여운 pet 구매를 원하시는군요! 탁월한 선택이십니다.^^")
                print('==================소개판==================')
                print(' 털뭉치 : 방어력을 5만큼 증가시켜줍니다.| $10')
                print(' 캔디볼 : 방어력을 10만큼 증가시켜줍니다| $15')
                print('도토리볼: 방어력을 15만큼 증가시켜줍니다| $20')

                while True:
                    choice_pet = input('1) 털뭉치 | 2) pet2 | 3) pet3 \n:')
                    if choice_pet == '1':
                        print('털뭉치를 구입하셨습니다!')
                        pet1.upgrade_defense(player_character_list[0])
                        pet1.upgrade_defense(player_character_list[1])
                        pet1.upgrade_defense(player_character_list[2])
                        print(f'털뭉치가 모두의 방어력을 5만큼 증가시켰습니다!')

                        player_money[0] -= pet1.price
                        break

                    elif choice_pet == '2':
                        print('캔디볼을 구입하셨습니다!')
                        pet2.upgrade_defense(player_character_list[0])
                        pet2.upgrade_defense(player_character_list[1])
                        pet2.upgrade_defense(player_character_list[2])
                        print(f'캔디볼이 모두의 방어력을 10만큼 증가시켰습니다!')

                        player_money[0] -= pet2.price
                        break

                    elif choice_pet == '3':
                        print('도토리볼을 구입하셨습니다!')
                        pet3.upgrade_defense(player_character_list[0])
                        pet3.upgrade_defense(player_character_list[1])
                        pet3.upgrade_defense(player_character_list[2])
                        print(f'도토리볼이 모두의 방어력을 15만큼 증가시켰습니다!')

                        player_money[0] -= pet3.price
                        break

                    else:
                        print('\n1, 2, 3 중에 선택해주십시오.')
                        continue

            else:
                print('\n1, 2, 3 중에 선택해주세요!!')
                continue

            print(f'남은 소지금은{player_money[0]}원 입니다!')

            if player_money[0] == 0:
                print('가지고 계신 소지금을 모두 사용하셨습니다!\n다음에 또 만나요~')
                time.sleep(3)
                print("마을로 돌아갑니다")
                time.sleep(3)
                town()

            elif player_money[0] < 10:
                print('아쉽지만 더이상 구매하실 수 있는 물건이 없습니다!\n다음에 또 만나요~')
                time.sleep(3)
                print("마을로 돌아갑니다")
                time.sleep(3)
                town()

            buy_again = input('구매를 계속 진행하시겠습니까?\n y/n로 선택해주세요:')

            if buy_again == 'y':
                continue
            elif buy_again == 'n':
                print('구매를 종료합니다. 저희 냥냥상점을 찾아주셔서 감사합니다!\n다음에 또 만나요~')
                time.sleep(3)
                print("마을로 돌아갑니다")
                time.sleep(3)
                town()

    else:
        print(
            f'현재 소지금이 {player_money[0]}$ 이시군요! 30$ 이상부터 냥냥상점을 이용하실 수 있습니다.\n 아쉽지만 다음에 만나요~')
        time.sleep(3)
        print("마을로 돌아갑니다")
        time.sleep(3)
        town()


"""메인 시작"""
# Character List
# character = {
#     '1': Character("냥검사", 1, 150, 30, 15, 20, 13),
#     '2': Character("냥법사", 1, 120, 50, 12, 13, 10),
#     '3': Character("냥궁수", 1, 100, 40, 18, 10, 18),
#     '4': Character("냥힐러", 1, 140, 50, 9, 16, 14)
# }
player_character_list = []

# 플레이어 돈
player_money = [1000]

# 보스 clear 확인
boss_clear = [0]

# System check
os_check = platform.system()
clear = ''
if os_check == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'


# 인트로 부분
os.system(clear)
print("==========================")
time.sleep(1)
print("====== 고양이 게임 =======")
time.sleep(1)
print("==========================")
time.sleep(1)
print("")
time.sleep(1)

# 캐릭터 선택(3 마리)
while len(player_character_list) < 4:
    os.system(clear)
    print("간택 받고 싶은 고양이 세마리를 골라주세요!(현재:", end=" ")
    print(*player_character_list, end=" ")
    print(")")
    select = input("1)냥검사 2)냥법사 3)냥궁수 4)냥힐러 : ")
    if select.isdigit() == False:
        print("정수를 입력해주세요.")
        time.sleep(1)
    elif bool(re.search("[1-4]", select)) == False:
        print("잘못 입력했습니다. 다시 시도하세요.")
        time.sleep(1)
    elif characters[select] in player_character_list:
        print(f"이미 {characters[select]}에게 간택 받았습니다.")
        time.sleep(1)
    else:
        player_character_list.append(characters[select])

        # 3 마리가 다 채워졌다면 break
        if len(player_character_list) == 3:
            break


os.system(clear)
print("당신은", end=" ")
print(*player_character_list, end="")
print("를 선택했습니다. 이제 모험을 떠나볼까요.")
# time.sleep(4)


# Story #1. 길 걷기
os.system(clear)
print("여행을 떠난 당신은 길을 걷다 한 마을에 도착했습니다.")
# time.sleep(2)

print("마을을 한번 둘러볼까요.")
# time.sleep(2)

# 어떤 행동 끝나면 마을
run = 0
while run < 3:
    town()
    run += 1
