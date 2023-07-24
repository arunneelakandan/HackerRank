#!/bin/python3

import math
import os
import random
import re
import sys


def transformSentence(sentence):
    # Write your code here

    new_string = ''
    for strings in sentence.split(' '):
        for i in range(0,len(strings)):
            if i == 0:
                new_string += strings[i]
            
            elif strings[i] > strings[i - 1]:
                new_string += strings[i].upper()
            
            elif strings[i] < strings[i - 1]:
                new_string += strings[i].lower()
            
            elif strings[i] == strings[i - 1]:
                new_string += strings[i]
                
        if len(sentence.split(' ')) > 1:
            new_string += ' '
    

    return new_string

if __name__ == '__main__':

    sentence = input()

    result = transformSentence(sentence)

    print(result)