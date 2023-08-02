from collections import deque


d = deque()
for _ in range(int(input())):
    args = input().strip().split()
    
    if args[0] == 'append':
        d.append(args[1])
    
    elif args[0] == 'appendleft':
        d.appendleft(args[1])
        
    elif args[0] == 'clear':
        d.clear()        

    elif args[0] == 'extend':
        d.extend(args[1])
    
    elif args[0] == 'extendleft':
        d.extendleft(args[1])
        
    elif args[0] == 'count':
        d.count(args[1])
        
    elif args[0] == 'pop':
        d.pop()
    
    elif args[0] == 'popleft':
        d.popleft()
        
    elif args[0] == 'extend':
        d.extend(args[1])
        
    elif args[0] == 'remove':
        d.remove(args[1])
        
    elif args[0] == 'reverse':
        d.reverse()
        
    elif args[0] == 'rotate':
        d.rotate(args[1])
        
print(' '.join(d))