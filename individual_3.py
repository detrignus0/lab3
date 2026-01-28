#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Варианты покупки:")

for bulls in range(11):
    for cows in range(21):
        calves = 100 - bulls - cows

        if calves >= 0:
            price = (bulls * 10) + (cows * 5) + (calves * 0.5)

            if price == 100:
                print(f"Быков: {bulls}, Коров: {cows}, Телят: {calves}")