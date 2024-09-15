import functools
import math

@functools.cache
def g(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1/2
    else:
        return (1-1/n)*g(n-1) + (1/n)*g(n-2)
    
def main():
    for i in range(1, 30 + 1):
        print("g(%5d) = %.20f" % (i, abs(g(i) - 1/math.e)))

if __name__ == "__main__":
    main()