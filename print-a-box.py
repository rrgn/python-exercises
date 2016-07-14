n = raw_input("> ")
n = int(n)

def printSquare(n):
    counter = 0
    row = makeARow(n);
    while counter < n:
        print row
        counter += 1

def makeARow(n):
    row = ""
    counter = 0
    while counter < n:
        row = row + '*'
        counter = counter + 1

    return row

printSquare(n)


##alternate
def square(n)
    for i in xrange(0, n):
        print "*" * n

n = int(raw_input("Enter a number: "))
square(n)
