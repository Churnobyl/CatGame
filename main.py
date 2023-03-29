import os
import platform
import random
import re
import time

# 레벨업마다 전체스탯이 오르는 함수입니다. 15퍼센트씩(15.0) 오르는 것으로 임의 조정해놨습니다.. 오류.. 뜰지도 모르겠습니다... :>...
def sh_state_up(a):
    return int(a * (1.0 + 15.0 / 100.0))

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
        
    # 
    # 일반공격_플레이어_몬스터_전부사용 / 공격력비례 랜덤값 
    def normal_attack(self, monster):
        damage = random.randint(int(self.attack * 0.8), int(self.attack * 1.2))
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        time.sleep(2)
        if monster.HP == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
    
    
    # 특수공격_냥검사 / 마나값, 공격값은 공격력비례 임의의 랜덤(기본 ~ +50%)값으로 주었습니다
    def dealing_Skill(self, monster):
        self.MP = max(self.MP -30, 0)
        if self.mp == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        damage = random.randint(self.attack, int(self.attack* 1.5))
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.hp == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False
    

    # 특수공격_냥법사 / 마나값, 디벞값은 방어력비례 임의의 랜덤(기본 ~ +30%)값으로 주었습니다
    def debuff_Skill(self, monster):
        self.MP = max(self.MP -40, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        debuff = random.randint(self.defense, int(self.defense * 1.3))
        monster.defense = max(monster.defense - debuff, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}의 방어력을 {debuff}만큼 깎았습니다.")
        if monster.hp == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False
    

    # 특수공격_냥궁수 / 마나값, 공격값은 스피드비례 임의의 랜덤(기본 ~ +50%)값으로 주었습니다
    def shooting_Skill(self, monster):
        self.MP = max(self.MP -30, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        damage = random.randint(self.speed, int(self.speed * 1.5))
        monster.HP = max(monster.HP - damage, 0)
        print(f"{self.name}의 {self.skill}! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        if monster.hp == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False
            
    
    # 특수공격_냥힐러 / 마나값, 힐링값 임의로 주었습니다 / 전체회복일지.. 특정캐릭 회복일지.. 정해봅시덩.. 지금은 본인 회복만 가능하게 되어있어서..
    def healing_Skill(self, monster):
        self.MP = max(self.MP -50, 0)
        if self.MP == 0:
            print("보유 중인 MP가 모자랍니다! 스킬을 사용할 수 없습니다!")
            return
        healing = max(self.HP+int(self.HP*0.3), self.max_HP)
        print(f"{self.name}의 {self.skill}! {self.name}의 HP를 {healing}만큼 회복했습니다.")
        if monster.hp == 0:
            print(f"{monster.name}(이)가 쓰러졌습니다.")
            time.sleep(2)
            return True
        else:
            return False

    # 상속용 스테이터스였는데..제가 써놓고도 잘 모르겟습니다 죄송함다 
    def status(self):
        print(f"{self.name} LV.{self.level} : HP {self.HP}/{self.max_HP} | MP {self.MP}/{self.max_MP}")
        
        # 중간보스, 최종보스는 스테이터스에 마나상태 나와야할 것 같긴한데 잡몹하고 어떻게 구분할지 모르겠어서 일단 주석처리하겠습니당
        # print(f"{monster.name}의 상태: HP {self.HP}/{self.max_HP} | MP {self.MP}/{self.max_HP}") 
    
    
    # 클래스 호출 시 문자열 출력
    def __str__(self):
        if self.HP == 0:
            return "기절"
        else:
            return self.name
        
   
class Character(Object): 
    def __init__(self, name, level, HP, MP, attack, defense, speed, eq='', exp=0) -> None:
        super().__init__(name, level, HP, MP, attack, defense, speed)
        self.exp = exp
        self.max_exp = 100
        self.eq = eq
 
    def status(self):
        print(f"{self.name} LV.{self.level} : EXP {self.exp}/{self.max_exp}\n   HP {self.HP}/{self.max_HP} | MP {self.MP}/{self.max_MP}")
    
    # sh개인메모,, 레벨오를때마다 self.exp의 초기화와 max_exp의 값이올라야함,, 또는 self.max_exp의 값만 올라가게 만들어서 같아질 때 마다 레벨업하기.. 이거는 경험치수급량 보면서 min or max랑 섞어써야할듯
    def Level_up(self):
        if self.exp >= self.max_exp:
            self.level+1
            print(f'{self.name}가 LV.{self.level}로 레벨업했습니다!')
            
        
    def level_plus1(self):
        self.max_HP = sh_state_up(self.max_HP)
        self.HP = sh_state_up(self.HP)
        self.max_MP = sh_state_up(self.max_MP)
        self.MP = sh_state_up(self.MP)
        self.attack = sh_state_up(self.attack)
        self.defense = sh_state_up(self.defense)
        self.speed = sh_state_up(self.speed)


class Monster(Object):
    def __init__(self, name, level, HP, MP, attack, defense, speed) -> None:
        super().__init__(name, level, HP, MP, attack, defense, speed)
        weight = round(level / 100, 2) # 레벨/100배 증가
        self.HP = int(HP * (1 + weight))
        self.max_HP = int(HP * (1 + weight))
        self.MP = int(MP * (1 + weight))
        self.max_MP = int(MP * (1 + weight))
        self.attack = int(attack * (1 + weight))
        self.defense = int(defense * (1 + weight))
        self.speed = int(speed * (1 + weight))
    
    
        
        
        
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
        player.attack += self.attack_effect
        print(f"{player.name}의 공격력이 {self.attack_effect}만큼 증가했습니다.")
    

        
class Potion_Item(Item):
    def __init__(self, name, explanation, hp_effect, mp_effect):
        super().__init__(name, explanation)        
        self.hp_effect = hp_effect       
        self.mp_effect = mp_effect

    def take_potion(self, player):
        player.HP += self.hp_effect
        print(f"{player.HP}가 {self.hp_effect}만큼 회복됐습니다.")
        player.MP += self.mp_effect
        print(f"{player.MP}가 {self.mp_effect}만큼 회복됐습니다.")

    # def take_potion(self, obj):
    #     if isinstance(obj, Object):
    #         obj.HP += self.hp_effect
    #         print(f"{obj.name}의 HP가 {self.hp_effect}만큼 회복됐습니다.")
    #         obj.MP += self.mp_effect
    #         print(f"{obj.name}의 MP가 {self.mp_effect}만큼 회복됐습니다.")
    #     else:
    #         print("잘못된 입력입니다.")

## 장비 아이템이랑 물약 아이템이 겹치는 게 있으니 Item이라는 클래스 두고 Equipment_Item, Potion_Item가 상속하는 건 어때요
## 

# character = {
#     '1' : Character("냥검사", 1, 150, 30, 15, 20, 13),
#     '2' : Character("냥법사", 1, 120, 50, 12, 13, 10),
#     '3' : Character("냥궁수", 1, 100, 40, 18, 10, 18),
#     '4' : Character("냥힐러", 1, 140, 50, 9, 16, 14)
# }


player = Character("냥검사", 1, 150, 30, 15, 20, 13)
player = Character("냥법사", 1, 120, 50, 12, 13, 10)
player = Character("냥궁수", 1, 100, 40, 18, 10, 18)
player = Character("냥힐러", 1, 140, 50, 9, 16, 14)


 
# 장비 아이템 장착
equipment = Equipment_Item("날카로운 발톱", "공격력을 10만큼 올려줍니다.", 10) #냥검사 전용 아이템
equipment = Equipment_Item("방울", "공격력을 10만큼 올려줍니다.", 10) #냥법사 전용 아이템
equipment = Equipment_Item("새총", "공격력을 10만큼 올려줍니다.", 10) #냥궁수 전용 아이템
equipment = Equipment_Item("장난감 막대", "공격력을 10만큼 올려줍니다.", 10) #냥힐러 전용 아이템
equipment.equip(player)

    
# 물약 사용
potion = Potion_Item("참치캔", "HP를 20만큼 채워줍니다.", 20, 0)
potion = Potion_Item("츄르", "MP를 20만큼 채워줍니다.", 0, 20)
potion = Potion_Item("북어포", "HP를 50만큼 채워줍니다.", 50, 0)
potion = Potion_Item("털실뭉치", "MP를 50만큼 채워줍니다.", 0, 50)
potion.take_potion(player)





# 일반 던전 배틀 전
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
    rand = round(random.randint(9, 12) / 10, 1)
    sum_ = 0
    for i in player_character_list:
        sum_ += i.level
    avg_lv = sum_ // 3 + random.randint(1,5)
    
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
    for i in range(random.randint(1,3)): # 1~3마리
        battle_monster.append(random.choice(monster_list))
    
    # 전투 시작
    battle(battle_character, battle_monster)

# 전투
def battle(players, monsters):
    os.system(clear)
    print("길을 걷다 천적을 발견했다!")
    time.sleep(2)
    print(*monsters, end=" ")
    print("이(가) 튀어나왔다!")
    time.sleep(2)
    print("가라!", end=" ")
    print(*players, end=" ")
    print(" ")
    time.sleep(2)
    
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
                os.system(clear)
                for k in range(len(players)):
                    print(
                        f"{players[k]} Lv. {players[k].level} HP: ({players[k].HP} / {players[k].max_HP}) MP: ({players[k].MP} / {players[k].max_MP})")
                    
                print("")
                for j in range(len(monsters)):
                    print(
                        f"{monsters[j]} Lv. {monsters[j].level} HP: ({monsters[j].HP} / {monsters[j].max_HP}) MP: ({monsters[j].MP} / {monsters[j].max_MP})")
                
                print("")
                action = input(f"{players[i]}가 대기중입니다. 어떻게 하시겠습니까? [ 1) 일반공격 2) 스킬 3) 포션 사용 4) 도망친다 ] : ")
                if action.isdigit() == False:
                    print("정수를 입력해주세요.")
                    time.sleep(2)
                elif bool(re.search(f"[1-4]", action)) == False:
                    print("잘못 입력했습니다. 다시 시도하세요.")
                    time.sleep(2)
                else:
                    if action == '1':
                        print("어떤 대상을 공격하시겠습니까?  ", end="")
                        print(''.join([f"{x}) {y} " for x, y in enumerate([x for x in monsters if x.HP != 0], start=1)]))
                        target = input()
                        if target.isdigit() == False:
                            print("정수를 입력해주세요.")
                            time.sleep(2)
                        elif bool(re.search(f"[1-{len(monsters)}]", target)) == False:
                            print("잘못 입력했습니다. 다시 시도하세요.")
                            time.sleep(2)
                        else:
                            targeted_monster = monsters[int(target) - 1]
                            check_ = players[i].normal_attack(targeted_monster)
                            if check_ == True:
                                earned_exp += int(targeted_monster.level * 2 * random.randint(1, 2) + targeted_monster.max_HP * 1.2 * random.randint(1, 2))
                                targeted_monster = '기절'
                                
                                cache = []
                                for i in monsters:
                                    if i.HP == 0:
                                        cache.append(i)
                                monsters = cache
                                
                                
                            
                            if len(monsters) == 0:
                                print("승리!")
                                time.sleep(2)
                                drop_item(earned_exp)
            
                                
                    elif action == 2:
                        pass
                    elif action == 3:
                        pass
                    elif action == 4:
                        # 각 고양이의 속도에 따라 탈출할 확률 다름
                        if players[i].speed * (1 + random.randint(1, 10)/ 10) > monster_avg_speed:
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
                
                targeted_player = random.randint(0,len(players) - 1)
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
                
            
               

def preboss_battle():
    pass
        
        
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
    
    # 보상 획득
    earn_random = input("보상을 획득하자! 1, 2, 3중에 숫자를 고르세요 : ")
    if earn_random.isdigit() == False:
        print("정수를 입력해주세요.")
        time.sleep(2)
    elif bool(re.search(f"[1-3]", earn_random)) == False:
        print("잘못 입력했습니다. 다시 시도하세요.")
        time.sleep(2)
    else:
        if earn_random == random.randint(1, 3):
            pass
    

def lose():
    pass
    
        
        
# 마을
def town():

    # 마을에서 행동 리스트
    town_action = {
        '1': prebattle,
        '2': preboss_battle,
        '3': inn,
        '4': buy_item
    }

    while True:
        os.system(clear)
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

class Pet(Item):
    def __init__(self, name, explanation,defense,price): 
        super().__init__(name, explanation)
        self.defense = defense
        self.price = price
        
    def upgrade_defense(self,other):
        other.defense += self.defense
        print(f'귀여운 {self.name}이 {other.name}의 방어력을 {self.defense}만큼 증가시켰습니다!' )
        
    #def upgrade_money():

pet1 = Pet('털뭉치','방어력을 5만큼 증가시켜줍니다.',5 ,10) 
pet2 = Pet('pet2','방어력을 10만큼 증가시켜줍니다.',10, 15) 
pet3 = Pet('pet3','방어력을 15만큼 증가시켜줍니다.',15, 20)    

# 금액제한

def buy_item():
    os.system(clear)
    print('    어서오세요! 냥냥상점입니다.*^^*')
    print('======================================')
    while player_money[0] >= 30:
        print('구매하실 물건을 선택해주세요!')
        choice = input('<소모품: 1> <장비: 2> < 귀여운 pet : 3>\n:')
        if choice == '1':
            print('================메뉴판================')
            print(' 참치캔: HP를 20만큼 채워줍니다.| $10')
            print('  츄르 : MP를 20만큼 채워줍니다.| $10')
            print(' 북어포: HP를 50만큼 채워줍니다.| $25')
            print('  캣닢 : MP를 50만큼 채워줍니다.| $25') # 이거 캣닢이나 모래로 바꿔도 될까요,,? 펫으로 털뭉치 쓰고싶어요ㅜㅜ>캣닢으로 바꿨어요 와 감사합니닿ㅎ
            
            choice_potion = input('1) 참치캔 | 2) 츄르 | 3) 북어포 | 4) 캣닢\n:')
            
            if choice_potion == '1':
                print('참치캔을 구입하셨습니다!')
                #potion1.take_potion(player)
                player_money[0] -= 10 #potion1.price 
                
            elif choice_potion == '2':
                print('츄르를 구입하셨습니다!')
                #potion2.take_potion(player)
                player_money[0] -= 10 #potion2.price
                
            elif choice_potion == '3':
                print('북어포을 구입하셨습니다!')
                #potion3.take_potion(player)
                player_money[0] -= 25 #potion3.price
                
            elif choice_potion == '4': 
                print('캣닢을 구입하셨습니다!')
                #potion4.take_potion(player)
                player_money[0] -= 25 #potion4.price
                   
            else:
                print('1, 2, 3, 4 중에 선택해주십시오.') 
                # 다시 바깥if문으로..
                         
        elif choice == '2':
            print('장비 구매를 원하시는군요!')
            print('장비 구매의 가격은 $30 입니다.')
            
            choice_equipment = input('구매하시겠습니까? y/n로 선택해주세요!\n:')
            
            if choice_equipment == 'y':
                player.attack += 10
                print(f"{player.name}의 공격력이 10만큼 증가했습니다.")
                
            elif choice_equipment == 'n':
                continue
            
            else:
                print('y/n로 선택해주세요!')
                # 다시 바깥if문으로..
            
        elif choice == '3':
            print("귀여운 pet 구매를 원하시는군요! 탁월한 선택이십니다.^^")
            print('==================소개판==================')
            print('털뭉치: 방어력을 5만큼 증가시켜줍니다.| $10')
            print(' pet2 : 방어력을 10만큼 증가시켜줍니다| $15')
            print(' pet3 : 방어력을 15만큼 증가시켜줍니다| $20')
            
            choice_pet = input('1) 털뭉치 | 2) pet2 | 3) pet3 \n:')
            
            if choice_pet == '1':
                print('털뭉치를 구입하셨습니다!')
                pet1.upgrade_defense(player)
                player_money[0] -= pet1.price
                
            elif choice_pet == '2':
                print('pet2를 구입하셨습니다!')
                pet2.upgrade_defense(player)
                player_money[0] -= pet2.price
                
            elif choice_pet == '3':
                print('pet3을 구입하셨습니다!')
                pet3.upgrade_defense(player)
                player_money[0] -= pet3.price
                   
            else:
                print('1, 2, 3 중에 선택해주십시오.') 
                # 다시 바깥if문으로..
            
        else :
            print('1, 2, 3 중에 선택해주세요!!')
            continue
        
        print(f'{character.name}님의 남은 소지금은{player_money[0]}원 입니다!')
        
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
        
        buy_again = input('구매를 계속 진행하시겠습니까?\n y/n로 선택해주세요!')
        
        if buy_again == 'y':
            continue
        elif buy_again == 'n':    
            print('구매를 종료합니다. 저희 냥냥상점을 찾아주셔서 감사합니다!\n다음에 또 만나요~') 
            time.sleep(3)
            print("마을로 돌아갑니다")
            time.sleep(3)
            town()
            
    print(f'현재 소지금이 ${player_money[0]}이시군요! $30 이상부터 냥냥상점을 이용하실 수 있습니다.\n 아쉽지만 다음에 만나요~')        
    time.sleep(3)
    print("마을로 돌아갑니다")
    time.sleep(3)
    town()
    

"""메인 시작"""

# Character List
character = {
    '1' : Character("냥검사", 1, 150, 30, 15, 20, 13),
    '2' : Character("냥법사", 1, 120, 50, 12, 13, 10),
    '3' : Character("냥궁수", 1, 100, 40, 18, 10, 18),
    '4' : Character("냥힐러", 1, 140, 50, 9, 16, 14)
}

player_character_list = []

# 플레이어 돈
player_money = [1000]

# System check
os_check = platform.system()
clear = ''
if os_check == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'



# Game Start
os.system(clear)
print("==========================")
time.sleep(1)
print("====== 고양이 게임 ========")
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
    elif character[select] in player_character_list:
        print(f"이미 {character[select]}에게 간택 받았습니다.")
        time.sleep(1)
    else:
        player_character_list.append(character[select])

        # 3 마리가 다 채워졌다면 break
        if len(player_character_list) == 3:
            break
    

os.system(clear)
print("당신은", end=" ")
print(*player_character_list, end="")
print("를 선택했습니다. 이제 모험을 떠나볼까요.")
time.sleep(4)


# Story #1. 길 걷기
os.system(clear)
print("여행을 떠난 당신은 길을 걷다 한 마을에 도착했습니다.")
time.sleep(2)

print("마을을 한번 둘러볼까요.")
time.sleep(2)

# 어떤 행동 끝나면 마을
run = 0
while run < 3:
    town()
    run += 1










        
            

        

    