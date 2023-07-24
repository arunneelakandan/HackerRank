def print_rangoli(size):
    # your code goes here
    alphabets = list(reversed(list(map(chr, range(97, 123)))[:size]))
    index = 1
    for i in range(1,2*size):
        if i < size:
            sliced_string = '-'.join(alphabets[0:i] + list(reversed(alphabets[0:i-1])))
            print(sliced_string.center((((size + (size - 1)) * 2) - 1) ,'-'))
        elif i == size:
            sliced_string = '-'.join(alphabets[0:i] + list(reversed(alphabets[0:i-1])))
            print(sliced_string.center((((size + (size - 1)) * 2) - 1) ,'-'))
        elif i > size:
            index -= 1
            sliced_string = '-'.join(alphabets[0:i][0:index-1] + list(reversed(alphabets[0:i-1][0:index-2])))
            print(sliced_string.center((((size + (size - 1)) * 2) - 1) ,'-'))
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)