gTotal = 0

def Hanoi(n, a, b, c):
    global gTotal
    if(n > 0):
        Hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        gTotal = gTotal + 1
        Hanoi(n-1, b, a, c)

Hanoi(3, 'A', 'B', 'C')
print("Total Steps: %s" % gTotal)