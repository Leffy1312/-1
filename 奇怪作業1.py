# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:25:26 2024

@author: USER
"""

import random

num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = 0,0,0,0,0,0,0,0,0,0

count = 0
while count < 10:
    random_number = random.randint(1, 20) * 5
    if random_number != num1 and random_number != num2 and random_number != num3 and random_number != num4 and random_number != num5 and random_number != num6 and random_number != num7 and random_number != num8 and random_number != num9 and random_number != num10:   
        if count == 0:
            num1 = random_number
        elif count == 1:
            num2 = random_number
        elif count == 2:
            num3 = random_number
        elif count == 3:
            num4 = random_number
        elif count == 4:
            num5 = random_number
        elif count == 5:
            num6 = random_number
        elif count == 6:
            num7 = random_number
        elif count == 7:
            num8 = random_number
        elif count == 8:
            num9 = random_number
        elif count == 9:
            num10 = random_number
        count += 1

print("十個不重複且可被5整除的數字:", num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)