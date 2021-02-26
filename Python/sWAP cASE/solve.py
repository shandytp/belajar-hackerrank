# cara saya

def swap_case(s):
    swap = ""

    for letter in s:
        if letter.isupper() == True:
            swap += letter.lower()
        else:
            swap += letter.upper()

    return swap

# cara komentar di HackerRank

# def swap_case(s):
#     return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)