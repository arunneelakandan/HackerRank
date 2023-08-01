if __name__ == '__main__':
    n = int(input())
    
    list_of_string = []
    for i in range(n):
        list_of_string.append(input())
    
    print(len(set(list_of_string)))
    
    _t = {}
    
    for i in list_of_string:
        if i in list_of_string and i in _t:
            _t[i] += 1
        elif i in list_of_string:
            _t[i] = 1
            
    print(' '.join([str(i) for i in _t.values()]))