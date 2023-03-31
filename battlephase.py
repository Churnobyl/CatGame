from object import *
from utility import *
from items import *
import time
import random

#                 LV  HP  MP  ATK  DEF  SPD
bosses = [
    Boss("슈뢰딩거", 15, 2000, 0, 150, 100, 300, "상 자식"),
    Boss("잼민이", 20, 1300, 0, 120, 100, 400, "돌 던지기"),
    Boss("잼순이", 20, 1300, 0, 180, 100, 400, "꼬리 당기기"),
    Boss("제리", 25, 2300, 0, 200, 130, 400, "볼링쇼")
]

# 여기에 보스 스킬명 따로 필요 없나요? - 세희
bosses_skills = [
    bosses[0].box_shot,
    bosses[1].boss_attack,
    bosses[2].boss_attack,
    bosses[3].jerry_attack
]

# 일반배틀 준비


def prebattle(character_list, money, character_skills):
    battle_character = []
    for i in character_list:
        if i.HP != 0:
            battle_character.append(i)

    if len(battle_character) == 0:
        print("싸울 수 있는 고양이가 없습니다. 마을로 돌아갑니다.")
        time.sleep(2)
        return 'town', money

    # 일반 던전 몬스터 가중치
    sum_ = 0
    for i in character_list:
        sum_ += i.level
    avg_lv = sum_ // 3 + random.randint(1, 3)

    # Monster List        HP / MP / ATK / DEF / SPD
    monster_list = [
        Monster("쥐", avg_lv, 70, 0, 13, 15, 10),
        Monster("까치", avg_lv, 100, 0, 18, 18, 7),
        Monster("바퀴벌레", avg_lv, 110, 0, 15, 30, 12),
        Monster("뱀", avg_lv, 80, 0, 20, 20, 10)
    ]

    # 전투에 나올 몬스터
    battle_monster = []

    # 몬스터 뽑기
    for i in range(random.randint(1, 3)):
        battle_monster.append(monster_list.pop(
            random.randint(0, len(monster_list)-1)))

    # 전투 시작
    return battle(battle_character, battle_monster, money, character_skills)


