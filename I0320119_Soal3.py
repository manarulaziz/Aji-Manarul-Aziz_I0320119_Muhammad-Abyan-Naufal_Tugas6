for i in range(10, 25):
    if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
        print(i, "adalah bilangan prima")
    else:
        print(i, "bukan prima")