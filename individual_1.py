#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Введите число карандашей (N <= 10): "))

if n == 1:
    word = "карандаш"
elif 2 <= n <= 4:
    word = "карандаша"
else:
    word = "карандашей"

print(f"Я купил {n} {word}")