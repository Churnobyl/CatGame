import os
import re
import platform


def input_check(x, y, text):
    pattern = "[{}-{}]".format(x, y)
    if text.isdigit() is False:
        print("정수를 입력해주세요.")
        return False
    elif bool(re.fullmatch(pattern, text)) is False:
        print("잘못 입력했습니다. 다시 시도하세요.")
        return False
    else:
        return True


def input_check2(text):
    if bool(re.fullmatch("[xy]", text)) is False:
        print("잘못 입력했습니다. 다시 시도하세요.")
        return False
    else:
        return True


def screen_clear():
    os_check = platform.system()
    if os_check == 'Windows':
        os.system("cls")
    else:
        os.system("clear")
