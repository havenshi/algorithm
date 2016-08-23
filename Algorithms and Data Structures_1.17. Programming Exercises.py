# 1.Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
class fraction:
	def __init__(self,n,m):
		self.num=n
		self.den=m

		if self.den<0:
			self.num=-n
			self.den=-m

	def __str__(self):
		return str(self.num)+'/'+str(self.den)
		
	def getNum(self):
		return self.num
		
	def getDen(self):
		return self.den
		
	def __add__(self,other):                           # +
		new_den=self.den*other.den
		new_num=self.num*other.den+self.den*other.num
		
		common=GCD(new_den,new_num)
		
		modify_den=new_den/common
		modify_num=new_num/common
		
		return str(modify_num) +'/'+str(modify_den)
		
	
	def __sub__(self,other):                           # -
		new_den=self.den*other.den
		new_num=self.num*other.den-self.den*other.num
		
		common=GCD(new_den,new_num)
		
		modify_den=new_den/common
		modify_num=new_num/common
		
		return str(modify_num) +'/'+str(modify_den)
		
		
	def __mul__(self,other):                           # *
		new_den=self.den*other.den
		new_num=self.num*other.num
		
		common=GCD(new_den,new_num)
		
		modify_den=new_den/common
		modify_num=new_num/common
		
		return str(modify_num) +'/'+str(modify_den)
		
		
	def __truediv__(self,other):                       # /
		new_den=self.den*other.num
		new_num=self.num*other.den
		
		common=GCD(new_den,new_num)
		
		modify_den=new_den/common
		modify_num=new_num/common
		
		return str(modify_num) +'/'+str(modify_den)
	
	def check(self):
		if type(self.den) is int and type(self.num) is int:
			return True
		
		else:
			raise RuntimeError('not both numerator and denominator are integers')
			
f1=fraction(6,8)
print f1
print f1.getNum()
print f1.getDen()


# 2.In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
def GCD(a,b):
	while a%b!=0:
		olda=a
		oldb=b
		a=oldb
		b=olda%oldb
	
	return b

	
f2=fraction(5,12)
print f1+f2


# 3.Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).
print f1-f2
print f1*f2
print f1.__truediv__(f2)


# 4.Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)
# gt(a, b) is equivalent to a > b 
# ge(a, b) is equivalent to a >= b
# lt(a, b) is equivalent to a < b
# le(a, b) is equivalent to a <= b
# ne(a, b) is equivalent to a != b

class rich_comparisons:
	def __init__(self,n,m):
		self.num=n
		self.den=m
	
	def __str__(self):
		return str(self.num)+'/'+str(self.den)
		
	def getNum(self):
		return self.num
		
	def getDen(self):
		return self.den
		
	def __gt__(self,other):                           # >
		new_num1=self.num*other.den
		new_num2=self.den*other.num

		return new_num1>new_num2
		
r1=rich_comparisons(6,8)
r2=rich_comparisons(5,12)
print r1>r2


# 5.Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer the constructor should raise an exception.
f1.check()

#~ f3=fraction(3.4,5.5)
#~ f3.check()


# 6.In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.
f4=fraction(4,-5)
f5=fraction(-2,-9)

print f4         # -4/5
print f5         # 2/9


# 7.Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.
# reversed add


# 8.Repeat the last question but this time consider the __iadd__ method.
# +=


# 9.Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.
# return "%s(%r)" % (self.__class__, self.__dict__)


