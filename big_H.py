if __name__ == "__main__":
    num = int(input())
    complete_pattern_list = []
    
    for i in range(num**2):
        if i < num:
            print(str('H'*(((i+1)*2)-1)).center(num*2 - 1,'-'))
        elif i >= num and i <= num**2 - num:
            print(str('H'*num).ljust(num**2,'-') + str('H'*num).rjust(num**2,'-'))
        elif i > num**2 - num:
            print(str('H'*(((i+1)*2)-1)).center(num*2 - 1,'-'))