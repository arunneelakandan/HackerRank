from itertools import combinations


def minion_game(string):
    stuart = 0
    kevin = 0
    
    vowels = ['a','e','i','o','u']
    
    for r in range(0, len(string)):
        for l in range(1,len(string)+1):
            startwith_vowel = False
            if string[r:l] and string[r:l][0] in vowels:
                startwith_vowel = True

        
            if startwith_vowel:
                kevin += 1
                
            else:
                stuart += 1
            
    if stuart > kevin:
        print('Stuart',stuart)
    else:
        print('Kevin',kevin)        
    

if __name__ == '__main__':
    s = input()
    minion_game(s)