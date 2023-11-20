from collections import Counter

if __name__ == "__main__":
    n = int(input())
    list_of_all_shoes = list(map(int,input().split()))
    
    amount_collected = 0
    for _ in range(int(input())):
        args = input().strip().split()
        if int(args[0]) in list_of_all_shoes:
            amount_collected += int(args[1])
            list_of_all_shoes.remove(int(args[0]))
        
        else:
            pass
        
    print(amount_collected)