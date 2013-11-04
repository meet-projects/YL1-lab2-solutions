def divisors(n):
    n = int(n)
    for number in xrange(1, n + 1):
        if n%number == 0:
            print number

if __name__=="__main__":
    n = raw_input("Enter a number: ")
    divisors(n)