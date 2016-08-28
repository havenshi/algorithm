# 15.Find a Sudoku puzzle in the local newspaper. Write a program to solve the puzzle.
import random


class Su:
	# properties
	row_names = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	col_names = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	# two attributes of suit and rank number
	def __init__(self, row, col,output = None):
		self.row = row
		self.col = col
		self.output = output
		
	def getRow(self):
		return self.row
		
	def getCol(self):
		return self.col
		
	def getOutput(self):
		self.output = self.performTableLogic()
		return self.output
		
	def __str__(self):
		return 'E[%d,%d] is %s' % (self.row,self.col,str(self.output))
		
#~ su11=Su(1,1,4)
#~ print su11

class EachSu(Su):
	def __init__(self,row,col,output = None):
		Su.__init__(self,row,col,output = None) 
	
	def performTableLogic(self):
		i=self.getRow()
		j=self.getCol()
		if init[i-1][j-1]!=None:
			return init[i-1][j-1]
		else:
			return 99
			
	#~ def assign(self):
		#~ row_alist=[1,2,3,4,5,6,7,8,9]
		#~ col_alist=[1,2,3,4,5,6,7,8,9]
		#~ for i in [1,2,3,4,5,6,7,8,9]:
			#~ 
		#~ row_alist.pop(self.getRow)
		#~ col_alist=	



#~ Step 2: insert initial non-empty value to table
#~ i=self.getRow()
#~ j=self.getCol()
#~ if init[i-1][j-1]!=None:
	#~ return init[i-1][j-1]
#~ else:
	#~ return 0

# Step 1: test if call performTableLogic successfully
#~ if self.getRow()==1 and self.getCol()==1:
	#~ return 4
#~ else:
	#~ return 5

#~ susu=EachSu(1,2)
#~ print susu
#~ E[1,2] is None
#~ print susu.getOutput()
#~ 5


class Table:
	def __init__(self):
		self.sus = []
		for row in range(1,10):
			rows=[]
			for col in range(1,10):
				eachsu=EachSu(row,col,output = None)
				rows.append(eachsu.getOutput())
			self.sus.append(rows)
	
	def __str__(self):
		return str(self.sus)


init=[[5, 3, None, None, 7, None, None, None, None], 
      [6, None, None, 1, 9, 5, None, None, None], 
      [None, 9, 8, None, None, None, None, 6, None], 
      [8, None, None, None, 6, None, None, None, 3], 
      [4, None, None, 8, None, 3, None, None, 1], 
      [7, None, None, None, 2, None, None, None, 6], 
      [None, 6, None, None, None, None, 2, 8, None], 
      [None, None, None, 4, 1, 9, None, None, 5], 
      [None, None, None, None, 8, None, None, 7, 9]]




table=Table()
print table


