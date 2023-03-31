from utility import *
import time
from items import *
from battlephase import *

# store - 양예린

pet_list = []
# money > pet1.price


def buy_item(character_list, money):
    screen_clear()
    print('    어서오세요! 냥냥상점입니다.*^^*')
    print('======================================')

    while True:
        print('\n구매하실 물건을 선택해주세요.')
        choice = input('<소모품: 1> <장비: 2> < 귀여운 pet : 3>\n:')
        if input_check(1, 3, choice) == False:
            continue
        elif choice == '1':
            print('================메뉴판================')
            print(' 참치캔: HP를 20만큼 채워줍니다.| $10')
            print('  츄르 : MP를 20만큼 채워줍니다.| $10')
            print(' 북어포: HP를 50만큼 채워줍니다.| $25')
            print('  캣닢 : MP를 50만큼 채워줍니다.| $25')

            while True:
                choice_potion = input('1) 참치캔 | 2) 츄르 | 3) 북어포 | 4) 캣닢\n:')
                if input_check(1, 4, choice_potion) == False:
                    continue
                elif choice_potion == '1':
                    if money > potion1.price:
                        print('참치캔을 구입하셨습니다!')
                        potion1.num += 1
                        money -= 10  # potion1.price
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                elif choice_potion == '2':
                    if money > potion2.price:
                        print('츄르를 구입하셨습니다!')
                        potion2.num += 1
                        money -= 10  # potion2.price
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                elif choice_potion == '3':
                    if money > potion3.price:
                        print('북어포을 구입하셨습니다!')
                        potion3.num += 1
                        money -= 25  # potion3.price
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                elif choice_potion == '4':
                    if money > potion4.price:
                        print('캣닢을 구입하셨습니다!')
                        potion4.num += 1
                        money -= 25  # potion4.price
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                else:
                    print('1, 2, 3, 4 중에 선택해주십시오.')

        elif choice == '2':
            print('장비 구매를 원하시는군요!')
            print('================ 전용 장비 ================')
            print(' 냥검사 : 날카로운 발톱 \t| $30')
            print(' 냥법사 :      방울    \t\t| $30')
            print(' 냥궁수 :      새총    \t\t| $30')
            print(' 냥힐러 :  장난감 막대  \t| $30')
            browse_equipment = {
                "냥검사": equipment1.equip,
                "냥법사": equipment2.equip,
                "냥궁수": equipment3.equip,
                "냥힐러": equipment4.equip
            }
            for i in range(len(character_list)):
                print(f'{character_list[i]}의 장비 : ', end=' ')
            print('를 구매하실 수 있습니다.')

            while True:
                select = input("1,2,3:")
                if input_check(1, 3, select) == False:
                    continue
                elif select == '1':
                    if money > 30:
                        check = browse_equipment[character_list[0].name](
                            character_list[0])
                        print("장착 후 공격력 :", character_list[0].attack,
                              "장착한 무기 :", character_list[0].eq)
                        if check:
                            money -= 30
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break
                elif select == '2':
                    if money > 30:
                        check = browse_equipment[character_list[1].name](
                            character_list[1])
                        print("장착 후 공격력 :", character_list[1].attack,
                              "장착한 무기 :", character_list[1].eq)
                        if check:
                            money -= 30
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break
                elif select == '3':
                    if money > 30:
                        check = browse_equipment[character_list[2].name](
                            character_list[2])
                        print("장착 후 공격력 :", character_list[2].attack,
                              "장착한 무기 :", character_list[2].eq)
                        if check:
                            money -= 30
                        break
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break
                break

        elif choice == '3':
            print("\n귀여운 pet 구매를 원하시는군요! 탁월한 선택이십니다.^^\n")
            print(
                f'현재 pet) 털뭉치: {pet1.state} | 캔디볼: {pet2.state} | 도토리볼: {pet3.state}')
            print('※안내※ pet은 종류당 한 마리만 구매하실 수 있습니다.\n')

            print('====================소개판====================')
            print(' 털뭉치 : 방어력을 5만큼 증가시켜줍니다.| $100')
            print(' 캔디볼 : 방어력을 10만큼 증가시켜줍니다| $200')
            print('도토리볼: 방어력을 15만큼 증가시켜줍니다| $300')

            while True:
                choice_pet = input('1) 털뭉치 | 2) 캔디볼 | 3) 도토리볼 \n:')
                if input_check(1, 3, choice_pet) == False:
                    continue
                elif choice_pet == '1':
                    if money > pet1.price:
                        if pet1.state == 0:
                            print('털뭉치를 구입하셨습니다!')
                            pet1.upgrade_defense(character_list[0])
                            pet1.upgrade_defense(character_list[1])
                            pet1.upgrade_defense(character_list[2])
                            print(f'털뭉치가 모두의 방어력을 5만큼 증가시켰습니다!')
                            pet1.state += 1
                            pet_list.append(pets[choice_pet].name)
                            money -= pet1.price
                            break

                        else:
                            print(f'이미 {pet1.name}을 소유하고 계십니다!')
                            print('※주의※ pet은 종류당 한 마리만 구매하실 수 있습니다!!')
                            print('다른 종류의 pet으로 다시 선택해주세요!\n')
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                elif choice_pet == '2':
                    if money > pet2.price:
                        if pet2.state == 0:
                            print('캔디볼을 구입하셨습니다!')
                            pet2.upgrade_defense(character_list[0])
                            pet2.upgrade_defense(character_list[1])
                            pet2.upgrade_defense(character_list[2])
                            print(f'캔디볼이 모두의 방어력을 10만큼 증가시켰습니다!')
                            pet2.state += 1
                            pet_list.append(pets[choice_pet].name)
                            money -= pet2.price
                            break

                        else:
                            print(f'이미 {pet2.name}을 소유하고 계십니다!')
                            print('※주의※ pet은 종류당 한 마리만 구매하실 수 있습니다!!')
                            print('다른 종류의 pet으로 다시 선택해주세요!\n')
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                elif choice_pet == '3':
                    if money > pet3.price:
                        if pet3.state == 0:
                            print('도토리볼을 구입하셨습니다!')
                            pet3.upgrade_defense(character_list[0])
                            pet3.upgrade_defense(character_list[1])
                            pet3.upgrade_defense(character_list[2])
                            print(f'도토리볼이 모두의 방어력을 15만큼 증가시켰습니다!')
                            pet3.state += 1
                            pet_list.append(pets[choice_pet].name)
                            money -= pet3.price
                            break

                        else:
                            print(f'이미 {pet3.name}을 소유하고 계십니다!')
                            print('※주의※ pet은 종류당 한 마리만 구매하실 수 있습니다!!')
                            print('다른 종류의 pet으로 다시 선택해주세요!\n')
                    else:
                        print('소지금이 모자랍니다! 다른 상품을 구매해주세요!')
                        break

                else:
                    print('\n1, 2, 3 중에 선택해주십시오.')
                    continue

        else:
            print('\n1, 2, 3 중에 선택해주세요!!')
            continue

        print(f'남은 소지금은{money}원 입니다!')

        if money == 0:
            print('가지고 계신 소지금을 모두 사용하셨습니다!\n다음에 또 만나요~')
            time.sleep(3)
            print("마을로 돌아갑니다")
            time.sleep(3)
            town()

        buy_again = input('구매를 계속 진행하시겠습니까?\n y/n로 선택해주세요:')

        if input_check2(buy_again) == False:
            continue

        elif buy_again == 'y':
            continue

        elif buy_again == 'n':
            print('구매를 종료합니다. 저희 냥냥상점을 찾아주셔서 감사합니다!\n다음에 또 만나요~')
            time.sleep(3)
            print("마을로 돌아갑니다")
            time.sleep(3)
            return 'town', money


