if __name__ == '__main__':
    score_list = []
    name_list = []
    name_score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        name_list.append(name)
        name_score_list.append((name,score))
    
    first_min_number = min(set(score_list))
    score_list = [i for i in score_list if i != first_min_number]
    second_min_number = min(score_list)
    
    index_list = []
    for i,j in name_score_list:
        if j == second_min_number:
            index_list.append(i)
            
    
    sorted_name = sorted(index_list)
    for i in sorted_name:
        print(i) 