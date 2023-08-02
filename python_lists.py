if __name__ == '__main__':
    
    d = []
    for _ in range(int(input())):
        args = input().strip().split()
        
        if args[0] == 'insert':
            d.insert(int(args[1]),int(args[2]))
        
        elif args[0] == 'print':
            print(d)

        elif args[0] == 'remove':
            d.remove(int(args[1]))
                
        elif args[0] == 'append':
            d.append(int(args[1]))
        
        elif args[0] == 'sort':
            d.sort()        

        elif args[0] == 'pop':
            d.pop()
            
        elif args[0] == 'reverse':
            d.reverse()
