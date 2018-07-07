#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:31:51 2018

@author: lucas
"""

def genSubsets(list_of_numbers):
    if len(list_of_numbers) == 0:
        return [[]]
    last_numbers = genSubsets(list_of_numbers[1:])
    first_element = list_of_numbers[:1]
    combine_first_with_others = []
    for other_element in last_numbers:
        combine_first_with_others.append(first_element + other_element)
    return last_numbers + combine_first_with_others


print(genSubsets([1,2,3])) 