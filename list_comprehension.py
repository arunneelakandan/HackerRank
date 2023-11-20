if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list_of_arr = [[k,j,i] for k in range(x+1) for j in range(y+1) for i in range(z+1) if i+j+k != n]
    print(list_of_arr)