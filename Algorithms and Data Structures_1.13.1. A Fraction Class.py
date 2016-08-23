class Fraction:

	def __init__(self,top,bottom):

		self.num = top
		self.den = bottom
		
	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def __add__(self,otherfraction):

		 newnum = self.num*otherfraction.den + self.den*otherfraction.num
		 newden = self.den * otherfraction.den
 
		 common = gcd(newnum,newden)
		
		 return Fraction(newnum//common,newden//common)



def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n

myf = Fraction(3,5)
print(myf)            # 3/5
print myf.__str__()   # 3/5
print str(myf)        # 3/5


f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
print(f3)             # 3/4
