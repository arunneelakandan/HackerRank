def print_rangoli(size):
    # your code goes here
    alphabets = list(reversed(list(map(chr, range(97, 123)))[:size]))
    for i in range(1,2*size-1):
        sliced_string = '-'.join(alphabets[0:i] + list(reversed(alphabets))[0:i-1])
        if i < size:
            print(sliced_string.center((((size + (size - 1)) * 2) - 1) ,'-'))
        
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)