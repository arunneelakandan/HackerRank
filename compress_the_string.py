from itertools import groupby
s=map(int,list(input()))
l=[(sum(1 for i in g),k) for k,g in groupby(s)]
print(' '.join(map(str,l)))