if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])

    scores = []
    for j in range(len(records)):
        scores.append(records[j][1])
    min_score = min(scores)

    while min_score in scores:
        scores.remove(min_score)
    
    second_lowest = []
    for i in range(len(records)):
        if records[i][1] == min(scores):
            second_lowest.append(records[i][0]) 
    second_lowest.sort()
    
    for name_ in second_lowest:
        print(name_)     
