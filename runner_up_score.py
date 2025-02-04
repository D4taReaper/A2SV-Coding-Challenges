if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    max_score = max(arr)
    runner_up = -200
    for num in arr:
        if num > runner_up and num < max_score:
            runner_up = num
    print(runner_up)
