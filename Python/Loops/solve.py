# cara saya
def looping(input):
    for i in range(input):
        if i <= 20:
            result = i ** 2
            print(result)
        else:
            break
looping(5)

# cara hackerrank

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        result = i * i
        print(result)



