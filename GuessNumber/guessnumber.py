# -*- coding: utf-8 -*-
"""
Copyright 2019 Joohyun Lee(ppiazi@gmail.com)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import random

MIN = 1
MAX = 99

def evaluate_number(target_num, num):
    """
    target_num과 num 값을 비교하여 결과를 반환한다.

    :param target_num:  guess해야 하는 숫자
    :param num: 사용자 입력 숫자
    :return:    0 (일치), 1(target_num > num), -1(target_num < num)
    """
    if target_num == num:
        return 0
    elif target_num > num:
        return 1
    else:
        return -1

def generate_target_number():
    """
    임의의 x >= MIN and x <=MAX 을 만족하는 정수를 생성한다.

    :return:    x >= MIN and x <=MAX 을 만족하는 정수
    """

    ret = random.randint(MIN, MAX)

    return ret

def get_number_from_user():
    """
    사용자로부터 x >= MIN and x <=MAX 를 만족하는 정수를 입력받는다.
    이외의 값을 입력받을 경우, 경고 메시지를 출력하고 다시 입력 받는다.

    :return: 사용자로부터 입력받은 정수
    """

    num = 0

    while True:
        try:
            int_str = input("정수를 입력하십시오 : ")
            num = int(int_str)
            if num >= MIN and num <= MAX:
                break
            raise ValueError
        except ValueError as e:
            print("%d ~ %d 사이 정수만 입력바랍니다." % (MIN, MAX))
            continue

    return num

def start_game():
    """
    숫자맞추기 게임을 시작한다.

    총 10번의 기회를 주어지며, 정답을 맞추지 못할 경우 게임이 종료된다.(정답을 알려준다.)

    :return:
    """
    success = False
    guess_cnt = 1

    print("임의의 숫자를 생성합니다.")
    target_num = generate_target_number()

    while guess_cnt <= 10:
        print("(%d / 10) 번째 시도" % (guess_cnt))
        num = get_number_from_user()
        result = evaluate_number(target_num, num)

        if result == 0:
            success = True
            break
        elif result == -1:
            print("대상 값보다 작습니다.")
        else:
            print("대상 값보다 큽니다.")

        guess_cnt = guess_cnt + 1

    if success == True:
        print("축하합니다. ( %d )" % (target_num))
    else:
        print("주어진 기회내에 정답을 맞추지 못했습니다. ( %d )" % (target_num))

if __name__ == "__main__":
    start_game()
