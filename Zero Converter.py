def neg(n):
    while n <= 0:
        print(n, end=" ")
        n += 1
def pos(n):
    while n >= 0:
        print(n, end=" ")
        n -= 1

n = int(input("Enter a number (positive or negative): "))
if(n<0):
    neg(n)
else:
    pos(n)
