def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    x1 = 1234
    y1 = 5678

    val = karatsuba(x,y)
    print val

def karatsuba(x,y):
    n = len(str(x))

    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        mid = n / 2

        a = x / 10**(mid)
        b = x % 10**(mid)
        c = y / 10**(mid)
        d = y % 10**(mid)

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        diff = karatsuba(a+b, c+d) - ac - bd
        
        final = ac * 10**(2*mid) + (diff * 10**mid) + bd
        return final


if __name__ == "__main__":
    main()
