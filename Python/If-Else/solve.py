def if_solver(n):
    if n % 2 == 1:
        print("Weird")
    elif n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n % 2 == 0:
        print("Not Weird")
    else:
        return 0

if_solver(24)