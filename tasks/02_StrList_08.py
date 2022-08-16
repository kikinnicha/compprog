import math

# take the input of a b and c and split it for each value
[a, b, c] = input().split(",")

# initial value of b
initial_b = b

# check if b, if not return 0
b = b if b else "0"

# calculate the numerator by joining string of decimal (b) and repeating decimal (c), convert to integer and minus by decimal that is not repeating (b)
numerator = int(b + c) - int(b)

# calculate the denominator by convert each repeating decimal (c) to 9 with length of repeating decimal times (len(c)), then join with 0 repeat by length of b times (len(initial_b))
denominator = int(''.join(map(str,([9] * len(c)) + ([0] * len(initial_b)))))

# calculate the exceed fraction to the denominator
numerator = denominator * int(a) + numerator

# find the divisor using math.gcd
divisor = math.gcd(numerator, denominator)

# divide numerator and denominator by gcd and print out the solution
print("%d / %d" % (numerator//divisor, denominator//divisor))

# formula from -> https://www.opendurian.com/news/mathcirdec/