# 전투
def battle(players, monsters, money, character_skills):
    boss_battle_check = False
    if monsters[0] in bosses:
        boss_battle_check = True

    if boss_battle_check:
        screen_clear()
        print("탑에 들어서니 등골이 서늘하다.")
        time.sleep(2)
        speaker = random.choice(players)
        print(f"{speaker}: 고요하군..")
        time.sleep(2)
        print(*monsters, end=" ")
        print("이(가) 등장했다!")
        time.sleep(2)
        print("가라!", end=" ")
        print(*players, end=" ")
        print(" ")
        time.sleep(2)
    else:
        screen_clear()
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

    status_battle = ''
    earned_exp = 0

    if player_avg_speed / len(players) >= monster_avg_speed / len(monsters):
        status_battle = 'player turn'
        print("재빠른 고양이들이 선공을 잡았다")
        time.sleep(2)
    else:
        status_battle = 'monster turn'
        print("아뿔싸! 적이 먼저 공격해왔다")
        time.sleep(2)

    # 턴 시작
    while True:
        first_check = players
        if status_battle == 'player turn':
            screen_clear()
            for i in range(len(players)):
                screen_clear()
                for k in range(len(players)):
                    # 캐릭터 기본 스테이터스 창
                    print(
                        f"{players[k]} Lv. {players[k].level} HP: ({players[k].HP} / {players[k].max_HP}) MP: ({players[k].MP} / {players[k].max_MP})")

                print("")
                for j in range(len(monsters)):
                    print(
                        f"{monsters[j]} Lv. {monsters[j].level} HP: ({monsters[j].HP} / {monsters[j].max_HP})")

                print("")
                action = input(
                    f"{players[i]}가 대기중입니다. 어떻게 하시겠습니까?\n [ 1) 일반공격 2) 스킬:{players[i].skill}(소모: {players[i].skill_cost}) 3) 포션 사용 4) 도망친다 ] : ")
                if input_check(1, 4, action) == False:
                    continue
                else:
                    if action == '1':
                        print("어떤 대상을 공격하시겠습니까?  ", end="")
                        print(''.join([f"{x}) {y} " for x, y in enumerate(
                            [x for x in monsters if x.HP != 0], start=1)]))
                        target = input()
                        if target.isdigit() == False:
                            print("정수를 입력해주세요.")
                            time.sleep(2)
                        elif bool(re.search(f"[1-{len(monsters)}]", target)) == False:
                            print("잘못 입력했습니다. 다시 시도하세요.")
                            time.sleep(2)
                        else:
                            target_monster = monsters[int(target) - 1]
                            check_ = players[i].normal_attack(target_monster)
                            if check_ == True:
                                earned_exp += int(target_monster.level * 2 * random.randint(
                                    1, 2) + target_monster.max_HP * 1.3 * random.randint(1, 2))
                                target_monster = '기절'
                                cache = []
                                for i in monsters:
                                    if i.HP != 0:
                                        cache.append(i)
                                monsters = cache
                            if len(monsters) == 0:
                                print("승리!")
                                time.sleep(2)
                                earned_exp
                                first_check[0].level_up(earned_exp)
                                first_check[1].level_up(earned_exp)
                                first_check[2].level_up(earned_exp)

                                # get the money
                                earned_money = int(
                                    earned_exp * round(random.random(), 2))
                                money += earned_money
                                print(" ")
                                print(f"{earned_money}$를 획득했습니다.")
                                print("")
                                input("\t 마을로 돌아가려면 아무 키나 누르세요.")
                                print("")
                                screen_clear()
                                if boss_battle_check:
                                    return 'town', money, True

                                return 'town', money

                    elif action == '2':
                        if players[i].skill == "그루밍":
                            while True:
                                print("어떤 대상을 힐링하시겠습니까?  ", end="")
                                print(*players, end=" ")
                                target = input()
                                if input_check(1, len(players), target) == False:
                                    continue
                                else:
                                    players[i].healing_Skill(
                                        players[int(target)-1])
                                    break
                        else:
                            while True:
                                print("어떤 대상을 스킬공격하시겠습니까?  ", end="")
                                print(''.join([f"{x}) {y} " for x, y in enumerate(
                                    [x for x in monsters if x.HP != 0], start=1)]))
                                target = input()
                                if input_check(1, len(monsters), target) == False:
                                    continue
                                else:
                                    target_monster = monsters[int(target) - 1]
                                    skill_find = character_skills[players[i].skill]
                                    check_ = skill_find(target_monster)
                                    # time.sleep(1)
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
                                        # earned_exp
                                        first_check[0].level_up(earned_exp)
                                        first_check[1].level_up(earned_exp)
                                        first_check[2].level_up(earned_exp)

                                        # get the money
                                        earned_money = int(
                                            earned_exp * round(random.random(), 2))
                                        money += earned_money
                                        print(f"{earned_money}$를 획득했습니다.")
                                        print("")
                                        input("\t 마을로 돌아가려면 아무 키나 누르세요.")
                                        print("")
                                        screen_clear()

                                        if boss_battle_check:
                                            return 'town', money, True
                                        return 'town', money
                                    break

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
                                        time.sleep(1)
                                        continue
                                    else:
                                        potion1.take_potion_hp(players[i])
                                        break

                                if use_potion == '2':
                                    if bool(potion2.num) == False:
                                        print('현재 소유하고 계신 츄르가 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        time.sleep(1)
                                        continue
                                    else:
                                        potion2.take_potion_mp(players[i])
                                        break

                                if use_potion == '3':
                                    if bool(potion3.num) == False:
                                        print('현재 소유하고 계신 북어포가 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        time.sleep(1)
                                        continue
                                    else:
                                        potion3.take_potion_hp(players[i])
                                        break

                                if use_potion == '4':
                                    if bool(potion4.num) == False:
                                        print('현재 소유하고 계신 캣닢이 없습니다.')
                                        print('소유하고 계신 소매품으로 선택해주세요!')
                                        time.sleep(1)
                                        continue
                                    else:
                                        potion4.take_potion_mp(players[i])
                                        break
                        else:
                            print('현재 소유하신 소모품이 없습니다!')
                            time.sleep(1)
                            print('저런. 턴이 넘어갔네요!')
                            time.sleep(1)

                    elif action == '4':
                        if monsters[0] in bosses:
                            print("보스한테서는 도망갈 수 없습니다")
                            time.sleep(1)
                            continue
                        # 각 고양이의 속도에 따라 탈출할 확률 다름
                        if players[i].speed * (1 + random.randint(1, 10) / 10) > monster_avg_speed:
                            screen_clear()
                            print("탈출에 성공했습니다.")
                            time.sleep(2)
                            print("마을로 돌아갑니다.")
                            time.sleep(2)
                            return 'town', money

            status_battle = 'monster turn'

        elif status_battle == 'monster turn':
            for j in range(len(monsters)):
                screen_clear()

                targeted_player = random.randint(0, len(players) - 1)
                check_ = monsters[j].normal_attack(players[targeted_player])
                if check_ == True:
                    players[targeted_player].faint = True
                    cache = []
                    for i in players:
                        if i.faint == False:
                            cache.append(i)
                    players = cache

                if len(players) == 0:
                    print("패배...")
                    time.sleep(2)
                    if boss_battle_check:
                        return 'lose', money, True

                    return 'lose', money

            status_battle = 'player turn'


# 보스배틀 준비
def prebossbattle(character_list, money, character_skills, boss_clear):
    battle_character = []
    for i in character_list:
        if i.HP != 0:
            battle_character.append(i)

    # 고양이 셋 다 기절해 있다면
    if len(battle_character) == 0:
        print("싸울 수 있는 고양이가 없습니다. 마을로 돌아갑니다.")
        time.sleep(2)
        return 'town', money, boss_clear

    # 고양이 셋 중 하나라도 기절해 있으면 의사 물어보기
    if len(battle_character) != len(character_list):
        question = input(
            "고양이들 중에 싸울 수 없는 고양이가 있는 것 같아요. 그래도 싸우시겠습니까? [ 1) 네 2) 마을로 돌아갈래요 ]")
        if question == '1':
            print("좋은 자신감이에요")
            time.sleep(2)
        else:
            return 'town', money, boss_clear

    # 나올 보스
    if boss_clear == 0:
        battle_monster = [bosses[0]]
    elif boss_clear == 1:
        battle_monster = [bosses[1], bosses[2]]
    elif boss_clear == 2:
        battle_monster = [bosses[3]]

    # 전투 시작
    return battle(battle_character, battle_monster, money, character_skills)


def lose(money):
    money = money//2
    print("소지금의 절반을 잃어버립니다.")
    time.sleep(1)
    print("마을로 돌아갑니다")
    return 'town', money
