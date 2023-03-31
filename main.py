import time
from utility import *
from object import *
from shop import *
from items import *
from battlephase import *

# Selected character list
player_character_list = []

# Money of player
player_money = 1000

# Check the boss cleared
boss_clear = 0

# Status
status = 'town'

"""Story Start"""

# Intro
screen_clear()
print("==========================")
time.sleep(1)
print("====== 냥이 키우기 =======")
time.sleep(1)
print("==========================")
time.sleep(1)
print("")
time.sleep(1)

# 캐릭터 선택(3 마리)
while len(player_character_list) < 4:
    screen_clear()
    print("간택 받고 싶은 고양이 세마리를 골라주세요!(현재:", end=" ")
    print(*player_character_list, end=" ")
    print(")")
    select = input("1)냥검사 2)냥법사 3)냥궁수 4)냥힐러 : ")
    if input_check(1, len(characters), select) == False:
        continue
    elif characters[select] in player_character_list:
        print(f"이미 {characters[select]}에게 간택 받았습니다.")
        time.sleep(1)
    else:
        player_character_list.append(characters[select])

        # 3 마리가 다 채워졌다면 break
        if len(player_character_list) == 3:
            break

screen_clear()
print("당신은", end=" ")
print(*player_character_list, end="")
print("를 선택했습니다. 이제 모험을 떠나볼까요.")
time.sleep(4)


# Story #1. 길 걷기
screen_clear()
print("여행을 떠난 당신은 길을 걷다 한 마을에 도착했습니다.")
time.sleep(2)

print("마을을 한번 둘러볼까요.")
time.sleep(2)

while status != 'quit':
    # 어떤 행동 끝나면 마을
    if status == 'town':
        status = town(player_character_list, player_money)

    # 여관
    elif status == 'inn':
        status, player_money = inn(player_character_list, player_money)

    # 상점
    elif status == 'buy_item':
        status, player_money = buy_item(player_character_list, player_money)

    # 일반 전투
    elif status == 'prebattle':
        status, player_money = prebattle(
            player_character_list, player_money, character_skills)

    # 보스 전투
    elif status == 'prebossbattle':
        status, player_money, check_boss_clear = prebossbattle(
            player_character_list, player_money, character_skills, boss_clear)

        # 보스 클리어 확인
        if check_boss_clear == True:
            boss_clear += 1
            check_boss_clear = False

        if boss_clear == 3:
            status == 'victory'

    elif status == 'lose':
        status, player_money = lose(player_money)

    # 총 스테이터스 창

    elif status == 'all_status':
        status = all_status_s(player_character_list)
