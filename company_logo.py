import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    for i,j in sorted({i:list(s).count(i) for i in list(s)}.items() ,key=lambda x:(-x[1], x[0]))[:3]:
        print(i,'',j)