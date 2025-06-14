import testinit as t

class driver:
    if __name__ == "__main__":
        import sys
        for i in range (2):
            real = int(input("Enter the real part: "))
            imag = int(input("Enter the imaginary part: "))
        x = t.ComplexTest(real, imag)
        print("{real}+{imag}i".format(real=x.real, imag=x.imag))

