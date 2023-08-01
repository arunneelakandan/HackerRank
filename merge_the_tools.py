def merge_the_tools(string, k):
    # your code goes here
    list_of_strings = [string[i:i+k] for i in range(0,len(string),k)]
    
    for sr in list_of_strings:
        t = ''
        for s in sr:
            if s not in t:
                t += s
        
        print(t)   


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)