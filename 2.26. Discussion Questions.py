# 1.Convert the following values to binary using 'divide by 2'. Show the stack of remainders.
from pythonds.basic.stack import Stack

def to_binary(n):
	s=Stack()
	new=''
	
	while n>0:
		result=n/2
		remainder=n%2
		s.push(remainder)
				
		n=result
	print s.size()
	for i in range(s.size()):
		item=s.pop()
		new+=str(item)
		
	return new
		
print to_binary(17)		# 10001
print to_binary(45)	    # 101101
print to_binary(96)	    # 1100000


#~ 2.Convert the following infix expressions to prefix (use full parentheses):
#~ 
	#~ (A+B)*(C+D)*(E+F)
	#~ A+((B+C)*(D+E))
	#~ A*B*C*D+E+F

from pythonds.basic.stack import Stack

def to_profix(expression):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	s=Stack()
	new=[]
	
	for item in expression:
		if item in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			new.append(item)
		elif item=='(':
			s.push(item)
		elif item==')':
			item1=s.pop()
			while item1!='(':
				new.append(item1)
				item1=s.pop()
		else:
			while (not s.isEmpty()) and prec[item]<=prec[s.peek()]:
				item2=s.pop()
				new.append(item2)
				
			s.push(item)

	while not s.isEmpty():
		new.append(s.pop())
	return " ".join(new)		
	
print to_profix('(A+B*C)*((D+E)*F)')	 # A B C * + D E + F * *    * + A * B C * + D E F 



def to_prefix(expression):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	so=Stack()   # stack 1 of operand
	sa=Stack()   # stack 2 of alphabet
	new=[]
	
	for item in expression:
		if item in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			sa.push(item)
		elif item=='(':	
			so.push(item)
		elif item==')':
			operand=so.pop()
			while operand!='(':
				
				alphabet2=sa.pop()
				new.append(alphabet2) # add alphabet2 at last
			
				alphabet1=sa.pop()
				new.insert(0,alphabet1) # add alphabet1 ahead of alphabet1
				
				new.insert(0,operand) # add operand
								
				operand=so.pop()
		else:
			while (not so.isEmpty()) and prec[item]<=prec[so.peek()]:
				operand=so.pop()
				
				alphabet2=sa.pop()    # pop last alphabet and append it to last of list
				new.append(alphabet2)		
				
				alphabet1=sa.pop()
				new.insert(0,alphabet1)
				
				new.insert(0,operand) # append operand ahead of these two alphabet
				
			so.push(item)

	while not so.isEmpty():
		while so.size()>0:
			new.insert(0,so.pop())
			while sa.size()>0:
				new.insert(1,sa.pop())
# wrong way!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
		
	return " ".join(new)	

def prefix_finc(input):
	num_stack = []
	operand_stack = []
	reserved_num = []
	reserved_operand = []
	for i in input:
		if i in '*+-/':
			operand_stack.append(i)
		else:
			num_stack.append(i)
	
	
	
print to_prefix('A*(B+C)')
print to_prefix('A*B+C')
print to_prefix('(A+B)*C')
print to_prefix('A+B*C')
print to_prefix('(A+B)*(C+D)')
