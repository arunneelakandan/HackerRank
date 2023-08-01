if __name__ == '__main__':
    N=int(input())
    M=3 * N
    C = '.|.'
    for i in range(N//2):
        print((C * (i*2 + 1)).center(M,'-'))
    
    print('WELCOME'.center(M,'-'))
        
    for i in range(N//2):
        print((C * ((N-(i*2)-2))).center(M,'-'))