# 마을
def town(character_list, money):
    # 마을에서 행동 리스트
    town_action = {
        '1': 'prebattle',
        '2': 'prebossbattle',
        '3': 'inn',
        '4': 'buy_item',
        '5': 'all_status'
    }
# status()
    while True:
        screen_clear()
        for i in character_list:
            print(i.status())

        print("-------------------------------------------------")
        print(f"소지금: {money}$")
        print("- 인벤토리 -")
        print(f"{potion1.name} : {potion1.num}개")
        print(f"{potion2.name} : {potion2.num}개")
        print(f"{potion3.name} : {potion3.num}개")
        print(f"{potion4.name} : {potion4.num}개")

        if bool(pet_list) == True:
            print('현재 pet : ', end=" ")
            print(*pet_list)

        action = input("어디로 갈까요? [ 1)길거리 2)높은 탑 3)여관 4)상점 5)총 스테이터스] : ")
        if input_check(1, 5, action) == False:
            continue
        else:
            return town_action[action]


def inn(character_list, money):
    while True:
        screen_clear()
        print("어서오세요~고양이 카페입니다. 쉬고 가실건가요?")
        time.sleep(1)
        print("요금은 100$입니다")
        time.sleep(1)
        print(f"소지금: {money}$")
        action = input("1)쉬기 2)돌아가기 : ")
        if input_check(1, 2, action) == False:
            continue
        elif money < 30:
            print("돈도 없는 주제에. 저리 꺼져")
            time.sleep(2)
            print("마을로 돌아갑니다")
            time.sleep(2)
            return 'town', money
        else:
            if action == '1':
                return recovery_in_inn(character_list, money)
            elif action == '2':
                return 'town', money


def recovery_in_inn(character_list, money):

    money -= 100

    for i in character_list:
        i.HP = i.max_HP
        i.MP = i.max_MP
        i.faint = False

    print("고양이 카페에서 푹 쉬었더니 고양이들의 체력이 회복되었습니다")
    time.sleep(3)
    print("마을로 돌아갑니다")
    time.sleep(3)

    return 'town', money


def all_status_s(players):
    screen_clear()
    print("==========================")
    for i in players:
        print(i.all_status())
    print("==========================\n")
    input("계속 하시려면 아무 키나 입력해주세요!")

    return 'town'
