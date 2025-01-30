def swap_case(s):
    s = list(s)
    i = 0
    while i < len(s):
        for char in s:
            if char.isupper():
                low = char.lower()
                s[i] = low
                i += 1   
            else:
                up = char.upper()
                s[i] = up
                i += 1
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
