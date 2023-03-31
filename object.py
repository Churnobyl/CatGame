import time
import random

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

    def normal_attack(self, other):
        first_damage = random.randint(
            int(self.attack * 0.7), int(self.attack * 1.2))
        damage = max(first_damage - int(other.defense * 0.4), 0)
        other.HP = max(other.HP - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        # time.sleep(2)
        if other.HP == 0:
            print(f"{other.name}(이)가 쓰러졌습니다.")
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
        self.faint = False

    # 특수공격_냥검사 / 마나값 임의 / 공격값은 공격력비례 임의의 랜덤(기본 ~ +50%)값 - 몬스터의 방어력비례(30퍼) / 임의값입니다

    def dealing_Skill(self, monster):
        self.MP = max(self.MP - 30, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        first_damage = random.randint(self.attack, int(self.attack * 1.5))
        damage = max(first_damage - int(monster.defense * 0.3), 0)
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
        damage = max(first_damage - int(monster.defense * 0.3), 0)
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 특수공격_냥힐러 / 마나값, 힐링값 임의로 주었습니다 / 지금 print 문이.. self.name이 시전하면서 self.name이 회복하는거라.. 이게 자힐로 들어가는 방법밖에.. 어떡할가여.. :>?

    def healing_Skill(self, friend):
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

    def level_plus1(self):
        self.max_HP = sh_state_up(self.max_HP)
        self.HP = sh_state_up(self.HP)
        self.max_MP = sh_state_up(self.max_MP)
        self.MP = sh_state_up(self.MP)
        self.attack = sh_state_up(self.attack)
        self.defense = sh_state_up(self.defense)
        self.speed = sh_state_up(self.speed)

    # exp의 값이 max_exp의 값과 같거나 넘칠 때 레벨업과 레벨업 print 출력, exp값 유지하는 대신 max_exp의 값만 비례값으로 올라갑니다.
    # 전투 종료시 경험치 드랍과 함께 매번 추가해주시는 함수와 같다고 생각해주시면 될 것 같습니다.

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
        return

#   캐릭터 전투시작 & 디폴트 스테이터스 창
    def status(self):
        return f"{self.name} LV. {self.level} || HP: ({self.HP} / {self.max_HP}) || MP: ({self.MP} / {self.max_MP})"

#   캐릭터 올 스테이터스 창
    def all_status(self):
        return f"{self.name} LV. {self.level} || EXP: ({self.exp} / {self.max_exp}) || HP: ({self.HP} / {self.max_HP}) || MP: ({self.MP} / {self.max_MP})\n   ATK: {self.attack} || DEF: {self.defense} || SPD: {self.speed} || 장비 : {self.eq} "


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
        damage = max(first_damage - int(monster.defense * 0.3), 0)
        monster.HP = max(monster.HP - damage, 0)
        print(
            f"{self.name}의 {self.skill}! 고양이를 박스로 후리다니! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
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
        damage = max(first_damage - int(monster.defense * 0.3), 0)
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
        damage = max(first_damage - int(monster.defense * 0.3), 0)
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
