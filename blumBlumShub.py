import math

def asalKontrol(sayi):
        kok = math.sqrt(sayi)
        if kok == 1:
                return 1
        for i in range(2, int(kok) + 1):
                if asalKontrol(i)== 1:
                        if (sayi % i == 0):
                                return 0
        return 1

#------------------------------------------------------------------------------

p = int(input("p = "))

while (asalKontrol(p) != 1):
	print("p asal degil")
	p = int(input("p = "))


q = int(input("q = "))

while (asalKontrol(q) != 1):
        print("q asal degil")
        q = int(input("q = "))

M = p * q

s = int(input("(Tohum) s = "))

miktar = int(input("Kac sayi uretilsin = "))

while miktar>0:
	sayi = (s**2) % M
	s = sayi
	print(sayi)
	miktar-=1
