class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None
        
	def isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()

		return count
		
	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:                      
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()		
	# same as unorderedlist
	
	
	def add(self,item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()

    temp = Node(item)
    if previous == None: # when found at first, previous is still None, add before head
        temp.setNext(self.head)
        self.head = temp
    else:                # when found at first, previous is still None, add between previous and current
        temp.setNext(current)
        previous.setNext(temp)

	        
    def search(self,item):
		current = self.head
		found = False
		stop = False
		
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()

		return found
