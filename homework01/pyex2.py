#Exercise 1
intlist = [4, 23, 3, 5, 3, 2, 63, 98, 1, 34]

def evenorodds(somelist):
    for x in somelist:
        if (x%2 == 0):
            print(f'{x}: even')
        else:
            print(f'{x}: odd')

evenorodds(intlist)
