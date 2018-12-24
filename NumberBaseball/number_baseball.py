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
MAX = 9

def generate_numbers():
    """
    1 ~ 9 사이의 정수를 무작위로 생성하며, 중복없는 3개의 정수를 반환한다.

    :return:    정수 3개를 갖는 리스트
    """
    nums = []

    while True:
        num = random.randint(MIN, MAX)
        if num in nums:
            continue

        nums.append(num)
        if len(nums) == 3:
            break
    print("nums : " + str(nums))

    return nums

def evaluate_numbers(target_nums, nums):
    """
    Strike와 Ball의 개수를 파악하여 반환한다.

    :param target_nums:
    :param nums:
    :return:
    """
    ball_cnt = 0
    strike_cnt = 0

    for inx in range(len(target_nums)):
        if target_nums[inx] == nums[inx]:
            strike_cnt = strike_cnt + 1
        else:
            if target_nums[inx] in nums:
                ball_cnt = ball_cnt + 1

    return (strike_cnt, ball_cnt)

def get_number_from_user():
    """
    사용자로부터 x >= MIN and x <=MAX 를 만족하는 정수 3개를 입력받는다.
    이외의 값을 입력받을 경우, 경고 메시지를 출력하고 다시 입력 받는다.
    중복된 입력이 있는 경우 다시 입력 받는다.

    :return: 사용자로부터 입력받은 정수
    """

    nums = None

    while True:
        int_str = input("3개의 정수를 입력하십시오 : ")
        nums = []

        if __check_user_input(int_str, nums) == False:
            continue
        else:
            break

    return nums

def __check_user_input(int_str, nums):
    """
    사용자로부터 받은 입력을 체크한다.
    - 길이가 3인지
    - 1 ~ 9 사이의 정수인지
    - 중복된 정수가 있는지

    :param int_str:
    :param nums:
    :return:
    """
    num = 0

    if len(int_str) != 3:
        print("입력값의 길이가 3이 아닙니다.")
        return False

    for ch in int_str:
        try:
            num = int(ch)
            if not (num >= MIN and num <= MAX):
                raise  ValueError
        except ValueError:
            print("1 ~ 9 사이 정수만 입력바랍니다. %s" % (ch))
            return False

        if not (num in nums):
            nums.append(num)
            continue
        else:
            print("중복된 값이 있습니다. %s" % (ch))
            return False

    return True

def start_game():
    success = False
    guess_cnt = 1

    print("임의의 숫자를 생성합니다.")
    target_nums = generate_numbers()

    while guess_cnt <= 10:
        print("(%d / 10) 번째 시도" % (guess_cnt))
        nums = get_number_from_user()
        strike_cnt, ball_cnt = evaluate_numbers(target_nums, nums)

        print("Strike (%d), Ball (%d)" % (strike_cnt, ball_cnt))

        if strike_cnt == 3:
            success = True
            break

        guess_cnt = guess_cnt + 1

    if success == True:
        print("축하합니다.")
    else:
        print("주어진 기회내에 정답을 맞추지 못했습니다. " + str(target_nums))

if __name__ == "__main__":
    start_game()
